import os
from dotenv import load_dotenv
from ytmusicapi import YTMusic
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

load_dotenv()
SPOTIPY_CLIENT_ID = os.getenv("SPOTIPY_CLIENT_ID")
SPOTIPY_CLIENT_SECRET = os.getenv("SPOTIPY_CLIENT_SECRET")
BRANDACC = os.getenv("BRANDACC")

sp=spotipy.Spotify(auth_manager=SpotifyClientCredentials())
ytmusic = YTMusic('headers_auth.json',BRANDACC)

SpotifyPlaylist_id='spotify:playlist:6JYZRixOceNAx6mr7bCf2q'
YTplaylistId = 'VLPL30yA52yH7dCLOJfmudocD5eDvZry9dHd'

if (__name__ == "__main__"):
    numsongs = sp.playlist_items(playlist_id=SpotifyPlaylist_id,fields='total') ['total'] #determine number of songs in spotify playlist
    offset = 0 #init offset for song list
    tracks = [] #list of all tracks from spotify playlist
    while offset<=numsongs:
        songs = sp.playlist_items(playlist_id=SpotifyPlaylist_id,fields='items.track.name,items.track.artists.name',offset=offset) #get songs in batches of 100
        tracks.append(songs['items'])
        offset+=100
    tracks=[y for x in tracks for y in x] #flattening list
    for i in tracks:
        searchterm = i['track']['name'] +" "+ i['track']['artists'][0]['name'] #create search term
        search_results = ytmusic.search(searchterm,filter="songs") #search for song
        print("Added: ",searchterm)
        ytmusic.add_playlist_items(YTplaylistId, [search_results[0]['videoId']]) #add to YTmusic playlist
    
    