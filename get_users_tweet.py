
# Reference https://developer.twitter.com/en/docs/twitter-api/v1/tweets/timelines/api-reference/get-statuses-user_timeline

import tweepy


USER_ID="chamath"
TEXT_TO_GREP="investing"


def get_twitter_auth():
    # Create a profile on https://developer.twitter.com/ and copy the 
    # consumer_key, consumer_secret, access_token, access_secret.
    consumer_key = <consumer_key>
    consumer_secret = <consumer_secret>
    access_token = <access_token>
    access_secret = <access_secret>
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    return auth


def get_twitter_client():
    auth = get_twitter_auth()
    twitter_client = tweepy.API(auth, wait_on_rate_limit=True)
    return twitter_client


if __name__ == "__main__":
    client = get_twitter_client()
    for tweet in tweepy.Cursor(client.user_timeline, screen_name=USER_ID,
                               count=None, since_id=None, max_id=None, trim_user=False,
                               exclude_replies=True, contributor_details=False,
                               include_entities=False, include_rts=False).items(200):
        if TEXT_TO_GREP in tweet.text:
            print(f"{tweet.text} \n")
