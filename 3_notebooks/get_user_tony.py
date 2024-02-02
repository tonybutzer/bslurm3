import ldap

# Define LDAP server details
ldap_server = "ldap://localhost"
bind_dn = "cn=ldapadm,dc=pcluster,dc=com"  # The bind DN with enough privileges to perform the search
bind_password = "yaml"

# User's base DN
user_base_dn = "uid=tony,ou=People,dc=pcluster,dc=com"
# user_base_dn = "dn: cn=lpadmin,dc=pcluster,dn=com"


# Initialize LDAP connection
ldap_conn = ldap.initialize(ldap_server)
#ldap_conn.simple_bind_s(bind_dn, bind_password)

try:
    # Bind with admin credentials
    ldap_conn.simple_bind_s(bind_dn, bind_password)

    # Retrieve DIT info for the user
    search_result = ldap_conn.search_s(user_base_dn, ldap.SCOPE_BASE)
    print(search_result)

    if search_result:
        user_dn, user_info = search_result[0]

        print(f"Distinguished Name (DN): {user_dn}")
        print("Attributes:")

        # Print all attributes and their values
        for attr, value in user_info.items():
            print(f"  {attr}: {value}")
    else:
        print(f"User {user_base_dn} not found")

except ldap.INVALID_CREDENTIALS:
    print("Invalid credentials")
except ldap.LDAPError as e:
    print(f"LDAP Error: {e}")
finally:
    # Unbind the connection
    ldap_conn.unbind()

