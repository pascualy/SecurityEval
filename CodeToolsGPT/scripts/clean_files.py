import os
import re

def process_files(path):
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith('.py'):
                with open(os.path.join(root, file), 'r') as f:
                    content = f.read()
                
                # Check if there is an explanation in the file
                if "```python" in content:
                    # Create a new file with .orig.py extension
                    new_file = os.path.join(root, file[:-3] + ".orig.py")
                    with open(new_file, 'w') as nf:
                        nf.write(content)

                    # Remove the explanation and keep only the code between ```
                    code = re.findall(r'```python(.*?)```', content, re.DOTALL)
                    code_str = "".join(code)

                    # Write the extracted code back to the original file
                    with open(os.path.join(root, file), 'w') as f:
                        f.write(code_str)

# Replace 'Result' with the path to your actual directory
process_files('./Testcases_code_assistant')
