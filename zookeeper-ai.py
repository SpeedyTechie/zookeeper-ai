import os
import pickle
import datetime
from rauth import OAuth2Service

def save_data(data):
    pickle.dump(data, open('data.txt', 'w'))

def get_data():
    data = {}
    if os.path.isfile('data.txt'):
        data = pickle.load(open('data.txt', 'r'))
    
    if 'client_id' in data:
        client_id = data['client_id']
    else:
        client_id = raw_input('Enter Client ID: ')
        data['client_id'] = client_id
    
    if 'client_secret' in data:
        client_secret = data['client_secret']
    else:
        client_secret = raw_input('Enter Client Secret: ')
        data['client_secret'] = client_secret
    
    save_data(data)
    
    return data


def oauth_get_service(client_id, client_secret):
    oauth_service = OAuth2Service(
        name='yahoo',
        client_id=client_id,
        client_secret=client_secret,
        access_token_url='https://api.login.yahoo.com/oauth2/get_token',
        authorize_url='https://api.login.yahoo.com/oauth2/request_auth',
        base_url='https://fantasysports.yahooapis.com/fantasy/v2/'
    )
    return oauth_service


def oauth_get_access_token(data):
    if 'access_token' in data and 'expires' in data and 'refresh_token' in data:
        if data['expires'] <= datetime.datetime.now():
            oauth_service = oauth_get_service(data['client_id'], data['client_secret'])
            raw_response = oauth_service.get_raw_access_token(data={'refresh_token': data['refresh_token'], 'grant_type': 'refresh_token', 'redirect_uri': 'oob'}).json()
            data['access_token'] = raw_response['access_token']
            data['expires'] = datetime.datetime.now() + datetime.timedelta(0, raw_response['expires_in'] - 120)
            data['refresh_token'] = raw_response['refresh_token']
            save_data(data)
    else:
        oauth_service = oauth_get_service(data['client_id'], data['client_secret'])
        print oauth_service.get_authorize_url(**{'redirect_uri': 'oob', 'response_type': 'code'})
        code = raw_input('Visit the URL above, and enter the code shown on the page: ')
        raw_response = oauth_service.get_raw_access_token(data={'code': code, 'grant_type': 'authorization_code', 'redirect_uri': 'oob'}).json()
        data['access_token'] = raw_response['access_token']
        data['expires'] = datetime.datetime.now() + datetime.timedelta(0, raw_response['expires_in'] - 120)
        data['refresh_token'] = raw_response['refresh_token']
        save_data(data)
    
    return data['access_token']

        
def oauth_get_session(data):
    oauth_service = oauth_get_service(data['client_id'], data['client_secret'])
    return oauth_service.get_session(oauth_get_access_token(data))


def main():
    data = get_data()
    oauth_session = oauth_get_session(data)
    test_json = oauth_session.get('game/nfl/position_types', params={'format': 'json'}).json()
    print test_json


if __name__ == '__main__': main()