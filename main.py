from pytube import YouTube
f = open("links2.txt","r")
mas = f.read().split("\n")
for link in mas:
    print(link)
    myStream = YouTube(link).streams.first()
    myStream.download()