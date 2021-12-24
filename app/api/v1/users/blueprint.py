####--------------------------------------------------------------------------
####--------------------------------------------------------------------------

import base64
import json, time, datetime, string, random

from flask import Flask, Blueprint, redirect, url_for, request, jsonify, make_response, session
from security_funcs import check_pass

from flask_restx import Namespace, Resource, fields

from app import app, mysql#, api


####--------------------------------------------------------------------------
####--------------------------------------------------------------------------

####--------------------------------------------------------------------------
####--------------------------------------------------------------------------

api_users = Blueprint('/v1/users', __name__)

####--------------------------------------------------------------------------
####--------------------------------------------------------------------------


####--------------------------------------------------------------------------
####--------------------------------------------------------------------------


####--------------------------------------------------------------------------------------------------------------
#### curl -X GET -H "Content-Type: application/json" -H "Accept: application/json" http://cors.org:7001/api/v1/clients/get_wellcome/
####--------------------------------------------------------------------------------------------------------------
#### curl -H "Content-Type: application/json" -X POST -d '{ "email": "nikola.tesla@gmail.com", "password": "1234asdf" }' http://0.0.0.0:7001/api/v1/users/login_user/
####--------------------------------------------------------------------------------------------------------------

# namespace = Namespace('login_user', 'Login Users related endpoints')

# login_user_model = namespace.model('LoginUser', {
#    'email': fields.String(
#       description = 'The user email'
#    ),
#    'password': fields.String(
#       description = 'The user password'
#    )
# })


####--------------------------------------------------------------------------
####--------------------------------------------------------------------------
@api_users.route('/login_user/', methods=["GET", "POST"])
def login_user():
# @api_users.route('/login_user/')
# class LoginUser(Resource):
#       def post(self):

         #user_auth = None
         #user_id = None

         #session['user_auth'] = user_auth
         #session['user_id'] = user_id

         email = str(request.json.get('email'))
         password = str(request.json.get('password'))

         if request.method == 'POST':

            try:
               cursor = mysql.connection.cursor()
               query_user = 'SELECT * FROM users WHERE email = "' + email + '"'
               cursor.execute(query_user)
               data_user = cursor.fetchall()
               cursor.close()

               print(data_user)

               for data in data_user:
                  full_name = data['full_name']
                  stored_passwd = data['passwd']
                  id_user = data['id_user']
               #print(' -- ', full_name)
               #print(' -- ', stored_passwd)

               verify_pass = check_pass(password, stored_passwd)
               #print(' -- ', verify_pass)

               if verify_pass == True:
                  #session['user_auth'] = True
                  #session['user_id'] = id_user

                  message = 'Wellcome ' + full_name + '!'
                  response = { 'status': 'success', 'message': message }
                  
                  #return jsonify(response)
                  return response
               else:
                  session['user_auth'] = None
                  session['user_email'] = None

                  message = 'Your email or password is incorrect!'
                  response = { 'status': 'success', 'message': message }
                  #return jsonify(response)
                  return response
               ##return 'asdf'
         
            except:
               message = 'Error in login method!'
               response = { 'status': 'error', 'message': message }
               #return jsonify(response)
               return response

         else:
            response = { 'status': 'error', 'message': 'Method Not Allowed!' }
            #return jsonify(response)
            return response


####--------------------------------------------------------------------------
####--------------------------------------------------------------------------

####--------------------------------------------------------------------------
####--------------------------------------------------------------------------

####--------------------------------------------------------------------------
####--------------------------------------------------------------------------

####--------------------------------------------------------------------------
####--------------------------------------------------------------------------



