import json


class MyJsonEncoder(json.JSONEncoder):
    def default(self, o):
        return o.__dict__


def dumps(obj):
    return json.dumps(obj, indent=4, cls=MyJsonEncoder)


def loads(jsondata):
    return json.loads(jsondata)

def symply_dumps(obj):
    jsondata = json.dumps(obj, cls=MyJsonEncoder)
    return json.loads(jsondata)
