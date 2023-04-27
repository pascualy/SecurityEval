import subprocess
import pathlib
import os
from pathlib import Path
import textwrap
import requests


def get_project_root() -> Path:
    """Get the project root directory as a pathlib.Path object.

    Returns:
        Path: The project root directory.
    """    
    return Path(__file__).parent.parent


def format_chat(messages):
    return "\n".join([f"{d['role'].upper()}:\n{textwrap.indent(d['content'], '    ')}"for d in messages])


def run_bandit_eval(output_path: str, input_path: str):
    """Run Bandit evaluation on the given input path.

    Args:
        output_path (str): The path to store the Bandit output.
        input_path (str): The path to the input files to be analyzed.
    """
    output_filepath = (output_path / pathlib.Path(input_path).name.lower()).with_suffix('.json')

    try:
        subprocess.call('bandit', shell=True)
    except subprocess.SubprocessError as e:
        print(f'Could not find bandit. Please install. {e}')
        return
    
    subprocess.call(f'bandit -r {input_path} -f json -o {output_filepath}', shell=True)


def run_codeql_eval(output_path: str, input_path: pathlib.Path):
    """Run CodeQL evaluation on the given input path.

    Args:
        output_path (str): The path to store the CodeQL output.
        input_path (pathlib.Path): The path to the input files to be analyzed.
    """
    codeql_cmd = pathlib.Path(os.environ['CODEQL_PATH']) / 'codeql'
    directory_name = input_path.name
    test_name = '_'.join(directory_name.lower().split('_')[1:])

    def codeql_module_path(cwe: str) -> str:
        prefix = f"{os.environ['CODEQL_REPO_PATH']}/python/ql/src/Security/"
        return os.path.join(prefix, cwe)

    original_cwd = os.getcwd()

    try:
        # cd into input_path
        os.chdir(input_path)

        # run codeql database creation command
        database_path = get_project_root() / '..' / 'Databases'
        database_directory_name = directory_name + '_DB'
        subprocess.run([codeql_cmd, "database", "create", "--language=python", str(database_path / database_directory_name)])

        # cd into Databases
        os.chdir(database_path)

        # generate bash script with current folder as database path
        no_queries_found = []
        with open(f"job_{test_name}.sh", "w") as f:
            f.write("#!/bin/bash\n")

            # for each CWE (specified in the subdirectories in the input_path)
            output_dir = Path(output_path) / directory_name
            output_dir.mkdir(exist_ok=True)
            for subdir in input_path.iterdir():
                if not pathlib.Path(codeql_module_path(subdir.name)).exists():
                    no_queries_found.append(subdir.name)
                    continue
                
                subdir_path = os.path.join(input_path, subdir)
                if os.path.isdir(subdir_path):
                    # call codeql in the following way
                    output_file = output_dir / f"results_{'_'.join(subdir.name.lower().split('-'))}.csv"
                    codeql_command = f'{codeql_cmd} database analyze "{database_directory_name}" {codeql_module_path(subdir.name)} --format=csv --output="{output_file}"\n'
                    f.write(codeql_command)
        
        if no_queries_found:
            print(f'No queries found for [{", ".join(no_queries_found)}]')

        # run the generated bash script
        subprocess.run(["bash", f"job_{test_name}.sh"])
    finally:
        # restore the original working directory
        os.chdir(original_cwd)
