import json
import requests


def lambda_handler(event, context):
    print(event)
    try:
        body=json.loads(event['body'])
        print(body)

        message_part=body['message'].get('text')
        print("Message part : {}".format(message_part))

        data = {'url':message_part}

        payload=requests.post('https://cleanuri.com/api/v1/shorten',data=data) 
        short_url = payload.json()['result_url']
        print("the short url is : {}".format(short_url))

        chat_id=body['message']['chat']['id']
        url = f'https://api.telegram.org/bot{token_no}/sendMessage'
        payload={
                  'chat_id': chat_id,
                  'text':short_url
                }
        r = requests.post(url,json=payload)
        return {
               "statusCode": 200
        }
    except:
        return {
               "statusCode": 200
        }
