#!/usr/bin/python

import mailerlitecli.commands.api_transactions as api
import mailerlitecli.commands.campaigns as campaigns
import mailerlitecli.commands.groups as groups
import mailerlitecli.commands.accounts as accounts
import mailerlitecli.commands.subscribers as subscribers
import mailerlitecli.utils.configfiles
import os
import fire

try:
    mailerlite_api_token = os.environ['MAILERLITE_API_TOKEN']
except KeyError as e:
    print("Message: {}".format(e))

class Pipeline(object):

    def __init__(self):
        self.group = groups.Group(mailerlite_api_token)
        self.group.subscriber = groups.subscriber(mailerlite_api_token)
        self.campaign = campaigns.Campaign(mailerlite_api_token)
        self.account = accounts.Account(mailerlite_api_token)
        self.subscriber = subscribers.Subscriber(mailerlite_api_token)

if __name__ == "__main__":
    fire.Fire(Pipeline)
