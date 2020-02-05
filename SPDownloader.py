import requests
import json

URI = '1230626905'
# clientID = 'c1ea3c73f6c54c0296e914eacf59ff78'
# clientSecret = '9cb60e86350544efb91f44f570bcc49a'
spotifyToken = 'Bearer BQBIE2GeWMSoDQXKBdXv-dq13RdN1TeKcb0wIXlLCT-LwDgQ7gP4tqdgBFVCHpuEhd3KitTHJkHGH7tLva4-EDqLSwHNICus8qjF6DCYhXngcMgzAq7LbR29PJA6-TitvvTALMzKmL4-KhdT3rg_pbipxeWQdAI'

# Get the authorization token, clientID:clientSecretID need to be base64 encoded
# Click on URL to get Authorization Token
# Copy Auth Return token into curl command code
# Execute curl command to get token variable, update spotifyToken
# Execute script

# https://accounts.spotify.com/authorize?client_id=c1ea3c73f6c54c0296e914eacf59ff78&scope=playlist-read-private&response_type=code&redirect_uri=https%3A%2F%2Fgoogle.com%2F
# curl -H "Authorization: Basic YzFlYTNjNzNmNmM1NGMwMjk2ZTkxNGVhY2Y1OWZmNzg6OWNiNjBlODYzNTA1NDRlZmI5MWY0NGY1NzBiY2M0OWE=" -d grant_type=authorization_code -d code=AQCZf9iHleoaHhynpIBVlVaS8iJqlfkxv80q0KgMpH0eJS_yx72uSUwV_arM3Fau9pTGDb5i-GAHnd--FVk6we190_cNrTLkxfSFQLtrUX-tU61GJPF5RPlJZWrlKKbF6QtGV-Kriul3cTikvtOFKRaOdpftt7Ivx2ouPbsZNHTUz9VgwSE2XsCuRIRcZWNhtddFDSWK0gMAlav31CEQmw -d redirect_uri=https%3A%2F%2Fgoogle.com%2F https://accounts.spotify.com/api/token

playlistRequestURL = 'https://api.spotify.com/v1/users/' + URI + '/playlists'

# GET Request getting the playlists from the user

playlistRequest = requests.get(playlistRequestURL, headers={"Authorization": spotifyToken})
playlistData = playlistRequest.json()
playlistID = None

for i in playlistData['items']:
    playlistName = i['name']
    if playlistName == 'SPDownloader':
        playlistID = i['id']

# GET Request getting the track names from the playlist

trackRequestURL = 'https://api.spotify.com/v1/playlists/' + playlistID + '/tracks'

trackRequest = requests.get(trackRequestURL, headers={"Authorization": spotifyToken})
trackData = trackRequest.json() 
print(trackData)
trackList = []

for t in trackData['items']:
    trackName = t['track']['name']
    trackArtist = t['track']['artists'][0]['name']
    trackList.append(trackName + ' ' + trackArtist)
    print(trackName + ' ' + trackArtist) 

# Deezer OAuth

# App ID: 391704
# Secret: 64f056ae7cca43c2b1045b374b74ce71
# OAuth URL : https://connect.deezer.com/oauth/auth.php?app_id=391704&redirect_uri=https://example.org&perms=basic_access

# Get Access Token by replacing Code with above code: 
# https://connect.deezer.com/oauth/access_token.php?app_id=391704&secret=64f056ae7cca43c2b1045b374b74ce71&code=frb7a137de9a8738e81df78d763fe358

# Update deezer token with new access token
deezerToken = 'frNO8y6MbeWpDZICI98CRv7FIg2cGJTTVD1j0dLYeumNiqlxZ9w'
finalURLs = []

for t in trackList:
    deezerURL = 'https://api.deezer.com/search?q=' + t
    deezerRequest = requests.get(deezerURL, headers={"Authorization": deezerToken})
    deezerData = deezerRequest.json()
    finalURLs.append(deezerData['data'][0]['link'])

# Create a new file and copy URLs into the text file

file = open("downloadLinks.txt", "w")
for t in finalURLs:
    file.write(t + '\n')
file.close()

# All the lists should now be in a downloadList.txt file in the folder