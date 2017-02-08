#!/usr/bin/python

# Test file for getting user stats
import requests
import bungie_config

def get_response(request):
    response = request.json().get('Response', [])
    if len(response) > 0:
        return response[0]
    else:
        return response

def get_membership_id():
    request = requests.get(bungie_config.PLAYER_PATH,
                           headers = bungie_config.HEADERS)
    response = get_response(request)
    if bungie_config.ID_KEY in response:
        return response[bungie_config.ID_KEY]
    else:
        raise RuntimeError("Unable to get membership id")

def get_user_stats():
    membership_id = get_membership_id()
    request = requests.get(bungie_config.get_stats_path(membership_id),
                           headers = bungie_config.HEADERS)
    print request.json()

if __name__ == '__main__':
    get_user_stats()
