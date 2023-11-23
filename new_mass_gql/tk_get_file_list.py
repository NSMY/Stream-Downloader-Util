# Global variable to hold the selected items
import json
import os
import sys
import tkinter as tk
from pathlib import Path
from tkinter import ttk

from utility_dir import util_functions

# from ..utility_dir import util_functions



""" # to make the file work as a stand alone
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from utility_dir import util_functions
"""
selected_items = []
# [] Super Twitch ONLY
def create_popup1(windowName, columns, data):
    global selected_items
    popup = tk.Tk()
    popup.overrideredirect(False)
    popup.title(windowName)
    style = ttk.Style()

    style.configure("Treeview", background="#0b0b13", foreground="white")
    tree = ttk.Treeview(popup, style="Treeview")
    popup.configure(
        bg="#0b0b13",
        border=10,
    )

    label = tk.Label(
        popup,
        text=(
            "Selection/s made by clicking on a Vod/s with Mouse\nUse 'CLOSE' "
            "(Bottom Right) Button to make selection Dont use (Windows)X"
        ),
        bg="#0b0a0d",
        fg="white",
        highlightcolor="white",
        justify="left",
        highlightbackground='#853a3a',
        highlightthickness=1,
        padx=5,

    )
    label.grid(row=2, column=1, sticky='s')

    # Calculate the maximum length of the content
    # max_length = max(len(value) for value in data)

    tree = ttk.Treeview(
        popup,
        columns=columns,
        show='headings',
        height=17,
        selectmode='browse',
        padding=1,
        takefocus=2
    )
    tree.grid(row=1, column=1, sticky='nsew')

    vsb = ttk.Scrollbar(popup, orient="vertical", command=tree.yview)
    vsb.grid(row=1, column=2, sticky='nse')
    tree.configure(yscrollcommand=vsb.set)

    for col in columns:
        tree.heading(col, text=col)
        if col == 'index':
            tree.column(col, width=20, stretch=tk.NO)
        elif col == 'id':
            tree.column(col, width=75, stretch=tk.YES, anchor='center')
        elif col == 'downloaded':
            tree.column(col, width=55, stretch=tk.YES, anchor='center')
        elif col == 'publishedAt':
            tree.column(col, width=140, stretch=tk.YES, anchor='center')
        elif col == 'broadcastType':
            tree.column(col, width=75, stretch=tk.NO)
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
        popup,
        text=(f'Vods List for : {windowName.split('.')[0].title()}'),
        bg="#0b0a0d",
        fg="#296d8f",
        highlightcolor="red",
        justify="center",
        font="calabri",
        relief='groove',
        state='disabled',
        disabledforeground='white',
        activebackground='red',
        pady=5,
        padx=4,
    )
    label2.grid(row=0, column=1, sticky='nw')

    tree.bind("<ButtonRelease-1>", get_selection)

    button1 = tk.Button(
        popup,
        text="Make Selection-Close",
        command=lambda: popup.quit(),
        height=2,
        width=17,
        highlightcolor='yellow',
        background='#296d8f',
        foreground='white',
        activebackground='#ff004c',
        activeforeground='white',
        underline=5,
        relief="groove",
        overrelief='ridge',
        pady=1
    )
    button1.grid(row=2, column=1, sticky='se')

    button3 = tk.Button(
        popup,
        text="Open Folder",
        underline=5,
        justify='center',
        relief='flat',
        overrelief='raised',
        command=lambda: os.startfile(os.path.dirname(file)),  # NOTE gets link from File arg.
        height=1,
        width=9,
        highlightcolor='red',
        background='#125c81',
        foreground='white',
        activebackground='#1b582b',
        activeforeground='white'
    )
    button3.grid(row=2, column=1, sticky='sw')

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


def call_tk_vod_view(file_path):
    winName = os.path.basename(file_path)
    with open(file_path, 'r') as f:
        jsond = json.load(f)

    list1 = []
    for index, items in enumerate(jsond):
        vods_desc = (index, items['downloaded'], items['broadcastType'], items['publishedAt'], items['id'], items['gameName'], items['title'])
        list1.append(f'{vods_desc}')


# Define the column names as 'index' and specific keys from the JSON data
    columns = ['index', 'downloaded', 'id', 'broadcastType', 'publishedAt', 'gameName', 'title']  # replace 'key1', 'key2' with your specific keys
# Define the data as the index and values of the specific keys in the JSON data
    data = [[index] + [util_functions.simple_convert_timestamp(item[key]) if key == 'publishedAt' else item[key] for key in columns[1:]] for index, item in enumerate(jsond)]
# Call the function
    try:
        create_popup1(winName, columns, data)
    except tk.TclError as e:
        print(f'Error Closed Window using (X), Terminated early: {e}')
        create_popup1(winName, columns, data)

    listIndexs = [index[0] for index in selected_items]
    for index in listIndexs:
        print(jsond[int(index)].get('title'))
        print(jsond[int(index)].get('publishedAt'), '\n')
    return selected_items

# file = "C:\\Users\\970EVO-Gamer\\AppData\\Local\\Stream-Downloader-Util\\jsons\\sequisha.json"
if __name__ == '__main__':
    call_tk_vod_view(file_path)

# input('exit ................')
