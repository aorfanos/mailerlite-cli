import requests

class Subscriber(object):

    def __init__(self, mailerlite_api_token):
        self.mailerlite_api_token = mailerlite_api_token

    def list(self):
        mailerlite_api_token = self.mailerlite_api_token

        _subscriber_list = requests.get('https://api.mailerlite.com/api/v2/subscribers', headers={'X-MailerLite-ApiKey': '{}'.format(mailerlite_api_token)}).json()

        print(_subscriber_list)
