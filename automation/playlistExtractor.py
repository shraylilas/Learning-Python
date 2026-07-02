import requests

## I realised that my music taste is a bit hard to discern when there are, at the time of coding this, 298 songs in my YouTube playlist.
## So, let's try and print the titles of all the songs in the playlist and number the amount of videos.
## Of course, this applies to any youtube playlist, so you could do this for anything else.

videos = [] ## Our list of videos

api_key = input("Enter API key ") ## I'm not sure how to do this without compromising my API key, so I just made this part an input instead
playlist = input("Enter playlist id ")

url = f"https://www.googleapis.com/youtube/v3/playlistItems?playlistId={playlist}&part=snippet&maxResults=50&key={api_key}" ## 1st API request

response = requests.get(url)
data = response.json()

while True:
    items = data.get("items", [])

    for x in range(len(items)):
        videos.append(items[x]["snippet"]["title"])

    if "nextPageToken" not in data:
        break
## Subsequent API requests
    url = f"https://www.googleapis.com/youtube/v3/playlistItems?playlistId={playlist}&part=snippet&maxResults=50&pageToken={data['nextPageToken']}&key={api_key}"

    response = requests.get(url)
    data = response.json()

print(videos)
print(len(videos))