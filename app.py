from siteopsdashboard.extension.login_manager import login_manager
from siteopsdashboard.extension.ldap_manager import ldap_manager
from siteopsdashboard.models.users.users import create_database
from siteopsdashboard.models.users.users import DB_NAME
from siteopsdashboard.models.users.users import db
from flask import Flask

def create_app(config_object):
    app = Flask(__name__.split('.')[0])
    app.config.from_object(config_object)
    app.config['SECRET_KEY'] = 'SuprSecretKeyThatOnlyIknowrightNow001'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///templates/' + DB_NAME
    app.config['LDAP_BASE_DN'] = 'dc=savagebeast,dc=com'
    app.config['LDAP_USER_DN'] = 'ou=people'
    app.config['LDAP_GROUP_DN'] = 'cn=consoleadmins,ou=groups'
    app.config['LDAP_BIND_USER_DN'] = 'uid=svc-spm,ou=people,dc=savagebeast,dc=com'
    app.config['LDAP_BIND_USER_PASSWORD'] = 's8jsj2ffs12zc'
    
    def register_extensions(app):
        db.init_app(app)   
        create_database(app)
        register_blueprints(app)
        login_manager.init_app(app) 
        ldap_manager.init_app(app) 
        
    def register_blueprints(app):
        from siteopsdashboard.auth.views import auth
        from siteopsdashboard.ptools.views import ptools
        app.register_blueprint(auth, url_prefix='/')
        app.register_blueprint(ptools, url_prefix='/')


    register_extensions(app)
    return app


