import requests
import json

# Spotify URI for my Account
URI = '1230626905'
clientID = 'c1ea3c73f6c54c0296e914eacf59ff78'
clientSecret = '9cb60e86350544efb91f44f570bcc49a'
token = 'Bearer BQDc5tGKrQvioWjPyJiFQg3E3I2SAXZNPqzDjFAjfGryMsDH1aXx05yAV3Z2oU1O2aa7snoCpwXpQU43Bd9x3H7wcZdwivcHkUAq0vdfDbX4wOKA9eeDHrmij8lWBpx8jxErxj8O86qa_bziZqSsi5f5NwyJC8Q'

# Get the authorization token

# https://accounts.spotify.com/authorize?client_id=c1ea3c73f6c54c0296e914eacf59ff78&scope=playlist-read-private&response_type=code&redirect_uri=https%3A%2F%2Fgoogle.com%2F
# curl -H "Authorization: Basic YzFlYTNjNzNmNmM1NGMwMjk2ZTkxNGVhY2Y1OWZmNzg6OWNiNjBlODYzNTA1NDRlZmI5MWY0NGY1NzBiY2M0OWE=" -d grant_type=authorization_code -d code=AQANOeM6B7aS8fZlVVr2Us33cSG6U0N43xQhyh8KVhZLwb5FibyC9sITQZsWNGjMnowf30DrfTdhtAOpgnzwvsI3hPlDCZp5ay-vt22YF-C6zOCHQ3oXngel5S1xD1V1ePVsY4MpUWzhDfTBAzqL2Zf0W29MY_OPo7OeTL6W43l652jssgStWxIKVGqaA3Q7HpjVz1tziF7xYOmmtrRnng -d redirect_uri=https%3A%2F%2Fgoogle.com%2F https://accounts.spotify.com/api/token

playlistRequestURL = 'https://api.spotify.com/v1/users/' + URI + '/playlists'

# GET Request getting the playlists from the user

playlistRequest = requests.get(playlistRequestURL, headers={"Authorization": token})
playlistData = playlistRequest.json()
playlistID = None

for i in playlistData['items']:
    playlistName = i['name']
    # print ("%s, %s" % (playlistName, playlistID))

    if playlistName == 'edm':
        print(playlistName + "'s ID is: " + i['id'])
        playlistID = i['id']


print(playlistID)
# GET Request getting the track names from the playlist

trackRequestURL = 'https://api.spotify.com/v1/playlists/' + playlistID + '/tracks'

trackRequest = requests.get(trackRequestURL, headers={"Authorization": token})
trackData = trackRequest.json()
trackList = []

for t in trackData['items']:
    trackName = t['track']['name']
    trackList.append(trackName)
    print(trackName)


print(trackList)
