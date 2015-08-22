from OpenPNM.Base import Controller

class Simulation:
  def __init__(self, params):
    self.controller = Controller()
    self.topo = params['topology']
    self.geo = params['geometry']
    self.phs = params['phase']
    self.phys = params['physics']

  def run(self):
    self.controller.clear()
