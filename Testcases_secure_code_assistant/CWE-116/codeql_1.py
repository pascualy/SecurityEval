import re

def filterScriptTags(content): 
    '''
    remove script tags from content argument
    '''
    clean_content = re.sub(r'<script\b[^<]*(?:(?!<\/script>)<[^<]*)*<\/script>', '', content, flags=re.IGNORECASE)
    return clean_content