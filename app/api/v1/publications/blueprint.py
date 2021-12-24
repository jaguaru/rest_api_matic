####--------------------------------------------------------------------------
####--------------------------------------------------------------------------

import base64
import json, time, datetime, string, random

from flask import Flask, Blueprint, redirect, url_for, request, jsonify, make_response, session

from security_funcs import id_generator_8
from querys import token_exist, get_data_from_token

from app import app, mysql


####--------------------------------------------------------------------------
####--------------------------------------------------------------------------

####--------------------------------------------------------------------------
####--------------------------------------------------------------------------

api_publications = Blueprint('/v1/publications', __name__)

####--------------------------------------------------------------------------
####--------------------------------------------------------------------------


####--------------------------------------------------------------------------------------------------------------
####--------------------------------------------------------------------------------------------------------------
#### curl -H "Content-Type: application/json" -X POST -d '{ "token": "EDN2YUW8", "title": "My First Publication", "description": "This is my first publication in the API.", "priority": "1", "status": "1" }' http://0.0.0.0:7001/api/v1/publications/create_publication/
####--------------------------------------------------------------------------------------------------------------
@api_publications.route('/create_publication/', methods=["POST"])
def create_publication():

    token = str(request.json.get('token'))

    verify_token = token_exist(token)

    title = str(request.json.get('title'))
    description = str(request.json.get('description'))
    priority = str(request.json.get('priority'))
    status = str(request.json.get('status'))
    date_created = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    if request.method == 'POST':

       if verify_token == True:

            id_publication = str(id_generator_8())
            #fk_user = id_user
            user_data = get_data_from_token(token)
            for data in user_data:
               fk_user = str(data['id_user'])
               #print(fk_user)

            try:
               cursor = mysql.connection.cursor()
               query_insert = 'INSERT INTO publications (id_publication, title, description, priority, status, fk_user, date_created) VALUES (%s, %s, %s, %s, %s, %s, %s)'
               values = (id_publication, title, description, priority, status, fk_user, date_created)
               #print(' ---- query_insert ', query_insert)
               #print(' ---- values ', values)
               cursor.execute(query_insert, values)
               mysql.connection.commit()
               cursor.close()

               message = 'Publication created successfully!'

               response = { 'status': 'success', 'message': message, 'id_publication': id_publication }
               return jsonify(response)
               
            except:
               message = 'Error in create publication method!'
               response = { 'status': 'error', 'message': message }
               return jsonify(response)
       else:
          response = { 'status': 'error', 'message': 'Your email or password is incorrect!' }
          return jsonify(response)

    else:
       response = { 'status': 'error', 'message': 'Method Not Allowed!' }
       return jsonify(response)


####--------------------------------------------------------------------------------------------------------------
####--------------------------------------------------------------------------------------------------------------
#### curl -H "Content-Type: application/json" -X POST -d '{ "token": "EDN2YUW8", "id_publication": "Z9EQVFI1" }' http://0.0.0.0:7001/api/v1/publications/read_publication/
####--------------------------------------------------------------------------------------------------------------
@api_publications.route('/read_publication/', methods=["POST"])
def read_publication():

    token = str(request.json.get('token'))
    id_publication = str(request.json.get('id_publication'))

    verify_token = token_exist(token)

    if request.method == 'POST':

       if verify_token == True:
            #### there is a bug in this section after cursor.close()
            try:
               cursor = mysql.connection.cursor()
               query_publications = 'SELECT * FROM publications WHERE id_publication = "' + id_publication + '"'
               cursor.execute(query_publications)
               data_pubs = cursor.fetchall()
               cursor.close()

               print(' -- token ', token)
               print(' -- id_publication ', id_publication)
               print(' -- data_pubs ', data_pubs)

               #  apnd_pubs = []
               #  for pubs in data_pubs:
               #      json_pubs = {
               #         'token': pubs['token'], 
               #         'title': pubs['title'], 
               #         'description': pubs['description'], 
               #         'priority': pubs['priority'], 
               #         'status': pubs['status']
               #      }
               #  apnd_pubs.append(json_pubs)

               #  print(' -- apnd_pubs ', apnd_pubs)

               message = 'Publication created successfully!'

               response = { 'status': 'success', 'message': message, 'publication': apnd_pubs }
               print(' -- response ', response)
               #  return jsonify(response)
               return 'ASDF'
                     
            except:
               message = 'Error in read publication method!'
               response = { 'status': 'error', 'message': message }
               return jsonify(response)

       else:
          response = { 'status': 'error', 'message': 'Your email or password is incorrect!' }
          return jsonify(response)

    else:
       response = { 'status': 'error', 'message': 'Method Not Allowed!' }
       return jsonify(response)


####--------------------------------------------------------------------------------------------------------------
####--------------------------------------------------------------------------------------------------------------
#### curl -X GET -H "Content-Type: application/json" -H "Accept: application/json" http://0.0.0.0:7001/api/v1/clients/get_wellcome/
####--------------------------------------------------------------------------------------------------------------
# @api_publications.route('/delete_publication/', methods=["POST"])
# def delete_publication():

#     if request.method == 'POST':

#        response = { 'status': 'success', 'message': 'Bienvenido!' }
#        return jsonify(response)
#     else:
#        response = { 'status': 'error', 'message': 'Method Not Allowed!' }
#        return jsonify(response)


####--------------------------------------------------------------------------------------------------------------
####--------------------------------------------------------------------------------------------------------------
#### curl -H "Content-Type: application/json" -X POST -d '{ "token": "EDN2YUW8", "id_publication": "Z9EQVFI1", "title": "My First Publication (Edited)", "description": "This is my first publication in the API. (Edited)", "priority": "1", "status": "1" }' http://0.0.0.0:7001/api/v1/publications/update_publication/
####--------------------------------------------------------------------------------------------------------------
@api_publications.route('/update_publication/', methods=["POST"])
def update_publication():

    token = str(request.json.get('token'))
    id_publication = str(request.json.get('id_publication'))

    title = str(request.json.get('title'))
    description = str(request.json.get('description'))
    priority = str(request.json.get('priority'))
    status = str(request.json.get('status'))
    date_updated = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    verify_token = token_exist(token)

    if request.method == 'POST':

       if verify_token == True:

            try:
               cursor = mysql.connection.cursor()
               update_pubs = 'UPDATE publications SET title = "' + title + '", description = "' + description + '", priority = "' + priority + '", status = "' + status + '", date_updated = "' + date_updated + '" WHERE id_publication = "' + id_publication + '"'
               cursor.execute(update_pubs)
               mysql.connection.commit()
               cursor.close()

               message = 'Publication updated successfully!'

               response = { 'status': 'success', 'message': message }
               return jsonify(response)
                     
            except:
               message = 'Error in update publication method!'
               response = { 'status': 'error', 'message': message }
               return jsonify(response)

       else:
          response = { 'status': 'error', 'message': 'Your email or password is incorrect!' }
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



