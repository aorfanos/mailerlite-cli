import mailerlitecli.commands.groups as groups 
from mailerlitecli.utils.utils import args_parse
import requests
import re
import yaml
import json
from prettytable import PrettyTable

def getCampaignIDByName(campaign_name):
    pass

class Campaign(object):

    def __init__(self, mailerlite_api_token):
        self.mailerlite_api_token = mailerlite_api_token
        self.post_headers = {'Content-Type': 'application-json', 'X-MailerLite-ApiKey': '{}'.format(mailerlite_api_token)}

    def import_content(self, campaign_id ,html_file, plain_text_file="{$unsubscribe}\n{$url}"):
        mailerlite_api_token = self.mailerlite_api_token
        headers = self.post_headers

        _html = open(html_file, "r").read()
        
        _content_data = {
                'html': '{}'.format(_html),
                'plain': '{}'.format(plain_text_file)
                }

        _import_content = requests.put('https://api.mailerlite.com/api/v2/campaigns/'+str(campaign_id)+'/content', headers=headers, json=_content_data)
        print(_content_data)
        print(_import_content.content)

    def status(self, status):
        '''
        mailerlite-cli campaign status {sent,draft,outbox}
        '''
        mailerlite_api_token = self.mailerlite_api_token
        response_table = PrettyTable()
        response_table.field_names = ['ID', 'Name', 'Type', 'Status', 'Total Recipients', 'Opened %', 'Clicked %', 'Creation Date', 'Send Date']

        _campaigns_status_all = requests.get('https://api.mailerlite.com/api/v2/campaigns/'+str(status), headers={'X-MailerLite-ApiKey': '{}'.format(mailerlite_api_token)}).json()
        
        for _campaign in _campaigns_status_all:
            _id = _campaign['id']
            _name = _campaign['name']
            _type = _campaign['type']
            _status = _campaign['status']
            _recipients = _campaign['total_recipients']
            _opened = _campaign['opened']['rate']
            _clicked = _campaign['clicked']['rate']
            _date_created = _campaign['date_created']
            _date_send = _campaign['date_send']

            response_table.add_row(['{}'.format(_id), '{}'.format(_name), '{}'.format(_type),
                '{}'.format(_status), '{}'.format(_recipients), '{}'.format(_opened),
                '{}'.format(_clicked), '{}'.format(_date_created), '{}'.format(_date_send)])
            
        print(response_table)

        #print(_campaigns_status_all.content)

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
        elif _type == "regular":
            _groups = _config['groups']
            _subject = _config['subject']

            _data = {
                    'type': 'regular',
                    'subject': '{}'.format(_subject),
                    'groups': '{}'.format(_groups)
                    }
        else:
            raise ValueError("Campaign type not supported")
        
        _json_data = json.dumps(_data)
        _campaign_create = requests.post('https://api.mailerlite.com/api/v2/campaigns', headers=headers, json=_json_data)

        print("{0}\n{1}\n{2}".format(_campaign_create.status_code, _campaign_create.content, _json_data))

    def send(self, campaign_id,schedule=0, *extra_fields):
        '''
        Send and schedule campaigns, has options for managing
        followups and analytics.
        '''
        mailerlite_api_token = self.mailerlite_api_token
        headers = self.post_headers

        _data_dict = args_parse(extra_fields)

        if schedule in [1, 'enable', 'yes', 'on']:
            _data_dict['type'] = 2
            _campaign_send = requests.post('https://api.mailerlite.com/api/v2/campaigns/'+str(campaign_id)+'/actions/send',
                    headers = headers, json=_data_dict)
        else:
            _campaign_send = requests.post('https://api.mailerlite.com/api/v2/campaigns/'+str(campaign_id)+'/actions/send',
                    headers = headers)

        print(_campaign_send.content)

