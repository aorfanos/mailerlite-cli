import requests

def checkAPIStatus(mailerlite_api_token):
    _api_response = requests.get('https://api.mailerlite.com/api/v2', headers={'X-MailerLite-ApiKey': '{}'.format(mailerlite_api_token)})
    print("API status: {}".format(_api_response.status_code))
