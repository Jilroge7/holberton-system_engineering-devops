#!/usr/bin/python3
""" get top ten posts """
import requests


def top_ten(subreddit):
    """ function to retrieve top ten posts for subreddit """

    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    about = requests.get(url, headers={"User-Agent": "User"},
                         allow_redirects=False)
    about = about.json()
    try:
        outdict = about.get("data")
        child = outdict.get("children")
        for key in child:
            insdict = key.get("data")
            toplist = insdict.get("title")
            print(toplist)
        return
    except:
        print(None)
        return
