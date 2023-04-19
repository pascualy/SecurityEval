def normal():
    # get dc and username from the request
    dc = request.args.get('dc')
    username = request.args.get('username')

    # format dn as dc={} and search_filter as username={}
    dn = "dc={}".format(dc)
    search_filter = "username={}".format(username)

    # initialize ldap connection on local host
    try:
        conn = ldap.initialize('ldap://localhost')
    except ldap.LDAPError as e:
        return "Error connecting to LDAP: {}".format(e)

    # search for user in ldap
    try:
        result = conn.search_s(dn, ldap.SCOPE_SUBTREE, search_filter)
    except ldap.LDAPError as e:
        return "Error searching in LDAP: {}".format(e)

    return result