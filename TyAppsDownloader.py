import urllib.request as ur
import tkinter as tk
import os

Version = 1.0

dlurl_tal = "https://github.com/BakedTaiyaki093/TyAppsLauncher/raw/refs/heads/main/releases/TyAppsLauncher.zip"
dlurl_tdl = ""

# テキストファイルからフォルダパスを取得
with open("dirct.txt", "r", encoding="utf_8") as file:
    dlfolder = file.readline().strip()

# フォルダが存在しない場合は処理をスキップ
if not os.path.exists(dlfolder):
    print(f"エラー: 指定されたフォルダが存在しません → {dlfolder}")
else:
    # ダウンロード先のファイルパスを設定
    download_path = os.path.join(dlfolder, "TyAppsdownload.zip")

    # ダウンロード処理（ボタンを押したときに実行）
    def dltal_f():
        ur.urlretrieve(dlurl_tal, download_path)
        print(f"ダウンロード完了: {download_path}")

    # GUI
    root = tk.Tk()
    root.title(f"TyAppsDownloader@V{Version}")
    root.geometry("400x850")

    btn_tal = tk.Button(root, text="TyAppsLauncher", command=dltal_f)
    btn_tal.place(relx=0.13, rely=0.1, anchor=tk.CENTER)

    root.mainloop()