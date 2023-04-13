from codetoolsgpt.utils import get_project_root
import requests
import pathlib
import json
import tqdm

url_template = 'https://cwe.mitre.org/data/definitions/{cwe_number}.html'

result = {}

for dir_name in tqdm.tqdm(list((get_project_root().parent / 'Testcases_Prompt').iterdir())):
    cwe_number = int(dir_name.name.split('-')[1])
    n = requests.get(url_template.format(cwe_number=cwe_number))
    al = n.text
    title = al[al.find('<title>') + 7 : al.find('</title>')]
    title = title[title.find('CWE-'):]
    k, v = title.split(':', 1)
    result[k.strip()] = v.strip()

with open(pathlib.Path(__file__).parent / 'cwe_titles.json', 'w') as fp:
    fp.write(json.dumps(result, indent=4))
