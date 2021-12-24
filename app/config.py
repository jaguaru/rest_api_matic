import os


class Configuration(object):
      APPLICATION_DIR = os.path.dirname(os.path.realpath(__file__))
      #DEBUG = True
      DEBUG = False
      SECRET_KEY = '3QY67riqdZQM3mUB3AqX6'
      STATIC_DIR = os.path.join(APPLICATION_DIR, 'static')
      ALLOWED_IMGS = set(['jpg', 'jpeg', 'png'])
