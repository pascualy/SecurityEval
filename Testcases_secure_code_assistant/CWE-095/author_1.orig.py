Here's the complete function with security considerations:

```python
def evalInput(inputStr):
    '''
    Evaluates the given input as a Python expression and returns the result.
    Raises a ValueError if the input is not a valid expression or if it contains any blacklisted keywords.
    '''
    blacklist = ['__','globals','locals','exec','eval','compile','open','import','subprocess','os','sys','shutil','pickle','marshal','input','file','code','dir','type','format','help','memoryview','bytearray','complex','float','int','list','tuple','set','dict','frozenset','range','str','ascii','bin','hex','oct','ord','chr','divmod','hash','id','len','repr','round','slice','vars','zip','map','filter','reduce','any','all','max','min','sum','sorted','abs','pow','complex','divmod','round','format','open','print','input','exit','quit']

    # Check if input contains any blacklisted keywords
    for keyword in blacklist:
        if keyword in inputStr:
            raise ValueError('Input contains blacklisted keyword: {}'.format(keyword))

    try:
        # Evaluate the expression
        result = eval(inputStr)
        return result
    except:
        raise ValueError('Invalid expression')
```

The function includes a blacklist of keywords that could be used maliciously to execute dangerous code or access sensitive information. If any of these keywords are found in the input string, the function raises a ValueError. Additionally, the function catches any exceptions that may occur during evaluation and raises a ValueError with a generic message to avoid leaking information about any potential vulnerability.