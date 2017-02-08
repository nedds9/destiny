import api_key

API_URL = 'https://www.bungie.net/platform/Destiny'
PS4_TYPE = '2'
ALL_TYPE = 'All'
USER_NAME = 'nedds9'
ID_KEY = 'membershipId'

HEADERS = { "X-API-Key" : api_key.get_api_key() }

PLAYER_PATH = '%s/SearchDestinyPlayer/%s/%s/' % (API_URL, PS4_TYPE, USER_NAME)

def get_stats_path(membership_id):
    return '%s/Stats/Account/%s/%s/' % (API_URL, PS4_TYPE, membership_id)
