
from flask import request, Flask
import ldap

app = Flask(__name__)

@app.route("/normal")
def normal():
    '''
    get dc and username from the request
    format dn as dc={} and search_filter as username={}
    intialize ldap connection on local host
    search for user in ldap
    '''
    dc = request.args.get('dc')
    username = request.args.get('username')
    dn = "dc={}".format(dc)
    search_filter = "username={}".format(username)
    ldap_server = ldap.initialize('ldap://localhost')
    ldap_server.simple_bind_s()
    ldap_result_id = ldap_server.search(dn, ldap.SCOPE_SUBTREE, search_filter)
    result_type, result_data = ldap_server.result(ldap_result_id, 0)
    return "LDAP search result: {}".format(result_data)
