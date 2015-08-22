class Input:
  def __init__(self, params):
    if params is None:
      params = {}
    else:
      params = json.dumps(params)
    self._apply_defaults()

  def _apply_defaults(self):
    for name, value in self.DEFAULTS.items():
      if not hasattr(self, name):
        setattr(self, name, value)
