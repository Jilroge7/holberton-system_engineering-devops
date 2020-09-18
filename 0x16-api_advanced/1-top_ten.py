#!/usr/bin/python3
""" get top ten posts """
import requests


def top_ten(subreddit):
    """ function to retrieve top ten posts for subreddit """

    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    about = requests.get(url, headers={"User-Agent": "User"},
                         allow_redirects=False)
    about = about.json()
    outdict = about.get("data")
    child = outdict.get("children")
    if about.status_code != 200:
        print(None)
        return
    else:
        for key in child:
            insdict = key.get("data")
            toplist = insdict.get("title")
            print(toplist)
        return