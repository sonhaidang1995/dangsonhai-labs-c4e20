from youtube_dl import YoutubeDL
# Sample 1: Download a single youtube video
dl = YoutubeDL()
dl.download(["https://www.youtube.com/watch?v=CJYYsEFB2eU"])

# Sample 2: Download multiple youtube videos
dl = YoutubeDL()
dl.download(["https://www.youtube.com/watch?v=2Vv-BfVoq4g","https://www.youtube.com/watch?v=nSDgHBxUbVQ","https://www.youtube.com/watch?v=lp-EO5I60KA"])

# Sample 3: Download audio
audio = {
    'format':"bestaudio/audio"
}
dl = YoutubeDL(audio)
dl.download(["https://www.youtube.com/watch?v=ShZ978fBl6Y"])

# Sample 4: Search and download the first video
search = {
    'default_search':'ytsearch',
    'max_download': 1
}
dl = YoutubeDL(search)
dl.download(['Hà Nội Của Bố'])
# Sample 5: 
search = {
    'format':'bestaudio/audio',
    'default_search':'ytsearch',
    'max_download': 1
}
dl = YoutubeDL(search)
dl.download(['Ba Kể c0n nghe'])