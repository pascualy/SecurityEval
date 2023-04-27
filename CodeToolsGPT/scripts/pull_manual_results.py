import requests
import csv
import io
from pathlib import Path
import json


def pull_results(document_token='1t-C62ofKSBBkV1bjoB5A4BYQ_1AY1MYQc3mv15dKf7o'):
    response = requests.get(f'https://docs.google.com/spreadsheet/ccc?key={document_token}&output=csv')
    response.raise_for_status()
    
    csv_string = response.content.decode()
    csv_buffer = io.StringIO(csv_string)
    csv_buffer.readline()

    result_types = ['CA Result', 'SCA Result', 'PC Result']
    manual_results = {}

    for row in csv.DictReader(csv_buffer):
        if len(row['CWEID']):
            for rt in result_types:
                manual_results.setdefault(row['CWEID'], {})
                manual_results[row['CWEID']].setdefault(row['Filename'], {})
                manual_results[row['CWEID']][row['Filename']][rt] = row[rt]

    with open(Path(__file__).parent / 'manual_results.json', 'w') as fp:
        fp.write(json.dumps(manual_results, indent=2))

    with open(Path(__file__).parent / 'manual_results.csv', 'w') as fp:
        fp.write(csv_string)

pull_results()
