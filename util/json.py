import json
from json import JSONEncoder


class Encoder(JSONEncoder):
  def default(self, o):
    return o.__dict__

  def __json__(self, o):
    return json.dumps(o, indent=2, cls=Encoder)