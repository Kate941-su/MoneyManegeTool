import Scraping
import saveMovie
import sys
import tkinter
from tkinter import messagebox
from tkinter import filedialog
from tkinter import ttk
root = tkinter.Tk()
root.title(u"ストーリーほぞんあぷり")
root.geometry("400x120")
LABEL_POS = 5
TEXTBOX_POS = 200
BASE_VERTICAL_POS = 10
VERTICAL_SPACE = 20

# ボタンが押されるとここが呼び出される
def DeleteEntryValue(event):
    scraping = Scraping.Scraping()
    url = urlBox.get()
    userName = userNameBox.get()
    password = passwordBox.get()
    if (url == "" or password == "" or userName == "") :
        messagebox.showerror("エラー", "すべての項目を入力してください")
        return
    scraping.getUrl(url)
    scraping.getUserName(userName)
    scraping.getPassWord(password)
    filePath = filedialog.asksaveasfilename(initialdir = saveMovie.getDownloadsPath(), title = "Save as", defaultextension = "mp4")
    if (filePath == ""):
        return
    if(scraping.getMovie(url, filePath) == False):
        messagebox.showerror("エラー", "動画を作成できませんでした\nヒント：ストーリーは静止画では保存できません")
    else:
        urlBox.delete(0, tkinter.END)
        messagebox.showinfo("メッセージ", "動画作成を終了しました")

#エントリー
urlLabel = tkinter.Label(text = "ストーリーのURLを貼り付けてください")
urlLabel.place(x = LABEL_POS, y = BASE_VERTICAL_POS)
urlBox = tkinter.Entry(width = 30)
urlBox.place(x = TEXTBOX_POS, y = BASE_VERTICAL_POS)

userNameLabel = tkinter.Label(text = "ユーザー名を入力してください")
userNameLabel.place(x = LABEL_POS, y = BASE_VERTICAL_POS + VERTICAL_SPACE)
userNameBox = tkinter.Entry(width = 30)
userNameBox.place(x = TEXTBOX_POS, y = BASE_VERTICAL_POS + VERTICAL_SPACE)

passwordLabel = tkinter.Label(text = "パスワードを入力してください")
passwordLabel.place(x = LABEL_POS, y = 50)
passwordBox = tkinter.Entry(show = "*", width = 30)
passwordBox.place(x = TEXTBOX_POS, y = BASE_VERTICAL_POS + VERTICAL_SPACE * 2)

#ボタン
Button = tkinter.Button(text=u'動画作成', width=25)
Button.bind("<Button-1>",DeleteEntryValue)
Button.place(x=105, y=80)
root.mainloop()

#Scraping.getMovie()