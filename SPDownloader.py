import requests
import json

URI = '1230626905'
# clientID = 'c1ea3c73f6c54c0296e914eacf59ff78'
# clientSecret = '9cb60e86350544efb91f44f570bcc49a'
spotifyToken = 'Bearer BQASL7wgtkqKGrdd8Fy6VM07OKBhO4zswhhU0fgtCGis3ZqpOUwQTg4kAPfMw7RDlcIoG4GrZEZ7zny9bI_LmJ3gOvR2NBoOB--02k-K_FaOYyV5Yya0cPicdZqwz8VUdD5ElFux3ItTxca3dCVr1oUbCelWX-k'

# Get the authorization token, clientID:clientSecretID need to be base64 encoded
# Click on URL to get Authorization Token
# Copy Auth Return token into curl command code
# Execute curl command to get token variable, update spotifyToken
# Execute script

# https://accounts.spotify.com/authorize?client_id=c1ea3c73f6c54c0296e914eacf59ff78&scope=playlist-read-private&response_type=code&redirect_uri=https%3A%2F%2Fgoogle.com%2F
# curl -H "Authorization: Basic YzFlYTNjNzNmNmM1NGMwMjk2ZTkxNGVhY2Y1OWZmNzg6OWNiNjBlODYzNTA1NDRlZmI5MWY0NGY1NzBiY2M0OWE=" -d grant_type=authorization_code -d code=AQCBMQo5jiblxBD_AgSlr7MlsfyNDNJ3hzzrr0m-v6rwRb0js_HFR7GWSnFlnEtRINt96Vbtu_mHJSMlGHPGeY77hQvKW4JHErwM8Vgi4gvnToJXTHkgSokwCwpeIKgB8vw3JIsWuoc7e3Pdh0ddq_d60Igwb1YD1trQ2yb06NgyxxdqJC1vKE49rKMV9XhWtvBGRiO29crxohCXqL9QDQ -d redirect_uri=https%3A%2F%2Fgoogle.com%2F https://accounts.spotify.com/api/token

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
trackList = []

for t in trackData['items']:
    trackName = t['track']['name']
    trackList.append(trackName)
    print(trackName) 

# Deezer OAuth

# App ID: 391704
# Secret: 64f056ae7cca43c2b1045b374b74ce71
# OAuth URL : https://connect.deezer.com/oauth/auth.php?app_id=391704&redirect_uri=https://example.org&perms=basic_access

# Get Access Token by replacing Code with above code: 
# https://connect.deezer.com/oauth/access_token.php?app_id=391704&secret=64f056ae7cca43c2b1045b374b74ce71&code=fr74a75a8ac3f83966f7c35baa848af0

# Update deezer token with new access token
deezerToken = 'frlOepZxHJVpTcl1LM2TdT29rukfspfA8QEJNf6DPQsDcU3xOFM'
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