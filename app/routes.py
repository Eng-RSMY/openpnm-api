import json
from OpenPNM import __version__ as openpnm_version
from flask import g, render_template, request, Response, Blueprint
from app.lib import Topology, Geometry, Phase, Physics
from app.simulations import OrdinaryPercolation

# Simulation Enpoints

simulation_bp = Blueprint('simulations', __name__)

@simulation_bp.before_request
def modify_payload():
  g.query = {
    'topology': Topology(request.args.get('topology')),
    'geometry': Geometry(request.args.get('geometry')),
    'phase': Phase(request.args.get('phase')),
    'physics': Physics(request.args.get('physics'))
  }

@simulation_bp.route('/ordinary_percolation', methods=['GET'])
def op_simulation():
  simulation = OrdinaryPercolation(g.query)
  response = {
    'result': simulation.run()
  }
  return Response(json.dumps(response), mimetype='application/json')
