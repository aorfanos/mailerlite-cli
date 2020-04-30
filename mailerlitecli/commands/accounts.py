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

    def info(self):
        mailerlite_api_token = self.mailerlite_api_token
        response_table = PrettyTable()
        response_table.field_names = ['Key', 'Value']
        _account_info = requests.get("https://api.mailerlite.com/api/v2/me", headers={'X-MailerLite-ApiKey': '{}'.format(mailerlite_api_token)}).json()
        #for _account in _account_info['account']:
        _email = _account_info['account']['email']
        _from = _account_info['account']['from']
        _id = _account_info['account']['id']
        _name = _account_info['account']['name']
        _subdomain = _account_info['account']['subdomain']
        _tz_gmt = _account_info['account']['timezone']['gmt']
        _tz_id = _account_info['account']['timezone']['id']
        _tz_time = _account_info['account']['timezone']['time']
        _tz_timezone = _account_info['account']['timezone']['timezone']
        _tz_title = _account_info['account']['timezone']['title']
        
        response_table.add_row(['ID', '{}'.format(_id)])
        response_table.add_row(['Name', '{}'.format(_name)])
        response_table.add_row(['Account e-mail', '{}'.format(_email)])
        response_table.add_row(['FROM field', '{}'.format(_from)])
        response_table.add_row(['Subdomain', '{}'.format(_subdomain)])
        response_table.add_row(['Timezone ID', '{}'.format(_tz_id)])
        response_table.add_row(['Timezone', '{}'.format(_tz_timezone)])
        response_table.add_row(['Timezone Title', '{}'.format(_tz_title)])
        response_table.add_row(['Local Time', '{}'.format(_tz_time)])
        response_table.add_row(['Timezone GMT', '{}'.format(_tz_gmt)])
        print(response_table)

    def double_opt_in(self, disable=False):
        mailerlite_api_token = self.mailerlite_api_token
        response_table = PrettyTable()
        response_table.field_names = ['Key', 'Value']
        headers = {
                'Content-Type': 'application/json',
                'X-MailerLite-ApiKey': '{}'.format(mailerlite_api_token),
                }
        if disable == False:
            _double_opt_in_status = requests.post("https://api.mailerlite.com/api/v2/settings/double_optin",
                    headers=headers,
                    json={'enable': 'true'})
            response_table.add_row(['Double opt-in status','Enabled'])
        elif disable == True:
            _double_opt_in_status = requests.post("https://api.mailerlite.com/api/v2/settings/double_optin",
                    headers=headers,
                    json={'enable': 'false'})
            response_table.add_row(['Double opt-in status','Disabled'])
        else:
            _double_opt_in_status = requests.get("https://api.mailerlite.com/api/v2/settings/double_optin",
                    headers=headers).json()
            _is_enabled = _double_opt_in_status['enabled']
            for _path in _double_opt_in_status['previewPaths']:
                _email_path = _path['emailPath']
                _page_path = _path['pagePath']
            response_table.add_row(['Double opt-in status','{}'.format(_is_enabled)])
            response_table.add_row(['E-mail preview path','{}'.format(_email_path)])
            response_table.add_row(['Double opt-in status','{}'.format(_page_path)])

        print(response_table)
