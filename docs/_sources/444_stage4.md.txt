# Stage 4: Coding or Implementation.
    Stage 0: Feasibility and Concept Development
    Stage 1: Project Planning. The first stage of SDLC is all about “What do we want?” ...
    Stage 2: Gathering Requirements & Analysis. ...
    Stage 3: Design and Documentation. ...
    Stage 4: Coding or Implementation. ...
    Stage 5: Testing and Documentation. ...
    Stage 6: Deployment. ...
    Stage 7: Maintenance.

- alt174 Registered
- alt169 Copywrite - COMPLETED ©
## Reading
**https://aws.amazon.com/blogs/opensource/managing-aws-parallelcluster-ssh-users-with-openldap/**

---

- https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/6/html/deployment_guide/ch-configuring_authentication
- https://tldp.org/HOWTO/archived/LDAP-Implementation-HOWTO/pamnss.html
- https://kbr.percipio.com/books/5c6e78bc-5a7f-4bc1-905b-aafa2f06acc4/chapter/ch003#epubcfi(/6/58!/4/2%5Bepubmain%5D/2%5Bch003_s1_5%5D/2/2/1:0)
- 

## Authentication Moving Parts - too many - some old and dusty

https://community.cloudera.com/t5/Community-Articles/How-PAM-NSS-SSD-work-together-on-Linux-OS/ta-p/247879

---

** OverView **
> **LDAP** is a directory service (a type of database) along with a protocol that describes what information is stored, how to search it, etc. All kinds of things can be stored there, but in this case it'd be Unix user and group info. Very loosely, an alternative to /etc/passwd, /etc/shadow, /etc/group, and /etc/gshadow. Or to NIS.

---

> NSS is glibc's name service switch. It lets you (via /etc/nsswitch.conf) configure how various types of 'names' are resolved. Names include host names, user names, group names, and several other things. You could tell it to look up user names, group names, and passwords via LDAP instead of files.

---

> PAM handles authentication (checking who you claim you are), authorisation (grant or deny access to a given service), session setup, etc. When you're prompted for a password, that's usually PAM's doing. By editing its config you can completely customize that (e.g., you could ask for two passwords, or none at all, or a one-time password, or...). In an LDAP setup, you'd typically configure it to check passwords via the LDAP server. It also handles password changes, which you'd configure to be done in LDAP.

LDAP (Lightweight Directory Access Protocol) is a protocol used to access and maintain directory information services over a network. It's commonly used for centralized user authentication and authorization, as well as for storing other types of information like addresses, phone numbers, and more.

LDAP Authentication:
LDAP authentication is a method of validating the identity of a user or system by querying an LDAP server. When a user tries to log in, their credentials (username and password) are sent to the LDAP server. The server checks these credentials against its database and grants access if they match.

Roles of PAM, sssd, and NSS:

1. **PAM (Pluggable Authentication Modules):**
   - PAM is a framework used on Unix and Linux systems for authentication and authorization. It provides a standardized way to manage the authentication process for various applications and services.
   - PAM allows system administrators to configure different authentication methods (e.g., local files, LDAP, Kerberos) without modifying the applications themselves.
   - When it comes to LDAP authentication, PAM is responsible for interfacing with the authentication module that communicates with the LDAP server.

2. **sssd (System Security Services Daemon):**
   - sssd is a system daemon used on Linux and Unix systems for centralized identity and authentication management. It's particularly useful in environments that rely on LDAP or other identity providers.
   - sssd can cache authentication information, which reduces the load on LDAP servers and improves performance.
   - It provides services like caching of credentials, offline authentication, and user and group enumeration.

3. **NSS (Name Service Switch):**
   - NSS is a component of the GNU C Library (glibc) used on Unix and Linux systems to configure how system databases (like user accounts, groups, and hostnames) are accessed.
   - It allows system administrators to specify the sources where system information is obtained (e.g., local files, LDAP, NIS).
   - In the context of LDAP, NSS is crucial because it determines where the system looks for information about users, groups, and other entities.

The typical flow in a system with LDAP authentication, PAM, sssd, and NSS might look like this:

1. **User attempts to log in:**
   - The login request goes through PAM.

2. **PAM configuration:**
   - PAM checks its configuration to determine which authentication modules to use.

3. **PAM communicates with sssd:**
   - If LDAP authentication is configured, PAM interfaces with the appropriate module (usually provided by sssd) to query the LDAP server.

4. **sssd communicates with the LDAP server:**
   - sssd communicates with the LDAP server, passing along the user's credentials.

5. **LDAP server authentication:**
   - The LDAP server checks the credentials against its database.

6. **Authentication response:**
   - The result of the authentication is sent back through sssd, PAM, and finally, the user is either granted access or denied based on the LDAP server's response.

These components work together to enable centralized authentication and authorization in a Unix or Linux environment using LDAP.

## LDAP Coding Trials

### Build an LDAP Test Server in ws account
1. manually create terraform host ®©
2. create ship.tf and variables.tf ©
    - use hardened ec2 image - see example hosts
3. install ldap

#### install ldap
**References**
- https://linux.die.net/man/1/ldapadd
- https://help.bizagi.com/bpm-suite/en/index.html?ldap_attributes.htm
- https://www.freeipa.org/
- 

| Term    | Definition                                                                                          | Comment                                                             |
|---------|-----------------------------------------------------------------------------------------------------|---------------------------------------------------------------------|
| DIT     | Directory Information Tree                                                                          | https://ldap.com/dit-and-the-ldap-root-dse/                         |
| rootDSE | the root of the directory data tree on a directory server. The rootDSE is not part of any namespace | root DSA-specific entry (DSE)                                       |
| x       | y                                                                                                   | z                                                                   |
| x       | y                                                                                                   | z                                                                   |
| DN      | Distinguished Name                                                                                  | https://help.bizagi.com/bpm-suite/en/index.html?ldap_attributes.htm |

1. ssh ws-ldap-tester
2. sudo yum install openldap*



#### configure ldap
0. sudo bash
1. systemctl start slapd
2. systemctl enable slapd
3. slappasswd
    - yaml
    - save the hash
        - {SSHA}8XZPCTE9V7hyjwNxq9GNNW72NqRROU5N

1. cd /etc/openldap/slapd.d/cn\=config/
2. we will edit the hdb adn monitor files using LDIF files and ldapmodify

- https://www.youtube.com/watch?v=_zLeO68wZA0&t=40s

#### db.ldif

```
dn: olcDatabase={2}hdb,cn=config
changetype: modify
replace: olcSuffix
olcSuffix: dc=pcluster,dc=com

dn: olcDatabase={2}hdb,cn=config
changetype: modify
replace: olcRootDN
olcRootDN: cn=ldapadm,dc=pcluster,dc=com

dn: olcDatabase={2}hdb,cn=config
changetype: modify
replace: olcRootPW
olcRootPW: {SSHA}8XZPCTE9V7hyjwNxq9GNNW72NqRROU5N
```

1. ldapmodify -Y EXTERNAL -H ldapi:/// -f ~/db.ldif

```
[root@ip-10-12-64-214 cn=config]# ldapmodify -Y EXTERNAL -H ldapi:/// -f ~/db.ldif
SASL/EXTERNAL authentication started
SASL username: gidNumber=0+uidNumber=0,cn=peercred,cn=external,cn=auth
SASL SSF: 0
modifying entry "olcDatabase={2}hdb,cn=config"

modifying entry "olcDatabase={2}hdb,cn=config"

modifying entry "olcDatabase={2}hdb,cn=config"
```

2. edits successful
```
olcSuffix: dc=pcluster,dc=com
olcRootDN: cn=ldapadm,dc=pcluster,dc=com
```

3. monitor changes
4. monitor.ldif

```
dn: olcDatabase={1}monitor,cn=config
changetype: modify
replace: olcAccess
olcAccess: {0}to * by dn.base="gidNumber=0+uidNumber=0,cn=peercred,cn=external, cn=auth" read by dn.base="cn=ldapadm,dc=pcluster,dc=com" read by * none
```
5. ldapmodify  -Y EXTERNAL -H ldapi:/// -f ~/monitor.ldif


6. Starter Config and Starter SChemas

```
cp /usr/share/openldap-servers/DB_CONFIG.example /var/lib/ldap/DB_CONFIG
chown ldap:ldap /var/lib/ldap/*
ldapadd -Y EXTERNAL -H ldapi:/// -f /etc/openldap/schema/cosine.ldif
ldapadd -Y EXTERNAL -H ldapi:/// -f /etc/openldap/schema/nis.ldif
ldapadd -Y EXTERNAL -H ldapi:/// -f /etc/openldap/schema/inetorgperson.ldif

```

1. Base ou stuff

```
#-----------------base.ldif --------------------#
dn: dc=pcluster,dc=com
dc: pcluster
objectClass: top
objectClass: domain

dn: cn=ldapadm,dc=pcluster,dc=com
objectClass: organizationalRole
cn: ldapadm
description: LDAP Manager

dn: ou=People,dc=pcluster,dc=com
objectClass: organizationalUnit
ou: People

dn: ou=Group,dc=pcluster,dc=com
objectClass: organizationalUnit
ou: Group
```
- ldapadd -x -W -D "cn=ldapadm,dc=pcluster,dc=com" -f ~/base.ldif

```
[root@ip-10-12-64-214 cn=config]#  ldapadd -x -W -D "cn=ldapadm,dc=pcluster,dc=com" -f ~/base.ldif
Enter LDAP Password:
adding new entry "dc=pcluster,dc=com"

adding new entry "cn=ldapadm,dc=pcluster,dc=com"

adding new entry "ou=People,dc=pcluster,dc=com"

adding new entry "ou=Group,dc=pcluster,dc=com"

```

1. Test Search

- ldapsearch -D cn="ldapadm,dc=pcluster,dc=com" -W -b "dc=pcluster,dc=com" objectClass=*

```
[root@ip-10-12-64-214 cn=config]# ldapsearch -D cn="ldapadm,dc=pcluster,dc=com" -W -b "dc=pcluster,dc=com" objectClass=*
Enter LDAP Password:
# extended LDIF
#
# LDAPv3
# base <dc=pcluster,dc=com> with scope subtree
# filter: objectClass=*
# requesting: ALL
#

# pcluster.com
dn: dc=pcluster,dc=com
dc: pcluster
objectClass: top
objectClass: domain

# ldapadm, pcluster.com
dn: cn=ldapadm,dc=pcluster,dc=com
objectClass: organizationalRole
cn: ldapadm
description: LDAP Manager

# People, pcluster.com
dn: ou=People,dc=pcluster,dc=com
objectClass: organizationalUnit
ou: People

# Group, pcluster.com
dn: ou=Group,dc=pcluster,dc=com
objectClass: organizationalUnit
ou: Group

# search result
search: 2
result: 0 Success

# numResponses: 5
# numEntries: 4
[root@ip-10-12-64-214 cn=config]#
```

7. Verify Port is listening

```
[root@ip-10-12-64-214 cn=config]# netstat -anpl | grep 389
tcp        0      0 0.0.0.0:389             0.0.0.0:*               LISTEN      11736/slapd
tcp6       0      0 :::389                  :::*                    LISTEN      11736/slapd

```

#### Adding Users to LDAP

1. sample org chart test

```
# slapd_accounting_basic.ldif

dn: ou=Manager,dc=pcluster,dc=com
objectClass: organizationalUnit
objectClass: top
ou: Manager

dn: ou=Customers,dc=pcluster,dc=com
objectClass: organizationalUnit
objectClass: top
ou: Customers

dn: cn=customerAccountAdmin,ou=Manager,dc=pcluster,dc=com
cn: customerAccountAdmin
objectClass: organizationalRole
objectClass: simpleSecurityObject
objectClass: top
userPassword: {SSHA}8XZPCTE9V7hyjwNxq9GNNW72NqRROU5N

dn: ou=Users,ou=Customers,dc=pcluster,dc=com
objectClass: organizationalUnit
objectClass: top
ou: Users

dn: ou=Groups,ou=Customers,dc=pcluster,dc=com
objectClass: organizationalUnit
objectClass: top
ou: Groups

#--- end
```


#### Notional tony.ldif

```
dn: uid=tony,ou=People,dc=pcluster,dc=com
uid: tony
cn: tony
objectClass: account
objectClass: posixAccount
objectClass: top
objectClass: shadowAccount
userPassword: {SSHA}8XZPCTE9V7hyjwNxq9GNNW72NqRROU5N
shadowLastChange: 10000
shadowMax: 99999
shadowWarning: 7
loginShell: /bin/bash
uidNumber: 1001
gidNumber: 1000
homeDirectory: /home/tony
```

1. add this user and pray
    -  ldapadd -x -W -D "cn=ldapadm,dc=pcluster,dc=com" -f ~/tony.ldif

        - adding new entry "uid=Gecko,ou=users,dc=linuxaholics,dc=com"


- ldapsearch -D cn="ldapadm,dc=pcluster,dc=com" -W -b "uid=tony,ou=People,dc=pcluster,dc=com" objectClass=*

[ get_user_tony.py](https://github.com/tonybutzer/bslurm/blob/main/3_notebooks/get_user_tony.py)


#### Terraform the test host for LDAP
- manual
- IAM Role = butzer-devops-policy
- Other Important AWS Things
    - vpc id subnet 
		- csr-vpc-dev-internal-Subnet-A subnet-08f1118dd59133513	Available	vpc-0055752230db6161d 

    - security groups sg sg-00005b1b65e6ec0bb - SG-SSH-Server-Internal-lcmap-dev
- nevermind ws-costanalyzer exists with all of the ingredients

- 

#### Demo Terraform for Brandon
- et-cost
- iac repo
- tfinit
- docker terraform
- ship.tf
- variables.tf
- book?

### Install and Learn LDAP
- git clone https://github.com/tonybutzer/the_libs.git
- build libTest6
- start jupyter 
- create training notebooks

### Docker LDAP tests


## M$ Active Directory Service - Brandon
- document steps here
- plans, problems, progress

## ldappasswd EXAMPLE

The `ldappasswd` command is used to change a user's password in an LDAP (Lightweight Directory Access Protocol) directory. Below is an example of how to use the `ldappasswd` command:
---
```bash
# prompts for passwd instead of random

$ ldappasswd -H ldap://localhost -D "cn=ldapadm,dc=pcluster,dc=com" -w yaml -x "uid=tony,ou=People,dc=pcluster,dc=com" -S
New password:
Re-enter new password:

```
---
```bash
ldappasswd -H ldap://your_ldap_server -D "cn=admin,dc=example,dc=com" -w admin_password -x "uid=johndoe,ou=users,dc=example,dc=com"
```

Explanation of the command:

- `ldappasswd`: This is the command itself.

- `-H ldap://your_ldap_server`: Specifies the URI of the LDAP server. Replace `your_ldap_server` with the actual address of your LDAP server.

- `-D "cn=admin,dc=example,dc=com"`: This option specifies the LDAP bind DN (Distinguished Name) to use for authentication. In this example, it's using the admin account's DN. Make sure to replace it with your actual admin DN.

- `-w admin_password`: Specifies the password for the LDAP admin account specified in the `-D` option.

- `-x`: This option specifies that simple authentication should be used. It's commonly used for LDAP servers that don't require strong authentication mechanisms.

- `"uid=johndoe,ou=users,dc=example,dc=com"`: This is the DN of the user whose password you want to change. Replace `johndoe`, `ou=users`, `dc=example,dc=com` with the actual username, organizational unit, and LDAP base domain, respectively.

After executing this command, you will be prompted to enter the new password for the user. Once you provide and confirm the new password, the user's password will be updated in the LDAP directory.

Please ensure you have appropriate permissions and authentication details to perform this operation. Additionally, always exercise caution when working with administrative tasks like changing passwords.

## LDAP Jargon
LDAP (Lightweight Directory Access Protocol) is a protocol used to access and maintain directory information services over a network. It's commonly used for centralized user authentication and authorization, as well as for storing other types of information like addresses, phone numbers, and more.

LDAP Authentication:
LDAP authentication is a method of validating the identity of a user or system by querying an LDAP server. When a user tries to log in, their credentials (username and password) are sent to the LDAP server. The server checks these credentials against its database and grants access if they match.

Roles of PAM, sssd, and NSS:

1. **PAM (Pluggable Authentication Modules):**
   - PAM is a framework used on Unix and Linux systems for authentication and authorization. It provides a standardized way to manage the authentication process for various applications and services.
   - PAM allows system administrators to configure different authentication methods (e.g., local files, LDAP, Kerberos) without modifying the applications themselves.
   - When it comes to LDAP authentication, PAM is responsible for interfacing with the authentication module that communicates with the LDAP server.

2. **sssd (System Security Services Daemon):**
   - sssd is a system daemon used on Linux and Unix systems for centralized identity and authentication management. It's particularly useful in environments that rely on LDAP or other identity providers.
   - sssd can cache authentication information, which reduces the load on LDAP servers and improves performance.
   - It provides services like caching of credentials, offline authentication, and user and group enumeration.

3. **NSS (Name Service Switch):**
   - NSS is a component of the GNU C Library (glibc) used on Unix and Linux systems to configure how system databases (like user accounts, groups, and hostnames) are accessed.
   - It allows system administrators to specify the sources where system information is obtained (e.g., local files, LDAP, NIS).
   - In the context of LDAP, NSS is crucial because it determines where the system looks for information about users, groups, and other entities.

The typical flow in a system with LDAP authentication, PAM, sssd, and NSS might look like this:

1. **User attempts to log in:**
   - The login request goes through PAM.

2. **PAM configuration:**
   - PAM checks its configuration to determine which authentication modules to use.

3. **PAM communicates with sssd:**
   - If LDAP authentication is configured, PAM interfaces with the appropriate module (usually provided by sssd) to query the LDAP server.

4. **sssd communicates with the LDAP server:**
   - sssd communicates with the LDAP server, passing along the user's credentials.

5. **LDAP server authentication:**
   - The LDAP server checks the credentials against its database.

6. **Authentication response:**
   - The result of the authentication is sent back through sssd, PAM, and finally, the user is either granted access or denied based on the LDAP server's response.

These components work together to enable centralized authentication and authorization in a Unix or Linux environment using LDAP.
