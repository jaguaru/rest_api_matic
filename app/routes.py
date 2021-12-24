####--------------------------------------------------------------------------
####--------------------------------------------------------------------------

import datetime, os, time
import hashlib, uuid

from flask import Flask, jsonify, redirect, url_for, request
from security_funcs import id_generator_8, gen_pass_hash, check_pass

from app import app, mysql, api

from flask_restx import Namespace, Resource, fields

####--------------------------------------------------------------------------
####--------------------------------------------------------------------------

datetime_now_str = str(datetime.datetime.now())

####--------------------------------------------------------------------------
####--------------------------------------------------------------------------

####--------------------------------------------------------------------------------------------------------------
####--------------------------------------------------------------------------------------------------------------
#### curl -X GET -H "Content-Type: application/json" -H "Accept: application/json" http://0.0.0.0:7001/home/
####--------------------------------------------------------------------------------------------------------------
#@app.route('/', methods=["GET", "POST"])
@app.route('/home/', methods=["GET", "POST"])
def home():
    datetime_now_str = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    message = 'Wellcome Home!'
    response = { 'status': 'success', 'message': message }
    return jsonify(response)


####--------------------------------------------------------------------------------------------------------------
####--------------------------------------------------------------------------------------------------------------
#### curl -H "Content-Type: application/json" -X POST -d '{ "full_name": "Nikola Tesla", "email": "nikola.tesla@gmail.com", "password": "1234asdf", "photo": "mypic.png" }' http://0.0.0.0:7001/register/
####--------------------------------------------------------------------------------------------------------------
@app.route('/register/', methods=["GET", "POST"])
def register():

    full_name = str(request.json.get('full_name'))
    email = str(request.json.get('email'))
    passwd = str(request.json.get('password'))
    photo = str(request.json.get('photo'))
    date_created = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    if request.method == 'POST':

       token = id_generator_8()
       passwd = gen_pass_hash(passwd)

       try:
          cursor = mysql.connection.cursor()
          query_insert = 'INSERT INTO users (token, full_name, email, passwd, photo, date_created) VALUES (%s, %s, %s, %s, %s, %s)'
          values = (token, full_name, email, passwd, photo, date_created)
          print(' ---- query_insert ', query_insert)
          print(' ---- values ', values)
          cursor.execute(query_insert, values)
          mysql.connection.commit()
          cursor.close()

          message = 'Wellcome, you are registered successfully! Save the token to login in to your account!'

          response = { 'status': 'success', 'message': message, 'token': token }
          return jsonify(response)
    
       except:
          message = 'Error in register method!'
          response = { 'status': 'error', 'message': message }
          return jsonify(response)

    else:
       response = { 'status': 'error', 'message': 'Method Not Allowed!' }
       return jsonify(response)


####--------------------------------------------------------------------------
####--------------------------------------------------------------------------


####--------------------------------------------------------------------------
####--------------------------------------------------------------------------


####--------------------------------------------------------------------------
####--------------------------------------------------------------------------


####--------------------------------------------------------------------------
####--------------------------------------------------------------------------


####--------------------------------------------------------------------------
####--------------------------------------------------------------------------


####--------------------------------------------------------------------------
####--------------------------------------------------------------------------
