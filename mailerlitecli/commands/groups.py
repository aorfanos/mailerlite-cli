import requests, os
from prettytable import PrettyTable

def getGroupNameByID(mailerlite_api_token, group_id):
    _group_list = requests.get("https://api.mailerlite.com/api/v2/groups", headers={'X-MailerLite-ApiKey': '{}'.format(mailerlite_api_token)}).json()
    for _group in _group_list:
        print("Checking: {0} vs {1}".format(_group['id'], group_id))
        if _group['id'] == group_id:
            _group_name = _group['name']
            return("{1}".format(_group_name))
        else:
            continue

def getGroupIDByName(mailerlite_api_token, group_name):
    _group_list = requests.get("https://api.mailerlite.com/api/v2/groups", headers={'X-MailerLite-ApiKey': '{}'.format(mailerlite_api_token)}).json()
    for _group in _group_list:
        print("Check: {0} vs {1}".format(group_name, _group['name']))
        if _group['name'] == group_name:
            _group_id = _group['id']
            return("{}".format(_group_id))
        else:
            continue

class Group(object):

    def __init__(self, mailerlite_api_token):
        self.mailerlite_api_token = mailerlite_api_token

    def create(self, group_name="New Group by mailerlite-cli"):
        mailerlite_api_token = self.mailerlite_api_token
        headers = {
                'Content-Type': 'application/json',
                'X-MailerLite-ApiKey': '{}'.format(mailerlite_api_token),
                }
        _create_group = requests.post("https://api.mailerlite.com/api/v2/groups", headers=headers, json={'name': '{}'.format(group_name)})
        print("Created group with name: {}".format(group_name))

    def list(self, full_info=False):
        mailerlite_api_token = self.mailerlite_api_token
        response_table = PrettyTable()
        if full_info is not False:
            response_table.field_names = ['ID', 'Name', 'Parent', 'Total', 'Active', 'Unsubscribed', 'Bounced', 'Unconfirmed', 'Junk', 'Sent', 'Opened', 'Clicked', 'Date_Created', 'Date_Updated' ]
        else:
            response_table.field_names = ['ID', 'Name', 'Total', 'Sent', 'Opened', 'Clicked']
        _group_list = requests.get("https://api.mailerlite.com/api/v2/groups", headers={'X-MailerLite-ApiKey': '{}'.format(mailerlite_api_token)}).json()
        for _group in _group_list:
            if full_info is not False:
                _group_id = _group['id']
                _group_name = _group['name']
                _group_parent_id = _group['parent_id']
                _group_total = _group['total']
                _group_active = _group['active']
                _group_unsubscribed = _group['unsubscribed']
                _group_bounced = _group['bounced']
                _group_unconfirmed = _group['unconfirmed']
                _group_junk = _group['junk']
                _group_sent = _group['sent']
                _group_opened = _group['opened']
                _group_clicked = _group['clicked']
                _group_date_created = _group['date_created']
                _group_date_updated = _group['date_updated']

                table_row = ([ _group_id, _group_name, _group_parent_id, _group_total,
                    _group_active, _group_unsubscribed, _group_bounced, _group_unconfirmed,
                   _group_junk, _group_sent, _group_opened, _group_clicked,
                   _group_date_created, _group_date_updated]
                   )

                response_table.add_row(table_row)
            else:
               _group_id = _group['id']
               _group_name = _group['name']
               _group_total = _group['total']
               _group_sent = _group['sent']
               _group_opened = _group['opened']
               _group_clicked = _group['clicked']

               table_row = ([_group_id, _group_name, _group_total,
                   _group_sent, _group_opened, _group_clicked])

               response_table.add_row(table_row)

        return(response_table)

    def update(self, group_name="", group_id="", parameter_key="", parameter_value=""):
        mailerlite_api_token = self.mailerlite_api_token
        headers = { 
                'Content-Type': 'application/json',
                'X-MailerLite-ApiKey': '{}'.format(mailerlite_api_token),
                }

        param = {'{}'.format(parameter_key): '{}'.format(parameter_value)}

        if group_id == "":
            group_id = str(getGroupIDByName(mailerlite_api_token, group_name))
            _update_group_parameter = requests.put("https://api.mailerlite.com/api/v2/groups/"+group_id, headers=headers, json=param)
        else:
            _update_group_parameter = requests.put("https://api.mailerlite.com/api/v2/groups/"+str(group_id), headers=headers, json=param)

        return("[{0}] Updated group ID {1} with key/value {2}/{3}".format(_update_group_parameter.status_code, 
            group_id, parameter_key, parameter_value  ))

    def delete(self, group_id="", group_name=""):
        mailerlite_api_token = self.mailerlite_api_token
        headers = {
                'Content-Type': 'application/json',
                'X-MailerLite-ApiKey': '{}'.format(mailerlite_api_token),
                }
        if group_id == "":
            group_id = str(getGroupIDByName(mailerlite_api_token, group_name))
            _delete_group = requests.delete("https://api.mailerlite.com/api/v2/groups/"+group_id, headers=headers)
        elif group_id != "":
            _delete_group = requests.delete("https://api.mailerlite.com/api/v2/groups/"+str(group_id), headers=headers)

        print("Deleted group {0} with ID {1}".format(group_name, group_id))

    def show(self, group_id="", group_name=""):
        mailerlite_api_token = self.mailerlite_api_token
        response_table = PrettyTable()
        response_table.field_names = ['Key', 'Value']
        if group_id == "":
            group_id = str(getGroupIDByName(mailerlite_api_token, group_name))
            _show_group_info = requests.get("https://api.mailerlite.com/api/v2/groups/"+group_id, headers={'X-MailerLite-ApiKey': '{}'.format(mailerlite_api_token)}).json()
        elif group_id != "":
            _show_group_info = requests.get("https://api.mailerlite.com/api/v2/groups/"+str(group_id), headers={'X-MailerLite-ApiKey': '{}'.format(mailerlite_api_token)}).json()

        response_table.add_row(['Name', '{}'.format(_show_group_info['name'])])
        response_table.add_row(['ID', '{}'.format(_show_group_info['id'])])
        response_table.add_row(['Total people in group', '{}'.format(_show_group_info['total'])])
        response_table.add_row(['Total active', '{}'.format(_show_group_info['active'])])
        response_table.add_row(['Total bounced', '{}'.format(_show_group_info['bounced'])])
        response_table.add_row(['Total unconfirmed', '{}'.format(_show_group_info['unconfirmed'])])
        response_table.add_row(['Total junk', '{}'.format(_show_group_info['junk'])])
        response_table.add_row(['Total sent', '{}'.format(_show_group_info['sent'])])
        response_table.add_row(['Total opened', '{}'.format(_show_group_info['opened'])])
        response_table.add_row(['Total clicked', '{}'.format(_show_group_info['clicked'])])
        response_table.add_row(['Date created', '{}'.format(_show_group_info['date_created'])])
        response_table.add_row(['Data updated', '{}'.format(_show_group_info['date_updated'])])

        print(response_table)

