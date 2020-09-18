#!/usr/bin/python3
""" return # of subscribers """
import requests


def number_of_subscribers(subreddit):
    """ function to return # of subscribers from specific subreddit """
    try:
        url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
        about = requests.get(url, headers={"User-Agent": "User"},
                             allow_redirects=False).json()
        count = about["data"].get("subscribers")
        return count
    except:
        return 0
