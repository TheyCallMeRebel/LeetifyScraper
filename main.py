from leetify import leetify
import requests
import logging





with requests.Session() as r:
    url = 'https://api.leetify.com/api/profile/76561198050765093/'
    page = r.get(url)
    stats = leetify.grabPlayer(page)
    if stats == 'KeyError':
        print('There was a key error placeholder')


