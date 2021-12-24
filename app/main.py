import routes
from app import app
from documentation import blueprint_swgr

#### localhost server
#HOST = '127.0.1.2'
#### externally visible server
HOST = '0.0.0.0'
PORT = 7001


from documentation import blueprint_swgr
app.register_blueprint(blueprint_swgr, url_prefix='/documentation')


from api.v1.publications.blueprint import api_publications
from api.v1.users.blueprint import api_users

app.register_blueprint(api_publications, url_prefix='/api/v1/publications')
app.register_blueprint(api_users, url_prefix='/api/v1/users')




if __name__ == '__main__':
   app.run(host=HOST, port=PORT)

