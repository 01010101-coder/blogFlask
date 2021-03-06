class Configuration(object):
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    #... ://user:password@server/database
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:root@localhost/test1'

    # Three slashes for a relative database path.
    # Four slashes for a absolute database path.
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///sqlite_database.db'

    SECRET_KEY = 'something very secret'

    ### Flask-security
    SECURITY_PASSWORD_SALT = 'salt'
    SECURITY_PASSWORD_HASH = 'sha512_crypt'
