from ytmusicapi import YTMusic
brandacc = '107367647290977345029'

if (__name__ == "__main__"):
	ytmusic = YTMusic('headers_auth.json',brandacc)
	playlistId = 'PL30yA52yH7dBOBZHK-7I1nE4_v5F3-d57'
	search_results = ytmusic.search("peaches justin beiber",filter="songs")
	ytmusic.add_playlist_items(playlistId, [search_results[0]['videoId']])
	print(search_results[0])