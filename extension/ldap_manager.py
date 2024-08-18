from flask_ldap3_login import LDAP3LoginManager
from config import  LDAP_USE_SSL, LDAP_HOST, LDAP_PORT
ldap_manager = LDAP3LoginManager()
from ldap3 import Tls 
import ssl

tls_ctx = Tls(
    version=ssl.PROTOCOL_TLSv1_2,
    ca_certs_file='siteopsdashboard/keys',
)

ldap_manager.add_server(
LDAP_HOST, LDAP_PORT, LDAP_USE_SSL, tls_ctx=tls_ctx 
)
