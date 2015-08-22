import json
from flask import Flask, Response
from app.routes import simulation_bp

api = Flask(__name__)
api.debug = True

__version__ = '0.1.0'

api.register_blueprint(simulation_bp, url_prefix='/simulations')

# Version Endpoint

@api.route('/version', methods=['GET'])
def version():
  response = {
    'api': __version__,
    'openpnm': openpnm_version,
  }
  return Response(json.dumps(response), mimetype='application/json')
