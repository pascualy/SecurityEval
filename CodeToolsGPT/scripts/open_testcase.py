# Usage: 
# cd CodeToolsGPT
# python scripts/open_testcase.py CWE-643 codeql_1.py

import os
import subprocess
import sys
from pathlib import Path

def open_files_in_vscode(cwe, name):
    file_path_1 = Path(f"../Testcases_code_assistant/{cwe}/{name}")    
    file_path_2 = Path(f"../Testcases_secure_code_assistant/{cwe}/{name}")
    file_path_3 = Path(f"../Testcases_prompt_chaining/{cwe}/{name}")
    file_path_4 = Path(f"../Testcases_Insecure_Code/{cwe}/{name}")

    if os.path.exists(file_path_1) and os.path.exists(file_path_2):
        subprocess.run(["code", file_path_1, file_path_2, file_path_3, file_path_4])
    else:
        print('\n'.join([file_path_1, file_path_2, file_path_3, file_path_4]))
        print("One or both of the file paths do not exist. Please check the file paths and try again.")


if __name__ == "__main__":
    open_files_in_vscode(sys.argv[1], sys.argv[2])