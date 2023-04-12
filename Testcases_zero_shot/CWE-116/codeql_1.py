import re

def filterScriptTags(content): 
    '''
    remove script tags from content argument
    '''
    script_regex = re.compile(r'<script\b[^>]*>(.*?)</script>', flags=re.DOTALL)
    return script_regex.sub('', content)