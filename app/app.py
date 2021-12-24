####--------------------------------------------------------------------------
####--------------------------------------------------------------------------

from flask import Flask

from flask_mysqldb import MySQL

from flask_restx import Api

from itsdangerous import URLSafeTimedSerializer
from config import Configuration


####--------------------------------------------------------------------------
####--------------------------------------------------------------------------

PROD_HOST = '14.20.18.2'
PROD_PORT = '3306'
PROD_USER = 'qwer'
PROD_PASS = 'asdf@'
PROD_DB_NAME = 'api_matic'
####-----------------------------------------

TEST_HOST = '12.12.12.01'
TEST_PORT = '2794'
TEST_USER = 'asdf'
TEST_PASS = 'am40'
TEST_DB_NAME = 'a2ce2'


####--------------------------------------------------------------------------
####--------------------------------------------------------------------------


app = Flask(__name__)
api = Api(app, version='1.0', title='API 1.0', description='This is the REST API for Matic',)

app.config.from_object(Configuration)


####--------------------------------------------------------------------------
####--------------------------------------------------------------------------

app.config['RESTPLUS_MASK_SWAGGER'] = False

app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

app.config['MYSQL_HOST'] = PROD_HOST
app.config['MYSQL_PORT'] = int(PROD_PORT)
app.config['MYSQL_DB'] = PROD_DB_NAME
app.config['MYSQL_USER'] = PROD_USER
app.config['MYSQL_PASSWORD'] = PROD_PASS
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

####--------------------------------------------------------------------------
####--------------------------------------------------------------------------

mysql = MySQL(app)

if mysql:
    print('--------------------------------------------')
    print('  ----  Connected to Matic DB!')
    print('--------------------------------------------')
else:
    print('--------------------------------------------')
    print('  ----  Conection Error!')
    print('--------------------------------------------')


####--------------------------------------------------------------------------
####--------------------------------------------------------------------------

expiration = 300 #1800 #900s=15min // 600s=10min // 300s=5min
ts = URLSafeTimedSerializer(app.config["SECRET_KEY"], expiration)


####--------------------------------------------------------------------------
####--------------------------------------------------------------------------
