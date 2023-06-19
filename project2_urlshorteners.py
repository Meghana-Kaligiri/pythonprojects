import pyshorteners
url=input("enter the url:")
def shortenural(url):
    s=pyshorteners.Shortener()
    #Shorteners predefined
    print(s.tinyurl.short(url))
    #tinyurl --- site name
    #short----to short url
shortenural(url)
#shorts the big url into small url and that url gives complete info...
#if u have large url with long descriptions it shorts
