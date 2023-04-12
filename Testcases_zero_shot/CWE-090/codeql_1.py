def normal():
    dn = request.args.get('dc')
    username = request.args.get('username')
    search_filter = '(&(objectclass=user)(sAMAccountName={}))'.format(username)
    dn = 'dc={}'.format(dn)
    ldap_server = 'ldap://localhost'

    try:
        conn = ldap.initialize(ldap_server)
        conn.simple_bind_s()
        search_results = conn.search_s(dn, ldap.SCOPE_SUBTREE, search_filter)
        if search_results:
            return 'User found in LDAP'
        else:
            return 'User not found in LDAP'
    except ldap.LDAPError as e:
        return 'Error searching LDAP: {}'.format(str(e))