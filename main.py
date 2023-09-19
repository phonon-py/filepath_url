import tkinter as tk
import pyperclip


# 追加で必要なライブラリはpyperclipのみ
def URL_Convert():
    before_text = before_entry.get("1.0",'end-1c')
    # ファイルパスの変換処理を実装
    URL = before_text.strip().replace("\\", "/").lstrip("file:/").strip('"')
    after_URL = "https:" + URL
    after_entry.delete("1.0", tk.END)
    after_entry.insert(tk.END, after_URL)
    pyperclip.copy(after_URL)  # クリップボードにコピー

app = tk.Tk()
app.title("ファイルパス to URL変換")

# ラベルとテキストエリアの作成
tk.Label(app, text="ファイルパス").pack()
before_entry = tk.Text(app, height=4, width=50)
before_entry.pack()

# 変換ボタンの作成
convert_button = tk.Button(app, text="変換", command=URL_Convert)
convert_button.pack()

# 結果の表示エリア
tk.Label(app, text="変換後URL").pack()
after_entry = tk.Text(app, height=4, width=50)
after_entry.pack()

# クリップボードにコピーするボタン
copy_button = tk.Button(app, text="クリップボードにコピー", command=lambda: pyperclip.copy(after_entry.get("1.0",'end-1c')))
copy_button.pack()

# メインループの開始
app.mainloop()
