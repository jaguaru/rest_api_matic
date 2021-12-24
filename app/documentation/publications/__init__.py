from flask import request
from flask_restx import Namespace, Resource, fields


ns_publications = Namespace('publications', 'Publications related endpoints')


create_publication_model = ns_publications.model('CreatePublication', {
   'token': fields.String(required=True),
   'title': fields.String(required=True),
   'description': fields.String(required=True),
   'priority': fields.String(required=True),
   'status': fields.String(required=True)
})

read_publication_model = ns_publications.model('ReadPublication', {
   'token': fields.String(required=True),
   'id_publication': fields.String(required=True)
})

delete_publication_model = ns_publications.model('DeletePublication', {
   'token': fields.String(required=True),
   'id_publication': fields.String(required=True)
})

publications_apnd = []

@ns_publications.route('/create_publication/<string:title>')
class CreatePublication(Resource):
      def get(self):
          #id_publication = '1234'
          #message = 'Publication created successfully!'
          #response = { 'status': 'success', 'message': message, 'id_publication': id_publication }
          return publications_apnd
      
      @ns_publications.expect(create_publication_model)
      def post(self):
          publications_apnd.append(api.payload)
          id_publication = '1234'
          message = 'Publication created successfully!'
          response = { 'status': 'success', 'message': message, 'id_publication': id_publication }
          #response = { 'token': 'EDN2YUW8', 'title': 'My First Publication', 'description': 'This is my first publication in the API.', 'priority': '1', 'status': '1' }
          return response

      @ns_publications.marshal_list_with(create_publication_model)
      @ns_publications.response(500, 'Internal Server Error')
      def post(self):
          response = { 'status': 'error', 'message': 'Internal Server Error' }
          return response

@ns_publications.route('/read_publication')
class ReadPublication(Resource):
      def get(self):
          message = 'Publication content successfully!'
          response = { 'status': 'success', 'message': message }
          return response

      @ns_publications.marshal_list_with(read_publication_model)
      @ns_publications.response(500, 'Internal Server Error')
      def get(self):
          response = { 'status': 'error', 'message': 'Internal Server Error' }
          return response

@ns_publications.route('/delete_publication')
class DeletePublication(Resource):
      def delete(self):
          message = 'Publication deleted successfully!'
          response = { 'status': 'success', 'message': message }
          return response

      @ns_publications.marshal_list_with(delete_publication_model)
      @ns_publications.response(500, 'Internal Server Error')
      def delete(self):
          response = { 'status': 'error', 'message': 'Internal Server Error' }
          return response

