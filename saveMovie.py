import urllib.request
def saveMovie(url, movieName = "nonTitle.mp4"):
    data = urllib.request.urlopen(url).read()
    with open(movieName, mode="wb") as f:
        f.write(data)

