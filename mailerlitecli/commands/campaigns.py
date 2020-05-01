import mailerlitecli.commands.groups as groups 
import requests
import re
import yaml
import json

class Campaign(object):

    def __init__(self, mailerlite_api_token):
        self.mailerlite_api_token = mailerlite_api_token

    def status(self):
        mailerlite_api_token = self.mailerlite_api_token
        _campaigns_status_all = requests.get('https://api.mailerlite.com/api/v2/campaigns', headers={'X-MailerLite-ApiKey': '{}'.format(mailerlite_api_token)}).json()
        print(_campaigns_status_all)

    def create(self, campaign_type, config_file=""):
        mailerlite_api_token = self.mailerlite_api_token
        headers = {
                "Content-Type": "application/json",
                "X-MailerLite-ApiKey": "{}".format(mailerlite_api_token),
                }

        _config_file = open(config_file, "r")
        _config = yaml.full_load(_config_file)

        _type = campaign_type
        
        if _type == "ab":
            _send_type = _config['send_type']
            _ab_win_type = _config['ab_win_type']
            _split_part = _config['split_part']
            _values = _config['values']
            _groups = _config['groups']
            _winner_after = _config['winner_after']
            _winner_after_type = _config['winner_after_type']

            _data = {
                    'data': {
                       'type': 'ab',
                       'groups': '{}'.format(_groups),
                       'ab_settings': {
                           'send_type': '{}'.format(_send_type),
                           'values': '{}'.format(_values),
                           'ab_win_type': '{}'.format(_ab_win_type),
                           'winner_after': '{}'.format(_winner_after),
                           'winner_after_type': '{}'.format(_winner_after_type),
                           'split_part': '{}'.format(_split_part),
                   },
                   }
               }
        elif _type == "regular":
            _groups = _config['groups']
            _subject = _config['subject']

            _data = {
                    'subject': '{}'.format(_subject),
                    'groups': '{}'.format(_groups),
                    'type': 'regular',
                    }
        else:
            raise ValueError("Unaccepted campaign type")

        
        _campaign_create = requests.post('https://api.mailerlite.com/api/v2/campaigns', headers=headers, json=json.dumps(_data))

        print("{0}\n{1}".format(_campaign_create.status_code, _campaign_create.content))
