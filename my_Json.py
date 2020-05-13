import json


class MyJsonEncoder(json.JSONEncoder):
    def default(self, o):
        return o.__dict__


def dumps(obj):
    jstring = json.dumps(obj, indent=4, cls=MyJsonEncoder)
    # jstring.replace("\\n", "\n")
    return jstring


def loads(jsondata: str):
    # jsondata.replace("\n","\\n")
    return json.loads(jsondata)

def symply_dumps(obj):
    jsondata = json.dumps(obj, cls=MyJsonEncoder)
    return json.loads(jsondata)

