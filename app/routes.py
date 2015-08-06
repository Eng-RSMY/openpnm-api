import json
from OpenPNM import __version__ as openpnm_version
from flask import render_template, request, Response
from app import api, __version__
from app.simulations import ordinary_percolation

# Version Endpoint

@api.route('/version', methods=['GET'])
def version():
  response = {
    'api': __version__,
    'openpnm': openpnm_version,
  }
  return Response(json.dumps(response), mimetype='application/json')

# Simulation Endpoints

@api.route('/simulations/ordinary_percolation', methods=['GET'])
def op_simulation():
  query = json.loads(request.args.get('query'))
  response = {
    'result': ordinary_percolation.run(query)
  }
  return Response(json.dumps(response), mimetype='application/json')
