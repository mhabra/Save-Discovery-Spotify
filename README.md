# Save Your Discovery
## A helpful Python tool
---

### Got a lot of code from @bobbymcgonigle/spotify-always-discover-weekly

## Intro

I always hated that my discover weekly would disappear. And the solutions I found weren't ideal. This program saves the content of your discover weekly into a text file, and optionally into a playlist titled: 'DW of [Date of Discover Weekly]'. The date portion of the title will be the date of that Monday in which the Discover Weekly playlist was created, with the format YYYY.MM.DD .

## Requirements
The program uses spotipy so make sure you:

`pip3 install spotipy`

It also uses the Spotify web API, so create an account, then create a project, and make note of your client ID, and client secret.

## Usage

Before running the script, put your client ID, client secret, redirect URI, and your Discover Weekly playlist ID in the fields provides in `save-your-discovery.py`. Also follow all on-screen instructions that spotipy might tell you to do.

Usage is:

`python3 save-your-discovery.py [USERNAME] [--createPlaylist]`

The createPlaylist flag can be shortened to `-c`, and will create a playlist in your library of that week's discover weekly.

### Example

`python3 save-your-discovery.py moustafa -c`


## Known Bugs

If you run the program with a playlist that has the same name of the playlist that will be created, it will create an empty playlist with the name, and add all the songs of your discover weekly to the original playlist that existed, before.

Honestly, I'm thinking of rewriting it from the ground-up to be cleaner and have more features.