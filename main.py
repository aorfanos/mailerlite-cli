#!/usr/bin/python

import mailerlitecli.commands.api_transactions as api
import mailerlitecli.commands.campaigns as campaigns
import mailerlitecli.commands.groups as groups
import os

try:
    mailerlite_api_token = os.environ['MAILERLITE_API_TOKEN']
except KeyError as e:
    print("Message: {}".format(e))

if __name__ == "__main__":
    #api_status.checkAPIStatus(mailerlite_api_token)

    #_campaigns_all = campaigns.getCampaignStatus(mailerlite_api_token)
    #_create_campaign = campaigns.createABCampaign(mailerlite_api_token, )
    #groups.createGroup(mailerlite_api_token)
    #print(groups.getGroups(mailerlite_api_token))

    groups.getGroupNameByID(mailerlite_api_token, 102814156)
