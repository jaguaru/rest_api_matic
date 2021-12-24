from flask import Blueprint
##from flask_restx import Api

from app import api

from documentation.hello_world import namespace as hello_world_ns
from documentation.user import ns_user as user_ns
from documentation.publications import ns_publications as publications_ns


blueprint_swgr = Blueprint('/documentation', __name__)


##api.add_namespace(hello_world_ns)
api.add_namespace(user_ns)
api.add_namespace(publications_ns)