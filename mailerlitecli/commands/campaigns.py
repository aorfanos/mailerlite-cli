import requests
import re

def getCampaignStatus(mailerlite_api_token):
    _campaigns_status_all = requests.get('https://api.mailerlite.com/api/v2/campaigns', headers={'X-MailerLite-ApiKey': '{}'.format(mailerlite_api_token)}).json()
    print(_campaigns_status_all)

def createABCampaign(mailerlite_api_token, groups, values, send_type, ab_win_type, split_part):
    headers = {
            "Content-Type": "application/json",
            "X-MailerLite-ApiKey": "{}".format(mailerlite_api_token),
            }

    _winner_after = re.split('(\D+)', winner_after)
    _winner_after_time_int = _winner_after[0]
    _winner_after_type = _winner_after[1]

    if campaign_type == "ab":
        data = {
                'groups': '{}'.format(groups),
                'type': 'ab',
                'ab_settings': {
                    'send_type': '{}'.format(send_type),
                    'values': '{}'.format(values),
                    'ab_win_type': '{}'.format(ab_win_type),
                    'winner_after': '{}'.format(_winner_after),
                    'winner_after_type': '{}'.format(_winner_after_type),
                    'split_part': '{}'.format(split_part),
                    },
                }

        _create_campaign = requests.post("https://api.mailerlite.com/api/v2/campaigns", headers=headers, json=data)

        print(_create_campaign)
