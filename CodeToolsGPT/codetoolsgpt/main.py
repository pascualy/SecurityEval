import argparse
import json

from pathlib import Path
from typing import List, Dict

from codetoolsgpt.evaluate import evaluate_methods
from codetoolsgpt.generate import generate_methods


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

    args = parser.parse_args()

    # Handle external evaluation methods
    if args.command == "evaluate":
        if args.method == 'bandit':
            evaluate_methods[args.method](args.output, args.directory)
        elif args.method == 'codeql':
            evaluate_methods[args.method](args.output, args.directory)

    input_data = []
    for cwe in args.directory.iterdir():
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
