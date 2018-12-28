import json
import tweepy
import random
import requests


# Twitter tokens configuration
config = json.load(open("tokens.json"))['twitter']
auth = tweepy.OAuthHandler(config["consumer_key"], config["consumer_secret"])
auth.set_access_token(config["access_token"], config["access_token_secret"])
api = tweepy.API(auth)


def select_from_file(filename):
    # Create sequence from choices list
    choices = []
    file = open('lists/%s' % filename, 'r')
    f = file.readlines()
    file.close()
    for choice in f:
        choices.append(choice.rstrip())

    return select_from_list(choices)


def select_from_list(l):
    # Get last pulse generated by UChile's beacon
    LAST_PULSE_URL = "https://random.uchile.cl/beacon/2.0/pulse/last"
    req = requests.get(LAST_PULSE_URL)
    seed = bytes.fromhex(json.loads(req.content)["pulse"]["outputValue"])

    random.seed(seed)
    return random.choice(l)
