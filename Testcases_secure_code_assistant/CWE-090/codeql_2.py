app = Flask(__name__)

@app.route("/normal")
def normal():
    # get dc and username from the request
    dc = request.args.get('dc')
    username = request.args.get('username')

    # format dn as dc={} and search_filter as username={}
    dn = "dc={}".format(dc)
    search_filter = "username={}".format(username)

    # initialize ldap3 connection on local host and get connection
    server = ldap3.Server('localhost')
    conn = ldap3.Connection(server)

    # search with search_filter and connection
    conn.search(dn, search_filter)

    return "Done"