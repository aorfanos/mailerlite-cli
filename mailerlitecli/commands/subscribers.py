import requests
import json
import yaml
from mailerlitecli.utils.configfiles import importYAML
from mailerlitecli.utils.utils import args_parse
from prettytable import PrettyTable

class Subscriber(object):

    def __init__(self, mailerlite_api_token):
        self.mailerlite_api_token = mailerlite_api_token
        self.response_table = PrettyTable()
        self.response_table.field_names = ['Key', 'Value']
        self.post_headers = {
                'Content-Type': 'application/json',
                'X-MailerLite-ApiKey': '{}'.format(mailerlite_api_token),
                }
        self.get_headers = {
                'X-MailerLite-ApiKey': '{}'.format(mailerlite_api_token),
                }
        
    def list(self):
        mailerlite_api_token = self.mailerlite_api_token
        response_table = self.response_table
        response_table.field_names = ['ID','E-mail','Type','Sent','Opened','Clicked','Subscribe Date', 'Created']
        _subscriber_list = requests.get('https://api.mailerlite.com/api/v2/subscribers', headers=self.get_headers).json()

        for _subscriber in _subscriber_list:
            _id = _subscriber['id']
            _email = _subscriber['email']
            _type = _subscriber['type']
            _sent = _subscriber['sent']
            _opened = _subscriber['opened']
            _clicked = _subscriber['clicked']
            _subscribe_data = _subscriber['date_subscribe']
            _created = _subscriber['date_created']

            table_row = ['{}'.format(_id),'{}'.format(_email),'{}'.format(_type),
                    '{}'.format(_sent),'{}'.format(_opened),'{}'.format(_clicked),
                    '{}'.format(_subscribe_data),'{}'.format(_created)]
            
            response_table.add_row(table_row)

        print(response_table)

    def add(self, email, name="", config_file=""):
        mailerlite_api_token = self.mailerlite_api_token
        response_table = self.response_table
        headers = self.post_headers

        if config_file == "":
            _data = {
                    'email': '{}'.format(email),
                    'name': '{}'.format(name),
                    }
            _subscriber_add = requests.post('https://api.mailerlite.com/api/v2/subscribers', headers=headers, json=_data)
        else:
            _config_file = importYAML(config_file)
            _subscriber_add = requests.post('https://api.mailerlite.com/api/v2/subscribers', headers=headers, json=_config_file)

        print("{}\n{}".format(_subscriber_add.status_code, _subscriber_add.content))

    def search(self, query=""):
        pass

    def update(self, identifier, *options): #identifier == subscriber ID or e-mail
        mailerlite_api_token = self.mailerlite_api_token
        headers = self.post_headers
        
        _data = args_parse(options)
        _update_subscriber_info = requests.put('https://mailerlite.com/api/v2/subscribers/'+str(identifier), headers=headers, json=_data)

        print(_update_subscriber_info.status_code)

    def show(self, identifier):
        mailerlite_api_token = self.mailerlite_api_token
        headers = self.get_headers
        response_table = self.response_table
        
        _subscriber_info = requests.get('https://mailerlite.com/api/v2/subscribers/'+str(identifier), headers=headers).json()

        _id = _subscriber_info['id']
        _email = _subscriber_info['email']

        response_table.add_row(['ID','{}'.format(_id)])
        response_table.add_row(['E-mail','{}'.format(_email)])

        for _key in _subscriber_info:
            if _key not in ["fields", "name", "email", "id"]:
                response_table.add_row(['{}'.format(_key), '{}'.format(_subscriber_info[_key])])

        for _field_count in range(len(_subscriber_info['fields'])):
           _key = _subscriber_info['fields'][_field_count]['key']
           _value = _subscriber_info['fields'][_field_count]['value']
           if _key not in ['email']:
               response_table.add_row(['{}'.format(_key),'{}'.format(_value)])

        print(response_table)
