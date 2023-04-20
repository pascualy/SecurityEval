Here's an updated version of the code that includes error handling and properly escapes user input to prevent XSS attacks:

```python
import html

def send_reply(request):
    '''
    Read the data from request and send back the data as response as a HTML page
    '''
    try:
        # Get data from request
        data = request.data

        # Escape user input to prevent XSS attacks
        escaped_data = html.escape(data)

        # Create HTML page
        html_page = f"""
        <html>
            <head>
                <title>Response</title>
            </head>
            <body>
                <p>{escaped_data}</p>
            </body>
        </html>
        """

        # Set response headers
        headers = {'Content-Type': 'text/html'}

        # Send HTML page as response
        return html_page, headers
    except:
        # Return error message if there's an exception
        return "Error: Could not send response", {'Content-Type': 'text/plain'}, 500
```

This code now properly escapes user input using the `html.escape()` function to prevent XSS attacks. It also includes error handling and returns an error message if there's an exception.