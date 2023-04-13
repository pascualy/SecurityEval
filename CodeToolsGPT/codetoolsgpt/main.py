import argparse
import json
import logging

from pathlib import Path
from typing import List, Dict

from codetoolsgpt.evaluate import evaluate_methods
from codetoolsgpt.generate import generate_methods


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
            

def main():
    parser = argparse.ArgumentParser(description="Process JSONL file or dictionary input")
    subparsers = parser.add_subparsers(dest="command", required=True)

    generate_parser = subparsers.add_parser("generate", help="Generate code examples from prompts")
    generate_parser.add_argument(
            "-m",
            "--method",
            type=str,
            choices=generate_methods.keys(),
            required=True,
            help="Choose the method to use for the selected subcommand.",
        )
    evaluate_parser = subparsers.add_parser("evaluate", help="Evaluate the security of the provided code")
    evaluate_parser.add_argument(
            "-m",
            "--method",
            type=str,
            required=True,
            choices=evaluate_methods.keys(),
            help="Choose the method to use for evaluate",
        )
    for subparser in (generate_parser, evaluate_parser):
        subparser.add_argument("-d", "--directory", type=Path, help="Path to the test directory")
        subparser.add_argument(
            "-o",
            "--output",
            type=Path,
            default=None,
            help="File path to save the output. If not provided, output will be printed to stdout.",
        )
        subparser.add_argument('-v', '--verbose', action='store_true', help='Increase output verbosity')
        subparser.add_argument('-c', "--cwe-list", type=str, default="", help="Comma-separated list of CWE numbers to generate or evaluate (e.g., 102,329)")
    
    args = parser.parse_args()

    # Set logging level based on verbosity flag
    log.setLevel(logging.DEBUG if args.verbose else logging.INFO)

    # Handle external evaluation methods
    if args.command == "evaluate":
        if args.method == 'bandit':
            evaluate_methods[args.method](args.output, args.directory)
        elif args.method == 'codeql':
            evaluate_methods[args.method](args.output, args.directory)

    cwe_list = [f"CWE-{num.strip()}" for num in args.cwe_list.split(",") if num.strip()]

    input_data = []
    for cwe in args.directory.iterdir():
        if len(cwe_list) and cwe.name not in cwe_list:
            continue

        for file in cwe.iterdir():
            with open(file) as fp:
                input_data.append({"CWE": cwe.name, "filename": file.name, "code": fp.read()})

    if args.command == "generate":
        results = generate_methods[args.method](input_data)
        if args.output:
            output_generate_results(output_path=args.output, test_name=args.method, results=results)
    
    elif args.command == 'evaluate':
        results_generator = evaluate_methods[args.method](input_data)
        if args.output:
            filename = Path(str(args.directory.name).lower() + f'_{args.method.lower()}.json')
            results = []
            for result in results_generator:
                results.append(result)
                with open(args.output / filename, 'w') as fp:
                    fp.write(json.dumps(results))

    if not args.output:
        print(json.dumps(results, indent=2))


if __name__ == "__main__":
    main()
