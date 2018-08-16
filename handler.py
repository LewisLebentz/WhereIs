import json
import requests
import sys
import time
from urllib.parse import unquote

def whereis(event, context):
    requests.packages.urllib3.disable_warnings()

    print(event)
    print(context)

    slackstring = event['body']

    slackstringdict = dict(item.split("=") for item in slackstring.split("&"))

    url = 'https://***REMOVED***/webacs/api/v3/data/Clients.json?userName="%s***REMOVED***"' % slackstringdict['text']

    resp = requests.get(url=url, verify=False, auth=('***REMOVED***','***REMOVED***'))
    data = resp.json()

    # print(data)
    # print("BREAK")
    # print(data['queryResponse'])
    # print("BREAK")
    # print(data['queryResponse']['entityId'])
    # print("BREAK")
    # print(data['queryResponse']['entityId'][0])
    # print("BREAK")
    # print(data['queryResponse']['entityId'][0]['@url'])

    url = str(data['queryResponse']['entityId'][0]['@url']) + '.json'
    resp = requests.get(url=url, verify=False, auth=('***REMOVED***','***REMOVED***'))
    data = resp.json()

    # print(data['queryResponse'])
    # print("BREAK")
    print(data['queryResponse']['entity'])
    print(data['queryResponse']['entity'][0]['clientsDTO']['updateTime'])

    updateTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(int(data['queryResponse']['entity'][0]['clientsDTO']['updateTime'])/1000))

    print(data['queryResponse']['entity'][0]['clientsDTO']['location'])

    print(updateTime)

    initialresponse = {
        "statusCode": 200,
        "body": data['queryResponse']['entity'][0]['clientsDTO']['location'] + " last seen at " + updateTime,
    }

    # print(slackstringdict['response_url'])
    # print(unquote(slackstringdict['response_url']))
    #
    # slack_data = {
    # 'text': data['queryResponse']['entity'][0]['clientsDTO']['location'] + " last seen at " + updateTime,
    # 'response_type': "in_channel",
    # }
    #
    # headers = {'Content-Type': 'application/json'}
    #
    #
    # sdata = json.dumps(slack_data)
    # r = requests.post(unquote(slackstringdict['response_url']), sdata, headers=headers)
    #
    # print(r.status_code)

    return(initialresponse)
