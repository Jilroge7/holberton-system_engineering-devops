#!/usr/bin/python3
""" get top ten posts """
import requests
from pprint import pprint


def top_ten(subreddit):
    """ function to retrieve top ten posts for subreddit """

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    about = requests.get(url, headers={"User-Agent": "User"},
                         allow_redirects=False).json()
    try:
        for posts in about:
            while len(posts < 10):
                top = about["data"].get("title")
                print(top)
    except:
        print(None)
