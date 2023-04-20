import re
from html import escape

def filterScriptTags(content): 
    '''
    remove script tags from content argument
    '''
    content = re.sub(r'<script\b[^<]*(?:(?!<\/script>)<[^<]*)*<\/script>', '', content)
    content = escape(content)
    return content