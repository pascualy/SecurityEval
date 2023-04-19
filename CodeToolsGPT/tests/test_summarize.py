import csv
from pathlib import Path
from codetoolsgpt.main import summarize_results
from tempfile import TemporaryDirectory


def recursive_compare(d1, d2, level='root'):
    # https://stackoverflow.com/questions/5903720/recursive-diff-of-two-dictionaries-keys-and-values
    if isinstance(d1, dict) and isinstance(d2, dict):
        if d1.keys() != d2.keys():
            s1 = set(d1.keys())
            s2 = set(d2.keys())
            print('{:<20} + {} - {}'.format(level, s1-s2, s2-s1))
            common_keys = s1 & s2
        else:
            common_keys = set(d1.keys())

        for k in common_keys:
            recursive_compare(d1[k], d2[k], level='{}.{}'.format(level, k))

    elif isinstance(d1, list) and isinstance(d2, list):
        if len(d1) != len(d2):
            print('{:<20} len1={}; len2={}'.format(level, len(d1), len(d2)))
        common_len = min(len(d1), len(d2))

        for i in range(common_len):
            recursive_compare(d1[i], d2[i], level='{}[{}]'.format(level, i))

    else:
        if d1 != d2:
            print('{:<20} {} != {}'.format(level, d1, d2))


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


def test_summarize():
    for generate_method in ['copilot', 'incoder']:

        test_data = load_test((Path('../Result') / f'testcases_{generate_method}.csv'))  # read test data

        with TemporaryDirectory() as d:
            do = summarize_results(Path(d), generate_method, Path('../Result'))
            cand_data = load_test(do)
            recursive_compare(test_data, cand_data)

