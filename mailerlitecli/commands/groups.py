import requests
from prettytable import PrettyTable

def createGroup(mailerlite_api_token, group_name="New Group by mailerlite-cli"):
    headers = {
            'Content-Type': 'application/json',
            'X-MailerLite-ApiKey': '{}'.format(mailerlite_api_token),
            }
    _create_group = requests.post("https://api.mailerlite.com/api/v2/groups", headers=headers, json={'name': '{}'.format(group_name)})
    print("Created group with name: {}".format(group_name))

def getGroups(mailerlite_api_token, full_info=False):
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

def getGroupNameByID(mailerlite_api_token, group_id):
    _group_list = requests.get("https://api.mailerlite.com/api/v2/groups", headers={'X-MailerLite-ApiKey': '{}'.format(mailerlite_api_token)}).json()
    for _group in _group_list:
        if _group['id'] == group_id:
            _group_name = _group['name']
            return("Group ID {0} corresponds to name: {1}".format(group_id, _group_name))
            break
        else:
            return("No records found for ID: {}".format(group_id))
            break

def getGroupIDByName(mailerlite_api_token, group_name):
    _group_list = requests.get("https://api.mailerlite.com/api/v2/groups", headers={'X-MailerLite-ApiKey': '{}'.format(mailerlite_api_token)}).json()
    for _group in _group_list:
        if _group['name'] == group_name:
            _group_id = _group['id']
            return("Group name {0} corresponds to ID: {1}".format(group_name, _group_id))
            break
        else:
            return("No records found for name: {0}".format(group_name))
            break
    
        


