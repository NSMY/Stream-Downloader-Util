# Global variable to hold the selected items
import json
import os
import sys
import threading
import tkinter as tk
from concurrent.futures import thread
from pathlib import Path
from tkinter import ttk

from utility_dir import util_functions

# from ..utility_dir import util_functions





#  # to make the file work as a stand alone
# sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
# from utility_dir import util_functions

# json_dir = f'{util_functions.get_appdata_dir()}/jsons'

# FEATURE Make a Class ????.

selected_items = []
# [] Super Twitch ONLY
def create_popup1(windowName, columns, data):
    global selected_items
    popup = tk.Tk()
    popup.overrideredirect(False)
    popup.title(windowName)
    style = ttk.Style(popup)
    style.theme_use("clam")
    style.configure("Treeview", background="#0b0a0d", fieldbackground="#0b0a0d", foreground="white")

    # style.configure("Treeview", background="#0b0b13", foreground="white")
    tree = ttk.Treeview(popup, style="Treeview")
    popup.configure(
        bg="#0b0b13",
        highlightbackground="#296D8F",
        highlightcolor='#0b0b13',
        highlightthickness=5
    )
    frame1 = tk.Frame(popup, bg="#0b0a0d",) #borderwidth=3, highlightthickness=1, highlightbackground='yellow')
    frame2 = tk.Frame(popup, bg="#0b0a0d", borderwidth=3) #, highlightthickness=1, highlightbackground='violet')
    frame3 = tk.Frame(popup, bg="#0b0a0d",) #borderwidth=3, highlightthickness=1, highlightbackground='white')
    frame4 = tk.Frame(popup, bg="#0b0a0d", borderwidth=3, highlightbackground='yellow', relief="raised")

    label = tk.Label(
        frame2,
        text=(
            "Selection/s made by clicking on a Vod/s with Mouse\nUse 'CLOSE' "
            "(Bottom Right) Button to make selection Dont use (Windows)X"
        ),
        bg="#0b0a0d",
        fg="white",
        font=("Calibri", 10, "bold"),
        highlightcolor="white",
        justify="left",
        # highlightbackground='#853a3a',
        # highlightthickness=1,
        relief='sunken',
        borderwidth=3,
        padx=5,
        pady=2,
        state="active",
        activebackground="silver"

    )
    # label.grid(row=2, column=1, sticky='n', pady=5)

    # Calculate the maximum length of the content
    # max_length = max(len(value) for value in data)

    tree = ttk.Treeview(
        frame1,
        columns=columns,
        show='headings',
        height=(len(data) if len(data) < 17 else 17),
        selectmode='browse',
        takefocus=2
    )
    # tree.grid(row=1, column=1, sticky='nsew')

    vsb = ttk.Scrollbar(frame3, orient="vertical", command=tree.yview, style='')
    # vsb.grid(row=1, column=2, sticky='nsw')
    tree.configure(yscrollcommand=vsb.set)

    for col in columns:
        tree.heading(col, text=col)
        if col == 'index':
            tree.column(col, width=20, stretch=tk.NO, anchor="w")
        elif col == 'id':
            tree.column(col, width=75, stretch=tk.YES, anchor='center')
        elif col == 'downloaded':
            tree.column(col, width=55, stretch=tk.YES, anchor='center')
        elif col == 'publishedAt':
            tree.column(col, width=140, stretch=tk.YES, anchor='center')
        elif col == 'status':
            tree.column(col, width=80, stretch=tk.YES, anchor='center')
        elif col == 'broadcastType':
            tree.column(col, width=75, stretch=tk.NO, anchor='center')
        elif col == 'gameName':
            tree.column(col, minwidth=90, stretch=tk.YES)
        elif col == 'title':
            tree.column(col, minwidth=200, width=500, stretch=tk.YES, anchor="w")
        else:
            tree.column(col, width=100, stretch=tk.YES)

    for item in data:
        tree.insert('', 'end', values=item)

    def get_selection(event):
        global selected_items
        clicked_index = tree.focus()
        clicked_item = tree.item(clicked_index)['values']
        if clicked_item in selected_items:
            selected_items.remove(clicked_item)
        else:
            selected_items.append(clicked_item)

    label2 = tk.Label(
        frame4,
        text=(f'Vods List for : {windowName.split('.')[0].title()}'),
        bg="#0b0a0d",
        # fg="#296d8f",
        # highlightcolor="red",
        justify="center",
        font=("calabri", 12, "bold"),
        relief='raised',
        highlightbackground='#096597',
        # highlightthickness=16,
        border=3,
        state='disabled',
        disabledforeground='#BBD5F0',
        activebackground='red',
        pady=5,
        padx=4,
    )
    # label2.grid(row=1, rowspan=3, column=3, padx=5, pady=5)

    tree.bind("<ButtonRelease-1>", get_selection)

    button1 = tk.Button(
        frame4,
        text="Make Selection-Close",
        command=lambda: popup.quit(),
        height=2,
        width=17,
        font=("calabri", 10, "bold", "italic"),
        highlightcolor='yellow',
        background='#296d8f',
        foreground='white',
        activebackground='#ff004c',
        activeforeground='white',
        underline=5,
        relief="groove",
        overrelief='ridge',
        pady=7
    )
    # button1.grid(row=1, rowspan=3, column=3, padx=5, pady=5)

    button3 = tk.Button(
        frame4,
        text="Open Folder",
        underline=5,
        justify='center',
        font=("Calabri", 8),
        relief='flat',
        overrelief='raised',
        command=lambda: os.startfile(json_dir),  # NOTE gets link from File arg.
        height=1,
        width=9,
        highlightcolor='red',
        background='#125c81',
        foreground='white',
        activebackground='#1b582b',
        activeforeground='white',
        pady=3
    )
    # button3.grid(row=1, rowspan=3, column=3, padx=5, pady=5)

    frame1.grid(row=1, column=1, sticky="nsew")
    tree.pack(side='left', fill='both', anchor='ne', expand=True)
    vsb.pack(side="left", fill="y", anchor='nw', expand=True, padx=2)

    frame2.grid(row=2, column=1, sticky="nsew")
    label.pack(side="right")

    frame3.grid(row=1, column=2, sticky="nsew")

    frame4.grid(row=1, column=3, sticky="nsew")

    label2.pack(side="top", fill="x", padx=5, pady=5)
    button1.pack(side="bottom", fill="x", padx=5, pady=5 )
    button3.pack(side="bottom", fill="x", padx=5, pady=5 )

    popup.grid_columnconfigure(1, weight=1)
    popup.grid_rowconfigure(1, weight=1)

    popup.update_idletasks()

    width = popup.winfo_width()
    height = popup.winfo_height()

    width += 5
    height += 5

    popup.geometry(f"{width}x{height}")
    popup.mainloop()
    popup.destroy()


def process_data(input_data, windName):
    # Define the column names as 'index' and specific keys from the JSON data
    columns = ['index', 'downloaded', 'id', 'broadcastType', 'status', 'publishedAt', 'gameName', 'title']  # replace 'key1', 'key2' with your specific keys
    # Define the data as the index and values of the specific keys in the JSON data
    data = [[index] + [util_functions.simple_convert_timestamp(item[key]) if key == 'publishedAt' else item[key] for key in columns[1:]] for index, item in enumerate(input_data)]
    # Call the function
    try:
        create_popup1(windName, columns, data)
    except tk.TclError as e:
        print(f'Error Closed Window using (X), Terminated early: {e}')
        create_popup1(windName, columns, data)

    listIndexs = [index[0] for index in selected_items]
    for index in listIndexs:
        print(input_data[int(index)].get('title'))
        print(input_data[int(index)].get('publishedAt'), '\n')
    return selected_items


def call_tk_file(file_path):
    windName = os.path.basename(file_path)
    with open(file_path, 'r') as f:
        jsond = json.load(f)
    return process_data(jsond, windName)
    # list1 = []
    # for index, items in enumerate(jsond):
    #     vods_desc = (index, items['downloaded'], items['broadcastType'], items['publishedAt'], items['id'], items['gameName'], items['title'])
    #     list1.append(f'{vods_desc}')


def call_tk_data(data):
    # windName = os.path.basename(data)
    # print(data)
    windName = data[0].get('displayName')
    t1 = threading.Thread(target=process_data, args=(data, windName)) 
    t1.start()
    return

# TODOmake another button that sets as downloaded.

# file = "C:\\Users\\970EVO-Gamer\\AppData\\Local\\Stream-Downloader-Util\\jsons\\deadlyslob.json"
# call_tk_file(file)
# if __name__ == '__main__':
#     call_tk_vod_view(file_path)

# input('exit ................')
