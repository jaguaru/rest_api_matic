from flask import request
from flask_restx import Namespace, Resource, fields


ns_user = Namespace('login_user', 'Login Users related endpoints')

login_user_model = ns_user.model('LoginUser', {
   'email': fields.String(),
   'password': fields.String()
})

@ns_user.route('')
class LoginUser(Resource):
      def post(self, full_name):
          full_name = 'Nikola Tesla'
          message = 'Wellcome ' + full_name + '!'
          response = { 'status': 'success', 'message': message }
          return response

      @ns_user.marshal_list_with(login_user_model)
      @ns_user.response(500, 'Internal Server Error')
      def post(self):
          response = { 'status': 'error', 'message': 'Internal Server Error' }
          return response