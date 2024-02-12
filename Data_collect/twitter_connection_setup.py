# API Twitter

import tweepy
# We import our access keys:
import Data_collect.Credentials.Credentials_paul as cd_paul
import Data_collect.Credentials.Credentials_Hugo as cd_hugo
import Data_collect.Credentials.Credentials_Noe as cd_noe


def twitter_setup(user="hugo"):
    """
    Utility function to setup the Twitter's API
    with an access keys provided in a file credentials.py
    :return: the authentified API
    """
    # Authentication and access using keys:
    if user == "hugo":
        auth = tweepy.OAuthHandler(
            cd_hugo.CONSUMER_KEY, cd_hugo.CONSUMER_SECRET)
        auth.set_access_token(cd_hugo.ACCESS_TOKEN, cd_hugo.ACCESS_SECRET)
    elif user == "paul":
        auth = tweepy.OAuthHandler(
            cd_paul.CONSUMER_KEY, cd_paul.CONSUMER_SECRET)
        auth.set_access_token(cd_paul.ACCESS_TOKEN, cd_paul.ACCESS_SECRET)
    elif user == "noe":
        auth = tweepy.OAuthHandler(
            cd_noe.CONSUMER_KEY, cd_noe.CONSUMER_SECRET)
        auth.set_access_token(cd_noe.ACCESS_TOKEN, cd_noe.ACCESS_SECRET)

    # Return API with authentication:
    api = tweepy.API(auth)
    return api
