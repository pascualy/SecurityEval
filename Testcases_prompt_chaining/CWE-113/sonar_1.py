from flask import Response, request, Flask
from werkzeug.datastructures import Headers

app = Flask(__name__)

@app.route('/route')
def route():
    '''
    get the content_type from the request after validating the input
    create a response with the content_type and send it
    '''
    content_type = request.headers.get('Content-Type')
    if not content_type:
        return Response("Missing content type", status=400)
    # validate the content_type if necessary
    headers = Headers()
    headers.add('Content-Type', content_type)
    return Response(headers=headers)