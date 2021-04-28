import json

def canshu_a(id):
    model_id = '{"rid":"R_SO_4_1492901593","threadId":"R_SO_4_1492901593","pageNo":"1","pageSize":"50","cursor":"-1","offset":"0",' \
          '"orderType":"1","csrf_token":""}'
    b = json.loads(model_id)
    b['rid'] = 'R_SO_4_{}'.format(id)
    b['threadId'] = 'R_SO_4_{}'.format(id)
    return json.dumps(b)
