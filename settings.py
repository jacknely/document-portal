import os

SECRET_KEY = 'tste'
DEBUG=True
DB_USERNAME='root'
DB_PASSWORD='rootpass'
DATABASE_NAME='document_db_1'
DB_HOST='mysql'
DB_URI="mysql+pymysql://%s:%s@%s/%s" % (DB_USERNAME, DB_PASSWORD, DB_HOST, DATABASE_NAME)
SQLALCHEMY_DATABASE_URI = DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS = True

S3_KEY = os.environ.get("S3_KEY")
S3_SECRET = os.environ.get("S3_SECRET")
