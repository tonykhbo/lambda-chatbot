import json, os
import requests
import pandas as pd

TOKEN = os.environ['WEBEX_CHATBOT_TOKEN']

def getMessage(event):
    print(event)
    url = "https://webexapis.com/v1/messages/" + event["data"]["id"]
    headers = {
        "Authorization": "Bearer "+ TOKEN,  # Bot's access token
        "Content-Type": "application/json"
    }
    
    response = requests.request("GET", url=url, headers=headers)
    return response.json()
    
def checkCSV(messageDetails):
    user_input = messageDetails["text"]
    SHEET_ID = '1LrhboEChYbmjTACMWDYlN0Q9fPKv9JodANNRo43OY8s'
    SHEET_NAME = 'data'
    url = f'https://docs.google.com/spreadsheets/d/{SHEET_ID}/gviz/tq?tqx=out:csv&sheet={SHEET_NAME}'
    df = pd.read_csv(url)
    #print(df.head())
    contactInfo = df[df["name"] == user_input]["ContactInfo"].iloc[0]
    return contactInfo

def postResponse(messageDetails, contactInfo):
    if (messageDetails["personEmail"] != "vumi@webex.bot"):
        url = "https://webexapis.com/v1/messages"
        headers = {
            "Authorization": "Bearer "+ TOKEN,
            "Content-Type": "application/json"
        }
        payload = {
            "roomId": messageDetails["roomId"],
            "text": contactInfo
        }
    
        response = requests.request("POST", url, data=json.dumps(payload), headers=headers)

def webhook(event, context):
    messageDetails = getMessage(json.loads(event["body"]))
    contactInfo = checkCSV(messageDetails)
    postResponse(messageDetails, contactInfo)

    return event
