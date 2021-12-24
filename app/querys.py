####--------------------------------------------------------------------------
####--------------------------------------------------------------------------

from app import mysql


####--------------------------------------------------------------------------
####--------------------------------------------------------------------------
def get_user_id(email):
    try:
          cursor = mysql.connection.cursor()
          query_user = 'SELECT * FROM users WHERE email = "' + email + '"'
          cursor.execute(query_user)
          data_user = cursor.fetchall()
          cursor.close()

          for data in data_user:
              id_user = data['id_user']
          
          return id_user

    except:
          message = 'Error the email is not registered!'
          response = { 'status': 'error', 'message': message }
          return response


####--------------------------------------------------------------------------
####--------------------------------------------------------------------------
def token_exist(token):
    try:
          cursor = mysql.connection.cursor()
          query_user = 'SELECT * FROM users WHERE token = "' + token + '"'
          cursor.execute(query_user)
          data_user = cursor.fetchall()
          cursor.close()

          verify = True
          
          return verify

    except:
          verify = True
          return verify

####--------------------------------------------------------------------------
####--------------------------------------------------------------------------
def get_data_from_token(token):
    try:
          cursor = mysql.connection.cursor()
          query_user = 'SELECT * FROM users WHERE token = "' + token + '"'
          cursor.execute(query_user)
          data_user = cursor.fetchall()
          cursor.close()
          
          return data_user

    except:
          message = 'Error the data no exist!'
          return verify

####--------------------------------------------------------------------------
####--------------------------------------------------------------------------

####--------------------------------------------------------------------------
####--------------------------------------------------------------------------

####--------------------------------------------------------------------------
####--------------------------------------------------------------------------

####--------------------------------------------------------------------------
####--------------------------------------------------------------------------