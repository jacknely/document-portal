class Config(object):
    SECRET_KEY = b"sdjklfg"
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProdConfig(Config):
    DEVELOPMENT = False
    DEBUG = False
    DB_USERNAME = "root"
    DB_PASSWORD = "rootpass"
    DATABASE_NAME = "document_db_1"
    DB_HOST = "mysql"
    DB_URI = "mysql+pymysql://%s:%s@%s/%s" % (
        DB_USERNAME,
        DB_PASSWORD,
        DB_HOST,
        DATABASE_NAME,
    )
    SQLALCHEMY_DATABASE_URI = DB_URI


class DevConfig(Config):
    DB_URI = "sqlite:///parts.db"
    SQLALCHEMY_DATABASE_URI = DB_URI
    SQLALCHEMY_TRACK_MODIFICATIONS = True


class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = "sqlite://"
    DEBUG = True

    ASSETS_DEBUG = True
