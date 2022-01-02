import urllib.request
import os
# urlから動画を保存する
def saveMovie(url, filePath):
    try:
        data = urllib.request.urlopen(url).read()
        with open(filePath, mode="wb") as f:
            f.write(data)
        return True
    except:
        return False

# ディレクトリ内に同一のファイルが存在するか
def getIsSameNamefile(filePath):
    return os.path.exists(filePath)

# Downloadsディレクトリを取得する
def getDownloadsPath():
    return os.path.join(os.path.join(os.environ['USERPROFILE']), 'Downloads')

