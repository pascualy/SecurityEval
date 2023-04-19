Here is an example of a middleware class that can be used in a Django application:

```python
class MyMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        
        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response
```

In this example, `MyMiddleware` is the middleware class. The `__init__` method takes `get_response` as a parameter, which is a callable that takes a request and returns a response. It sets `get_response` as an instance variable so it can be used later.

The `__call__` method is called for each request. It takes a request as a parameter and returns a response. The middleware logic is contained within this method. In this example, the middleware does not modify the request or response but simply calls the next middleware in the chain by invoking `self.get_response(request)` and returns the response.

To use this middleware, add its path to the `MIDDLEWARE` setting in your Django settings file. For example:

```python
MIDDLEWARE = [
    # ...
    'path.to.MyMiddleware',
    # ...
]
```