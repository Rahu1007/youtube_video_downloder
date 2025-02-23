import pytube
link = input("enter youtube video link")
yt = pytube.YouTube(link)
yt.streams.first().download()
print("download",link)