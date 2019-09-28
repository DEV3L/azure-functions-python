import logging
import requests

import azure.functions as func

url = "{url}"

payload = """[{
   "id": "1",
    "eventType": "pub-sub",
    "subject": "pubsub/event",
    "eventTime": "2019-09-28T12:00:00+00:00",
    "data": {
      "name": "|NAME|"
    },
    "dataVersion": "1.0",
    "metadataVersion": "1",
    "topic": "/subscriptions/{subscription}/resourceGroups/{resourcegroup}/providers/Microsoft.EventGrid/topics/pub-sub-grid\"
}]"""

headers = { 'aeg-sas-key': "{access_key}" }

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    if name:
        requests.request("POST", url, data=payload.replace("|NAME|", name), headers=headers)
        return func.HttpResponse(f"Hello {name}!")
    else:
        return func.HttpResponse(
             "Please pass a name on the query string or in the request body",
             status_code=400
        )
