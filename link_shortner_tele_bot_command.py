import json
import requests

token_no = ""

def sendMessage(id, msg):
  url = f'https://api.telegram.org/bot{token_no}/sendMessage'
  payload = {
    'chat_id': id,
    'text': msg
  }
  r  = requests.post(url, json=payload)
  
def isValidUrl(msg):
  if(msg[:4]=="http" or msg[:3]=="www"):
    return True
  return False
      
def lambda_handler(event, context):
  try:
    body = json.loads(event['body'])
    message_part = body['message'].get('text')
    chat_id = body['message']['chat']['id']

    if isValidUrl(message_part):
      short_url = requests.post(f'https://api.shrtco.de/v2/shorten?url={message_part}').json()['result']['full_short_link']
      sendMessage(chat_id, short_url)
      return {
        "statusCode": 200
      }
      
    else:
      sendMessage(chat_id,"Hello,"+"\n"+"Please Enter a Valid URL")
  except:
    return {
      "statusCode": 500
    }
