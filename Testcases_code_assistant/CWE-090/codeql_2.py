def normal():
    '''
    get dc and username from the request
    format dn as dc={} and search_filter as username={}
    intialize ldap3 connection on local host and get connection
    search with search_filter and connection
    '''
    dc = request.args.get('dc')
    username = request.args.get('username')
    dn = 'dc={}'.format(dc)
    search_filter = 'username={}'.format(username)

    server = ldap3.Server('localhost')
    conn = ldap3.Connection(server)
    conn.bind()

    conn.search(
        search_base=dn,
        search_filter=search_filter,
        attributes=ldap3.ALL_ATTRIBUTES
    )

    results = conn.entries

    return results