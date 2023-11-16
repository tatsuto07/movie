import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

def on_mousewheel(event):
    canvas.yview_scroll(-1 * (event.delta // 120), "units")

def display_movie_info(movie_name, movie_description, image_file):
    window.withdraw()
    info_window = tk.Toplevel()
    info_window.attributes('-fullscreen', True)
    info_window.title(movie_name)
    
    def close_info_window():
        info_window.destroy()
        window.deiconify()

    image = Image.open(image_file)
    image.thumbnail((600, 600))
    photo = ImageTk.PhotoImage(image)
    image_label = tk.Label(info_window, image=photo)
    image_label.photo = photo
    image_label.grid(row=0, column=1, padx=20)

    description_label = tk.Label(info_window, text=movie_description, wraplength=400, anchor="w", font=("Yu Gothic", 20, "bold"))
    description_label.grid(row=0, column=0, padx=20, pady=20)

    close_button = tk.Button(info_window, text="一覧へ戻る", command=close_info_window, font=("Yu Gothic", 15))
    close_button.grid(row=1, column=0, columnspan=2)

def get_release_date(movie_data):
    description = movie_data["説明"]
    release_date = description.split("公開日: ")[1].split("\n")[0]
    return release_date

def sort_movies():
    sort_option = sort_var.get()

    if sort_option == "名前昇順":
        movies_data.sort(key=lambda x: x["名前"])
    elif sort_option == "名前降順":
        movies_data.sort(key=lambda x: x["名前"], reverse=True)
    elif sort_option == "公開日昇順":
        movies_data.sort(key=lambda x: get_release_date(x))
    elif sort_option == "公開日降順":
        movies_data.sort(key=lambda x: get_release_date(x), reverse=True)    

    update_movie_list(search_var.get())

def update_movie_list(search_query=""):
    for widget in frame.winfo_children():
        widget.destroy()

    displayed_movies = [movie for movie in movies_data if search_query == "" or search_query in movie["名前"]]
    for index, movie_data in enumerate(displayed_movies):
        name = movie_data["名前"]
        image_file = movie_data["画像ファイル"]
        description = movie_data["説明"]

        image = Image.open(image_file)
        image.thumbnail((370, 370))
        photo = ImageTk.PhotoImage(image)
        image_label = tk.Label(frame, image=photo)
        image_label.photo = photo
        image_label.grid(row=index // num_columns * 3, column=index % num_columns, padx=(10, 10))
        name_label = tk.Label(frame, text=name, font=("Yu Gothic", 12, "bold"))
        name_label.grid(row=index // num_columns * 3 + 1, column=index % num_columns, padx=(10, 10))
        space_label = tk.Label(frame, text="", height=1)
        space_label.grid(row=index // num_columns * 3 + 2, column=0, columnspan=num_columns * 2)

        image_label.bind("<Button-1>", lambda e, name=name, desc=description, image=image_file: display_movie_info(name, desc, image))

def search_movies():
    search_query = search_var.get()
    update_movie_list(search_query)

def clear_search():
    search_var.set("")  
    update_movie_list("")  

window = tk.Tk()
window.title("映画")
window.attributes('-fullscreen', True)

canvas = tk.Canvas(window)
frame = tk.Frame(canvas)
vsb = tk.Scrollbar(window, orient="vertical", command=canvas.yview)
canvas.configure(yscrollcommand=vsb.set)

canvas.pack(side="left", fill="both", expand=True)
vsb.pack(side="right", fill="y")

canvas.create_window((4, 4), window=frame, anchor="nw")

window.bind_all("<MouseWheel>", on_mousewheel)

movies_data = [
    {"名前": "ショーシャンクの空に", 
     "画像ファイル": "./img/ショーシャンクの空に.jpg", 
     "説明": "「ショーシャンクの空に」\n\n 公開日: 1995年6月3日 \n 監督: フランク・ダラボン"},

    {"名前": "ワイルドスピード", 
     "画像ファイル": "./img/ワイルドスピード.jpg",
     "説明":"「ワイルドスピード」\n\n 公開日: 2001年10月20日 \n 監督: ロブ・コーエン"},

    {"名前": "ジュラシック・パーク", 
     "画像ファイル": "./img/ジュラシック・パーク.jpg",
     "説明":"「ジュラシック・パーク」\n\n 公開日: 1993年7月17日 \n 監督: スティーブン・スピルバーグ"},

    {"名前": "スタンド・バイ・ミー", 
     "画像ファイル": "./img/スタンド・バイ・ミー.jpg",
     "説明":"「スタンド・バイ・ミー」\n\n 公開日: 1987年4月18日 \n 監督: ロブ・ライナー"},

    {"名前": "ファイト・クラブ", 
     "画像ファイル": "./img/ファイト・クラブ.jpg",
     "説明":"「ファイト・クラブ」\n\n 公開日: 1999年12月11日 \n 監督: デビッド・フィンチャー"},

    {"名前": "トランスポーター", 
     "画像ファイル": "./img/トランスポーター.jpg",
     "説明":"「トランスポーター」\n\n 公開日: 2003年2月1日 \n 監督: ルイ・レテリエ"},

    {"名前": "ジョン・ウィック", 
     "画像ファイル": "./img/ジョン・ウィック.jpg",
     "説明":"「ジョン・ウィック」\n\n 公開日: 2015年10月16日 \n 監督: チャド・スタエルスキ"},

    {"名前": "タイタニック", 
     "画像ファイル": "./img/タイタニック.jpg",
     "説明":"「タイタニック」\n\n 公開日: 1997年12月20日 \n 監督: ジェームズ・キャメロン"},

    {"名前": "グリーンブック", 
     "画像ファイル": "./img/グリーンブック.jpg",
     "説明":"「グリーンブック」\n\n 公開日: 2019年3月1日 \n 監督: ピーター・ファレリー"},

    {"名前": "フォレスト・ガンプ", 
     "画像ファイル": "./img/フォレスト・ガンプ.jpg",
     "説明":"「フォレスト・ガンプ」\n\n 公開日: 1995年3月11日 \n 監督: ロバート・ゼメキス"},
    
    {"名前": "最強のふたり", 
     "画像ファイル": "./img/最強のふたり.jpg",
     "説明":"「最強のふたり」\n\n 公開日: 2012年9月1日 \n 監督: エリック・トレダノ オリビエ・ナカシュ"},

    {"名前": "セッション", 
     "画像ファイル": "./img/セッション.jpg",
     "説明":"「セッション」\n\n 公開日: 2015年4月17日 \n 監督: デイミアン・チャゼル"},

    {"名前": "グランド・イリュージョン", 
     "画像ファイル": "./img/グランド・イリュージョン.jpg",
     "説明":"「グランド・イリュージョン」\n\n 公開日: 2013年10月25日 \n 監督: ルイ・レテリエ"},

    {"名前": "アイ・アム・レジェンド", 
     "画像ファイル": "./img/アイ・アム・レジェンド.jpg",
     "説明":"「アイ・アム・レジェンド」\n\n 公開日: 2007年12月14日 \n 監督: フランシス・ローレンス"},

    # {"名前": "", 
    #  "画像ファイル": "./img/.jpg",
    #  "説明":"「」\n\n 公開日:  \n 監督: "},

]

num_columns = 4

search_var = tk.StringVar()
search_var.trace_add("write", lambda *args: search_movies())
search_label = tk.Label(window, text="映画を検索:")
search_label.pack(side="top", pady=5)
search_entry = ttk.Entry(window, textvariable=search_var)
search_entry.pack(side="top")

clear_button = tk.Button(window, text="検索をクリア", command=clear_search, font=("Yu Gothic", 10, "bold"))
clear_button.pack(side="top", pady=5)


sort_var = tk.StringVar()
sort_var.set("")
sort_label = tk.Label(window, text="ソート:")
sort_label.pack(side="top", pady=5)
sort_menu = ttk.Combobox(window, textvariable=sort_var, values=["名前昇順", "名前降順", "公開日昇順", "公開日降順"], height=5, state="readonly")
sort_menu.pack(side="top")
sort_menu.bind("<<ComboboxSelected>>", lambda e: sort_movies())

update_movie_list()

frame.update_idletasks()

canvas.config(scrollregion=canvas.bbox("all"))

close_button = tk.Button(window, text="閉じる", command=window.destroy, font=("Yu Gothic", 15, "bold"))
close_button.pack(side="bottom")

window.mainloop()