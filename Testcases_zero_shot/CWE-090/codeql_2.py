def normal():
    # Get dc and username from the request
    dc = request.args.get('dc')
    username = request.args.get('username')
    
    # Format dn as dc={} and search_filter as username={}
    dn = "dc={}".format(dc)
    search_filter = "username={}".format(username)
    
    # Initialize ldap3 connection on local host and get connection
    server = ldap3.Server('localhost')
    conn = ldap3.Connection(server)
    conn.bind()
    
    # Search with search_filter and connection
    conn.search(dn, search_filter)
    result = conn.entries
    conn.unbind()
    
    return result