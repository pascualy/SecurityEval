def normal():
    # Get dc and username from the request
    dc = request.args.get('dc')
    username = request.args.get('username')

    # Format dn as dc={} and search_filter as username={}
    dn = "dc={}".format(dc)
    search_filter = "username={}".format(username)

    # Initialize LDAP connection on local host
    ldap_server = "ldap://localhost"
    ldap_conn = ldap.initialize(ldap_server)

    # Search for user in LDAP
    ldap_conn.simple_bind_s()
    result = ldap_conn.search_s(dn, ldap.SCOPE_SUBTREE, search_filter)

    # Return the search results
    return result