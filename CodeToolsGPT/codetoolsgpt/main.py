import argparse
import json
import logging
import re
import csv

from pathlib import Path
from typing import List, Dict

from codetoolsgpt.evaluate import evaluate_methods
from codetoolsgpt.generate import generate_methods
from codetoolsgpt.utils import get_project_root


# Set up logging configuration
logging.basicConfig(level=logging.INFO,
                    format='%(message)s',
                    # format='%(asctime)s - %(levelname)s - %(message)s',
                    handlers=[logging.StreamHandler(),
                              logging.FileHandler('crawler.log', mode='a')])

log = logging.getLogger(__name__)


def output_generate_results(output_path: str, test_name: str, results: List[Dict[str, str]]):
    test_cases_dir = Path(output_path / f'Testcases_{test_name}')
    test_cases_dir.mkdir(exist_ok=True)

    for result in results:
        cwe = result['CWE']
        prefix_dir = test_cases_dir / cwe
        prefix_dir.mkdir(exist_ok=True)

        output_file = prefix_dir / result['filename']

        with output_file.open('w') as file:
            file.write(result['generated_code'])

def add_result(results, testgroup, testname, method, result):
    results.setdefault(testgroup, {})
    results[testgroup].setdefault(testname, {})
    results[testgroup][testname].setdefault(method, set())
    try:
        cwe_num = int(result)
    except ValueError:
        cwe_num = int(result.split('-')[1])

    results[testgroup][testname][method].add(cwe_num)


def load_test(path: Path):
    reader = csv.DictReader(path.open())

    multi_level_dict = {}

    for row in reader:
        cwe = row.pop('CWEID')
        sample_id = row.pop('SampleID')
        
        if cwe not in multi_level_dict:
            multi_level_dict[cwe] = {}
        
        multi_level_dict[cwe][sample_id] = {k.lower(): v for k,v in row.items() if k in ['CodeQL', 'Bandit']}
    
    return multi_level_dict


def summarize_results(output_path: Path, generate_method: str, input_path: Path):
    results = {}
    # Special result paths/formats for codeql and bandit
    codeql_result = input_path / f'testcases_{generate_method}'
    bandit_result = input_path / f'testcases_{generate_method}.json'

    # Standard result paths/formats for codetoolsgpt evaluators
    for evaluate_method in [ce for ce in evaluate_methods.keys() if ce not in ['codeql', 'bandit']]:
        custom_result = input_path / f'testcases_{generate_method}_{evaluate_method}.json'
        try:
            with custom_result.open() as fp:
                for result in json.loads(fp.read()):
                    for detected_cwe in result['detected_cwes']:
                        add_result(results, result['CWE'], result['filename'], evaluate_method, detected_cwe)
        except FileNotFoundError as e:
            log.error(f"No results found for following generate/evaluate pair: {generate_method}/{evaluate_method}")

    for result in codeql_result.iterdir():
        cwe_num = result.stem.split('_')[-1]
        with result.open() as fp:
            testcases = re.findall('/CWE-[0-9]+/[a-z]+_[0-9]+.py', fp.read())

        for tc in testcases:
            folder, file = tc.split('/')[-2:]
            add_result(results, folder, file, 'codeql', cwe_num)

    with bandit_result.open() as fp:
        for result in json.loads(fp.read())['results']:
            folder, file = result['filename'].split('/')[-2:]
            add_result(results, folder, file, 'bandit', result['issue_cwe']['id'])

    methods = [a for a in list(sorted(evaluate_methods.keys())) if a not in ['codeql', 'bandit']] + ['Bandit', 'CodeQL']
    # header = ['CWEID', 'SampleID', 'Modified'] + methods + ['Manual']
    header = ['CWEID', 'SampleID'] + methods + ['Manual']  # Remove modified field
    output_filename = f'testcases_{generate_method}.csv'
    rows = []

    with open(input_path / 'testcases.json') as fp:
        directories = json.load(fp)[0]['contents']

    with open(get_project_root() / 'scripts' / 'manual_results.json') as fp:
        manual_results = json.load(fp)

    mapping = {
       "code_assistant": "CA Result",
       "secure_code_assistant": "SCA Result",
       "prompt_chaining": "PC Result" 
    }

    for directory in directories:
        cwe_num = directory['name']

        for file in directory['contents']:
            filename = file['name']

            method_results = results.get(cwe_num, {}).get(filename, {})
            # row = [cwe_num, filename, '_'] # remove modified field
            row = [cwe_num, filename]
            for method in methods:
                method = method.lower()
                if method in method_results and int(cwe_num.split('-')[1]) in method_results[method]:
                    cell = 1
                else:
                    cell = 0
                
                row.append(cell)
            
            try:
                manual_result = manual_results[cwe_num][filename][mapping[generate_method]] 
                row.append(0 if manual_result == 'Secure' else 1) # Manual method
            except KeyError as e:
                print(f'Manual Result not found {(cwe_num, filename, generate_method, mapping[generate_method])}')
                raise e
            
            rows.append(row)
                                   
    with open(output_path / output_filename, 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(rows)

    return output_path / output_filename

def add_method_argument(parser, methods, help_text):
    parser.add_argument(
        "-m",
        "--method",
        type=str,
        choices=methods,
        required=True,
        help=help_text,
    )


def main():
    parser = argparse.ArgumentParser(description="Process JSONL file or dictionary input")
    subparsers = parser.add_subparsers(dest="command", required=True)

    summarize_parser = subparsers.add_parser("summarize", help="Generate summary file of results")
    add_method_argument(summarize_parser, list(generate_methods.keys()) + ['copilot', 'incoder'], "Choose the method to summarize the results for.")

    generate_parser = subparsers.add_parser("generate", help="Generate code examples from prompts")
    add_method_argument(generate_parser, list(generate_methods.keys()), "Choose the method to use for generate.")

    evaluate_parser = subparsers.add_parser("evaluate", help="Evaluate the security of the provided code")
    add_method_argument(evaluate_parser, list(evaluate_methods.keys()), "Choose the method to use for evaluate.")

    for subparser in (generate_parser, evaluate_parser, summarize_parser):
        subparser.add_argument("-d", "--directory", type=Path, required=True, help="Path to the test directory")
        subparser.add_argument(
            "-o",
            "--output",
            type=Path,
            default=None,
            required=True,
            help="File path to save the output. If not provided, output will be printed to stdout.",
        )
        subparser.add_argument('-v', '--verbose', action='store_true', help='Increase output verbosity')
        subparser.add_argument('-c', "--cwe-list", type=str, default="", help="Comma-separated list of CWE numbers to generate or evaluate (e.g., 102,329)")
    
    args = parser.parse_args()

    # Set logging level based on verbosity flag
    log.setLevel(logging.DEBUG if args.verbose else logging.INFO)

    # Handle external evaluation methods
    if args.command == "evaluate" and args.method in ['bandit', 'codeql']:
        evaluate_methods[args.method](args.output, args.directory)
    elif args.command == 'summarize':
        summarize_results(args.output, args.method, args.directory)
    else:

        cwe_list = [f"CWE-{num.strip()}" for num in args.cwe_list.split(",") if num.strip()]

        input_data = []
        for cwe in args.directory.iterdir():
            if (len(cwe_list) and cwe.name not in cwe_list) or cwe.name.startswith('.'):
                continue

            for file in cwe.iterdir():
                with open(file) as fp:
                    input_data.append({"CWE": cwe.name, "filename": file.name, "code": fp.read()})

        if args.command == "generate":
            results = generate_methods[args.method](input_data)
            if args.output:
                output_generate_results(output_path=args.output, test_name=args.method, results=results)
        
        elif args.command == 'evaluate':
            filename = Path(str(args.directory.name).lower() + f'_{args.method.lower()}.json')
            
            results = []
            results_set = set()
            if (args.output / filename).exists():
                with open(args.output / filename) as fp:
                    results = json.loads(fp.read())
                    results_set = set([(l['CWE'], l['filename']) for l in results])
            
            input_data = [inn for inn in input_data if (inn['CWE'], inn['filename']) not in results_set]

            results_generator = evaluate_methods[args.method](input_data)
            
            for result in results_generator:
                results.append(result)

                if args.output:
                    with open(args.output / filename, 'w') as fp:
                        fp.write(json.dumps(results))

        if not args.output:
            print(json.dumps(results, indent=2))


if __name__ == "__main__":
    main()
