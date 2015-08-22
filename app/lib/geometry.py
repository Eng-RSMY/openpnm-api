from .input import Input

class Geometry(Input):
  DEFAULTS = {
    'poreSeed': 'correlated',
    'lx': 1,
    'ly': 1,
    'lz': 1,
    'poreDiameter': 'weibull_min'
  }
