import sys
import spotipy
import pprint
import os
import subprocess
import spotipy.util as util
import datetime

# Space seperated permissions to request from Spotify
scope = "user-library-read playlist-modify-public playlist-modify-private"

# Creates a playlist named has date of this week's Monday
def create_playlist(username, sp):
    sp.trace = False
    playlist_name = get_playlist_title()
    playlist_description = 'Archive of one week\'s discover weekly'
    sp.user_playlist_create(username, playlist_name, True)  # True indicates it is a public playlist

# Returns id of new playlist that has date of this week's Monday
def get_playlist_id(username,sp):
    playlists = sp.user_playlists(username)
    for playlist in playlists['items']:
        if playlist['name'] == get_playlist_title():
            pprint.pprint(playlist)
            return playlist['id']
            
def get_playlist_title():
    today = datetime.date.today()
    monday = today - datetime.timedelta(days=today.weekday())
    title = "DW of " + monday.strftime("%Y.%m.%d")
    return title


# Gets the track ids in this weeks regular Discover Weekly Playlist
def get_track_ids(tracks):
    track_ids=[]
    songList = open(get_playlist_title() + '.txt', "w")
    for i, item in enumerate(tracks['items']):
        track = item['track']
        track_ids.append(track['id'])
        print("   %d %32.32s %s" % (i, track['artists'][0]['name'], # Print the songs added in console
            track['name']))
        songList.write("   %d %32.32s %s\n" % (i, track['artists'][0]['name'], track['name']))
    songList.close()
    return track_ids

# Get the playlist id of the regular Discover Weekly playlist
def add_new_songs(username,sp,playlist_id):
    results = sp.user_playlist('spotify','')
    tracks = results['tracks']
    track_ids = get_track_ids(tracks)
    sp.user_playlist_add_tracks(username,playlist_id,track_ids)

def main():
    if len(sys.argv) > 1:
        username = sys.argv[1]
    else:
        print("Usage: %s username --createPlaylist" % (sys.argv[0],))
        sys.exit()

    # Authorisation token
    token = util.prompt_for_user_token(username, scope, client_id='',
                                       client_secret='',
                                       redirect_uri='http://moustafa.io')

    # Once token is okay, check if playlist exists already, create if neccessary and add songs
    if token and (len(sys.argv) == 3):
        sp = spotipy.Spotify(auth=token)
        create_playlist(username, sp)
        add_new_songs('spotify', sp, get_playlist_id(username,sp))
        print('Created new playlist and added this weeks Discover Weekly Songs')
    elif token and (len(sys.argv) == 2):
        sp = spotipy.Spotify(auth=token)
        results = sp.user_playlist('spotify','')
        tracks = results['tracks']
        track_ids = get_track_ids(tracks)
        print('Created file with this weeks Discover Weekly Songs')
    else:
        print("Can't get token for", username)

main()
