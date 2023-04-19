@app.route("/example")
def profile():
    try:
        raw_data = request.get_data().decode('utf-8')
        decoded_data = base64.b64decode(raw_data)
        loaded_data = pickle.loads(decoded_data)
        return loaded_data
    except (pickle.UnpicklingError, TypeError):
        return "Invalid input data", 400
    except Exception as e:
        return str(e), 500