import json


class MyJsonEncoder(json.JSONEncoder):
    def default(self, o):
        return o.__dict__


def dumps(obj):
    return json.dumps(obj, indent=4, cls=MyJsonEncoder)


def loads(jsondata, hook):
    return json.loads(jsondata, object_hook=hook)


