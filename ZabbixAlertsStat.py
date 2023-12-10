import requests
import json
import pandas
from datetime import datetime

start = '50812700'
stop = '70575522'
auth_code = '318e84664c4c3324f23d8d9de429a7c8'
temp_set = set()

test1 = {
    "jsonrpc": "2.0",
    "method": "event.get",
    "params": {
        "output": [
            "name",
            "eventid",
            "objectid",
            "clock"
        ],
        "acknowledged": False,
        "severities": "4",
        "eventid_from": start,
        "eventid_till": stop,
        "sortfield": ["clock", "eventid"],
        "sortorder": "DESC"
    },
    "auth": auth_code,
    "id": 1
}

test = {
    "jsonrpc": "2.0",
    "method": "event.get",
    "params": {
        "output": [
            "name",
            "eventid",
            "objectid",
            "clock"
        ],
        "select_acknowledges": [
            "userid",
            "message"
        ],
        "acknowledged": True,
        "severities": "4",
        "eventid_from": start,
        "eventid_till": stop,
        "sortfield": ["clock", "eventid"],
        "sortorder": "DESC"
    },
    "auth": auth_code,
    "id": 1
}

name_set = {
    '32': 'alimpiev.kv',
    '35': 'fasykhov.sg',
    '136': 'zagryaditskiy.ai',
    '97': 'khellstrem.dn',
    '92': 'migulin.dg',
    '87': 'Movchan.MV',
    '107': 'pentelejchuk.er',
    '33': 'zhuravlev.ra'
}

Current_Session = requests.session()


response_ack = Current_Session.post(url='https://zabbix-new.esphere.local/api_jsonrpc.php',
                                    json=test,
                                    verify=False)
result = json.loads(response_ack.text)
pd = pandas.DataFrame(data=result['result'])


for index, value in enumerate(pd.values):

    temp_values = pd.loc[index, 'acknowledges']
    for iterate in temp_values:
        temp_ack_values = iterate["message"]
        print(temp_ack_values)

    if 'ГДИ' in temp_ack_values:
        temp_set.add(pd.loc[index, 'objectid'])
        pd.loc[index, 'acknowledges'] = 'ГДИ'
    else:
        pd.loc[index, 'acknowledges'] = temp_ack_values

pd.to_excel('output_ack.xlsx')




response_non_ack = Current_Session.post(url='https://zabbix-new.esphere.local/api_jsonrpc.php',
                                        json=test1,
                                        verify=False)
result_non_ack = json.loads(response_non_ack.text)
pd_non_ack = pandas.DataFrame(data=result_non_ack['result'])




for index, value in enumerate(pd_non_ack.values):
    if pd_non_ack.loc[index, 'objectid'] in temp_set:
        pd_non_ack.loc[index, 'acknowledges'] = 'ГДИ'
    else:
        pd_non_ack.loc[index, 'acknowledges'] = 'None'

pd_non_ack.to_excel('output_non_ack.xlsx')



