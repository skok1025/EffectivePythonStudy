import json


def load_json_key(data, key):
    try:
        result_dict = json.loads(data) # <1>
    except ValueError as e:
        print("except")
        raise KeyError from e
    else:
        print("else")
        return result_dict[key] # <2>

#assert load_json_key('{"foo": "bar"}', 'foo') == 'bar'

load_json_key('{"foo": "bar"', 'foo')