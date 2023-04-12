import subprocess
import pathlib
import os

from typing import Dict, List

from codetoolsgpt.utils import get_project_root


def zero_shot(jsonl_data: List[Dict[str, str]]) -> Dict[str, str]:
    # Evaluate the security of the "Insecure_code" in each dictionary
    # Replace this function with your actual implementation
    
    results = [] # Perform security evaluation on input_data and store the results in this dictionary
    for item in jsonl_data:
        results.append({**item, 'results': 'This is the evaluation.'})

    return results


def run_bandit_eval(output_path: str, input_path: str):
    output_filepath = (output_path / pathlib.Path(input_path).name.lower()).with_suffix('.json')

    try:
        subprocess.check_output('bandit')
    except subprocess.SubprocessError as e:
        print(f'Could not find bandit. Please install. {e}')
        return
    
    subprocess.check_output(f'bandit -r {input_path} -f json -o {output_filepath}')


def run_codeql_eval(output_path: str, input_path: pathlib.Path):
    
    codeql_path = os.environ['CODEQL_PATH']
    codeql_repo_path = os.environ['CODEQL_REPO_PATH']
    codeql_cmd = pathlib.Path(codeql_path) / 'codeql'
    directory_name = input_path.name
    test_name = '_'.join(directory_name.lower().split('_')[1:])

    def codeql_module_path(cwe: str) -> str:
        prefix = f"{codeql_repo_path}/python/ql/src/Security/"
        return os.path.join(prefix, cwe)

    original_cwd = os.getcwd()

    try:
        # cd into input_path
        os.chdir(input_path)

        # run codeql database creation command
        database_path = get_project_root() / '..' / 'Databases'
        database_directory_name = directory_name + '_DB'
        subprocess.run([codeql_cmd, "database", "create", "--language=python", os.path.join(database_path, database_directory_name)])

        # cd into Databases
        os.chdir(database_path)

        # generate bash script with current folder as database path
        with open(f"job_{test_name}.sh", "w") as f:
            f.write("#!/bin/bash\n")

            # for each CWE (specified in the subdirectories in the input_path)
            pathlib.Path(os.path.join(output_path, directory_name)).mkdir(exist_ok=True)
            for subdir in os.listdir(input_path):
                if not pathlib.Path(codeql_module_path(subdir)).exists():
                    print(f'Could not find {subdir} codeql module.')
                    continue
                
                subdir_path = os.path.join(input_path, subdir)
                if os.path.isdir(subdir_path):
                    # call codeql in the following way
                    output_file = os.path.join(output_path, directory_name, f"results_{'_'.join(subdir.lower().split('-'))}.csv")
                    codeql_command = f'{codeql_cmd} database analyze "{database_directory_name}" {codeql_module_path(subdir)} --format=csv --output="{output_file}"\n'
                    f.write(codeql_command)

        # run the generated bash script
        subprocess.run(["bash", f"job_{test_name}.sh"])
    finally:
        # restore the original working directory
        os.chdir(original_cwd)



evaluate_methods = {"zero_shot": zero_shot, "bandit": run_bandit_eval, "codeql": run_codeql_eval}
