# GPT Code Tools

This repository provides tools to add evaluation and generation test runs to the SecurityEval repository. SecurityEval is a project containing a dataset for evaluating machine learning-based code generation techniques, as described in the paper titled "SecurityEval Dataset: Mining Vulnerability Examples to Evaluate Machine Learning-Based Code Generation Techniques".

The provided tools in this repository will help you to perform test runs on the SecurityEval dataset using various code generation and evaluation methods. The results can then be added to the SecurityEval repository for further analysis and comparison.

## Setup

    poetry install

## Usage

There are two main subcommands in this CLI:

1. `generate`: Generate code examples from prompts
2. `evaluate`: Evaluate the security of the provided code

## Arguments
For both subcommands, the following arguments are available:

`-d` or `--directory`: Path to the test directory containing code files organized by CWE categories.

`-m` or `--method`: Choose the method to use for the selected subcommand. The choices are determined by the available methods in the codetoolsgpt.generate.generate_methods and codetoolsgpt.evaluate.evaluate_methods dictionaries.

`-o` or `--output`: File path to save the output. If not provided, output will be printed to stdout.


## Example Usage

To generate code examples using the `zero_shot` method:

    python cli.py generate -d ./Testcases_Insecure_Code -m zero_shot -o ./

To evaluate the security of the provided code using the `zero_shot` method:

    python cli.py evaluate -d ./Testcases_Inscode -m method2 -o ./Result


## Output Format

For the `generate` subcommand, the results will be saved in the specified output directory, with a folder structure based on the CWE categories and filenames derived from the input data.

For the `evaluate` subcommand, the results will be saved as a JSON file in the specified output directory. The filename will be based on the name of the test directory and the chosen evaluation method.



