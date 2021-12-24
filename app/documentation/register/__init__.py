from flask import request
from flask_restx import Namespace, Resource, fields


ns_register = Namespace('register', 'Register related endpoints')

register_user_model = ns_register.model('Register', {
   'full_name': fields.String(),
   'email': fields.String(),
   'password': fields.String(),
   'photo': fields.String()
})

@ns_register.route('')
class Register(Resource):
      def post(self):
          message = 'Wellcome, you are registered successfully! Save the token to login in to your account!'
          response = { 'status': 'success', 'message': message, 'token': token }
          return jsonify(response)

      @ns_register.marshal_list_with(register_user_model)
      @ns_register.response(500, 'Internal Server Error')
      def post(self):
          response = { 'status': 'error', 'message': 'Internal Server Error' }
          return response