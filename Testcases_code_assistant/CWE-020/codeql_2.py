def profile():
    raw_data = request.data.decode('utf-8')
    decoded_data = base64.b64decode(raw_data)
    loaded_data = pickle.loads(decoded_data)
    return loaded_data

@app.route("/example", methods=['POST'])
def example():
    return profile()