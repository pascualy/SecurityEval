import re

def filterScriptTags(content): 
    '''
    remove script tags from content argument
    '''
    script_pattern = re.compile(r'<script.*?>.*?</script>', re.DOTALL) # pattern to match script tag
    content = script_pattern.sub('', content) # remove script tag from content
    return content