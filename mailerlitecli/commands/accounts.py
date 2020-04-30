import requests
from prettytable import PrettyTable

class Account(object):

    def __init__(self, mailerlite_api_token):
        self.mailerlite_api_token = mailerlite_api_token

    def stats(self, timestamp=""):
        mailerlite_api_token = self.mailerlite_api_token
        response_table = PrettyTable()
        response_table.field_names = ['Key', 'Value']
        if timestamp == "":
            _account_stats = requests.get("https://api.mailerlite.com/api/v2/stats", headers={'X-MailerLite-ApiKey': '{}'.format(mailerlite_api_token)}).json()
        else:
            _account_stats = requests.get("https://api.mailerlite.com/api/v2/stats", 
                    headers={'X-MailerLite-ApiKey': '{}'.format(mailerlite_api_token)},
                        json={'timestamp': '{}'.format(timestamp)}).json()
        print(_account_stats)
