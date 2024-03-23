from pytube import YouTube
f = open("links.txt","r")
mas = f.read().split("\n")
for link in mas:
    myStream = YouTube(link).streams.first()
    myStream.download()
    