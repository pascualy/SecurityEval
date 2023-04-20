from flask import request, Flask
import ldap3

app = Flask(__name__)

@app.route("/normal")
def normal():
    dc = request.args.get('dc')
    username = request.args.get('username')
    
    dn = "dc={}".format(dc)
    search_filter = "username={}".format(username)
    
    server = ldap3.Server('localhost')
    conn = ldap3.Connection(server)
    
    conn.search(dn, search_filter)
    
    return "Search completed successfully."