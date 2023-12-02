# Global variable to hold the selected items
import json
import os
import sys
import threading
import tkinter as tk
from concurrent.futures import thread
from pathlib import Path
from tkinter import IntVar, Radiobutton, Toplevel, messagebox, ttk

# # from ..utility_dir import util_functions
import spinner
from utility_dir import util_functions

# from numpy import append


# # to make the file work as a stand alone
# sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
# import spinner
# from utility_dir import util_functions

# json_dir = f'{util_functions.get_appdata_dir()}/jsons'

# FEATURE Make a Class ????.


selected_items = []
# [] Super Twitch ONLY
def create_popup1(windowName, columns, processed_data, rawdata, file_path):
    global selected_items
    popup = tk.Tk()
    popup.overrideredirect(False)
    popup.title(windowName)
    popup.minsize(1350,500)
    style = ttk.Style(popup)
    style.theme_use("clam")
    style.configure("Treeview", background="#0b0a0d", fieldbackground="#0b0a0d", foreground="white")

    # style.configure("Treeview", background="#0b0b13", foreground="white")
    tree = ttk.Treeview(popup, style="Treeview")
    popup.configure(
        bg="#0b0b13",
        highlightbackground="#296D8F",
        highlightcolor='#0b0b13',
        highlightthickness=5,
        height=min(len(processed_data), 17)
    )
    frame1 = tk.Frame(popup, bg="#0b0a0d",) #borderwidth=3, highlightthickness=1, highlightbackground='yellow')
    frame2 = tk.Frame(popup, bg="#0b0a0d", borderwidth=3) #, highlightthickness=1, highlightbackground='violet')
    frame3 = tk.Frame(popup, bg="#0b0a0d",) #borderwidth=3, highlightthickness=1, highlightbackground='white')
    frame4 = tk.Frame(popup, bg="#0b0a0d", borderwidth=3, highlightbackground='yellow', relief="raised")
    frame2_subframe = tk.Frame(frame2, relief="sunken")

    explainer_lable = tk.Label(
        frame2,
        text=(
            "Selection/s made by clicking on a Vod/s with Mouse (Multi Hold Shift)\n"
            "Use 'Make Selection-Close' (Right) Button to make selection Dont use (Windows)X"
        ),
        bg="#0b0a0d",
        fg="white",
        font=("Calibri", 10, "bold"),
        highlightcolor="white",
        justify="left",
        relief='sunken',
        borderwidth=3,
        padx=5,
        pady=2,
        state="active",
        activebackground="silver",

    )

# -----------------------------------------------------------------------------------

    tree = ttk.Treeview(
        frame1,
        columns=columns,
        show='headings',
        height=min(len(processed_data), 17)
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
            tree.column(col, width=75, stretch=tk.YES, anchor='center')
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

    for item in processed_data:
        tree.insert('', 'end', values=item)
# -----------------------------------------------------------------------------------


    title_lable = tk.Label(
        frame4,
        text=(f'Vods List for : {windowName.split('.')[0].title()}'),
        bg="#0b0a0d",
        # fg="#296d8f",
        # highlightcolor="red",
        justify="center",
        font=("Arial", 14),
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


    # def get_selection(event):
    #     global selected_items
    #     clicked_index = tree.focus()
    #     clicked_item = tree.item(clicked_index)['values']
    #     if clicked_item in selected_items:
    #         selected_items.remove(clicked_item)
    #     else:
    #         selected_items.append(clicked_item)

    # tree.bind("<ButtonRelease-1>", get_selection)

    def quit_with_selection():
        if selected_items == []:
            q = messagebox.askyesno(
                title='QUITTING!!',
                message='No Selection has Been Made,\nAre you Sure you want to proceed?'
            )
            if q:
                popup.destroy()
        else:
            popup.destroy()

    make_selec_btn = tk.Button(
        frame4,
        text="Make Selection/Close",
        command=quit_with_selection,
        height=2,
        width=17,
        font=("Calabri", 10, "bold", "italic"),
        highlightcolor='yellow',
        background='#296d8f',
        foreground='white',
        activebackground='#00ff00',
        activeforeground='white',
        underline=5,
        relief="groove",
        overrelief='ridge',
        pady=7,
        cursor="star"
    )


    def delete_item():
        global selected_items
        for i in tree.selection():
            selected_item = tree.item(i)['values']
            if selected_item in selected_items:
                selected_items.remove(selected_item)

        selections_listbox.delete(0, tk.END)
        for items in selected_items:
            selections_listbox.insert(tk.END, f"Title Name: {items[0]}    {items[7]}")
        # print(selected_items)

    delete_btn = tk.Button(
        frame4,
        text="Delete selected Item from list",
        command=delete_item,
        height=1,
        width=13,
        font=("calabri", 9, "bold", "italic"),
        highlightcolor='yellow',
        background='#5e1d1d',
        foreground='white',
        activebackground='#df0000',
        activeforeground='white',
        underline=0,
        relief="groove",
        overrelief='ridge',
        pady=2
    )

    def clear_item():
        selected_items.clear()
        selections_listbox.delete(0, tk.END)

    clear_btn = tk.Button(
        frame4,
        text="Clear Selected List",
        command=clear_item,
        height=1,
        width=13,
        font=("calabri", 8, "bold", "italic"),
        highlightcolor='yellow',
        background='#29292c',
        foreground='#ff7272',
        activebackground='#df0000',
        activeforeground='white',
        underline=0,
        relief="groove",
        overrelief='ridge',
        pady=1,
        cursor="cross"
    )
    # new_win = Toplevel()
    # new_win.title('Set Item Downloaded')

    def set_item_downloaded(rawdata, file_path, selected_resolution):
        question = messagebox.askyesno("Change Item Downloaded Status", f"Set Item/s to '{resolutions[selected_resolution.get()]}' Download status ?")
        if selected_items is []:
            if question is False:
                print("User Closed Window")
        elif question is True:
            # print("User clicked Yes")
            items_selected = []
            for i in selected_items:
                items_selected.append(i[0])
            # print(items_selected, "\n")
            for i in items_selected:
                selected_value = resolutions[selected_resolution.get()]
                rawdata[i]["downloaded"] = False if selected_value == 'False' else selected_value
                # print(json.dumps(rawdata[i], indent=4))

            # Update the data for the Treeview
            data = [[index] + [util_functions.simple_convert_timestamp(item[key]) if key == 'publishedAt' else item[key] for key in columns[1:]] for index, item in enumerate(rawdata)]

            # Clear all existing items in the Treeview
            for item in tree.get_children():
                tree.delete(item)

            # Insert updated data into the Treeview
            for item in data:
                tree.insert('', 'end', values=item)
            with open(file_path, 'w') as f:
                json.dump(rawdata, f, indent=4)
            selected_items.clear()

    set_downloaded_btn = tk.Button(
        frame4,
        text='Set Item/s to "Downloaded"',
        command=lambda: set_item_downloaded(rawdata, file_path, x),
        height=1,
        width=13,
        font=("Arial", 9, "bold"),
        highlightcolor='yellow',
        background='#4d5a8f',
        foreground='white',
        activebackground='#a18542',
        activeforeground='white',
        underline=0,
        relief="groove",
        overrelief='ridge',
        pady=2,
        cursor="exchange"
    )

    selections_listbox = tk.Listbox(frame2_subframe, highlightbackground='#242c53', selectbackground='#0b0a0d', height=4, width=120, justify="left", bg='#0b0a0d', fg='white', activestyle="underline")
    selections_listbox.pack(side="left")

    # tree.bind('<ButtonRelease-1>', delete_item)

    def select_items(_):
        global selected_items

        # print(selected_items)
        for i in tree.selection():
            # print(i)
            # print(tree.item(i)['values'])
            selected_item = tree.item(i)['values']
            if selected_item in selected_items:
                selected_items.remove(selected_item)
                selected_items.append(selected_item)
            else:
                selected_items.append(selected_item)
            # selected_items.append(tree.item(i)['values'])
        # print(selected_items, "\n")
        selections_listbox.delete(0, tk.END)
        for items in selected_items:
            selections_listbox.insert(tk.END, f"Title Name: {items[0]}    {items[7]}")

    tree.bind('<<TreeviewSelect>>', select_items)


    open_appdata_btn = tk.Button(
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

    list_name_label = tk.Label(frame2, text="Selection List", font=('Arial', 10, "bold"), bg='#1d1515', fg="White", padx=2, highlightbackground="#737373", highlightthickness=2)
    explainer_lable.pack(side="right", anchor="e", fill="y")
    list_name_label.pack(anchor="nw", pady=1)

    def on_close():
        # Put your cleanup code here
        print("Window is closing")
        close_conf = messagebox.askyesno(title="CLOSE?", message="Close Window?")
        if close_conf:
            popup.destroy()

    # Change the behavior of the close button
    popup.protocol("WM_DELETE_WINDOW", on_close)
# -----------------------------------------------------------------------------------

    frame2_subframe.pack(side="left", expand=False, fill="both")
    # frame2_subframe.grid()

    frame1.grid(row=1, column=1, sticky="nsew")
    tree.pack(side='left', fill='both', anchor='ne', expand=True)
    vsb.pack(side="left", fill="y", anchor='nw', expand=True, padx=2)

    frame2.grid(row=2, column=1, sticky="nsew")

    frame3.grid(row=1, column=2, sticky="nsew")

    frame4.grid(row=1, column=3, sticky="nsew", rowspan=2)

# -----------------------------------------------------------------------------------
    open_appdata_btn.pack(side="top", fill="both", padx=5, pady=2)

    title_lable.pack(side="top", fill="x", padx=5, pady=2)

# -----------------------------------------------------------------------------------
    style = ttk.Style()
    style.configure("Line.TSeparator", background="#44296e")
    sep = ttk.Separator(frame4, orient="horizontal", style='Line.TSeparator')
    sep.pack(side='top', fill='x', padx=10, pady=10, expand=False)
# -----------------------------------------------------------------------------------


    resolutions = ["1080p", "720p", "480p", "360p", "160p", 'False']
    x = IntVar()
    for index in range(len(resolutions)):
        radiobutton = Radiobutton(
            frame4,
            bg='#0b0a0d',
            fg='#8c75ff',
            activebackground="#0b0a0d",
            activeforeground='#00ff95',
            highlightbackground='yellow',
            # selectcolor='aqua',
            anchor='w',
            text=resolutions[index], #adds text to radio buttons
            variable=x, #groups radiobuttons together if they share the same variable
            value=index, #assigns each radiobutton a different value
            padx=1, #adds padding on x-axis
            font=("Impact", 12),
            compound='left', #adds image & text (left-side)
            # style="switch",
        )
        radiobutton.pack(fill="both", anchor='w')

    set_downloaded_btn.pack(side="top", fill="x", padx=1, pady=5)
# -----------------------------------------------------------------------------------
    style = ttk.Style()
    style.configure("Line.TSeparator", background="#44296e")
    sep = ttk.Separator(frame4, orient="horizontal", style='Line.TSeparator')
    sep.pack(side='top', fill='x', padx=10, pady=10, expand=False)
# -----------------------------------------------------------------------------------


    make_selec_btn.pack(side="bottom", fill="x", padx=1, pady=2)


    delete_btn.pack(fill="x", side="bottom", padx=1, pady=2)

    clear_btn.pack(side="bottom", fill="x", padx=1, pady=2)
    



    popup.grid_columnconfigure(1, weight=1)
    popup.grid_rowconfigure(1, weight=1)

    popup.update_idletasks()

    width = popup.winfo_width()
    height = popup.winfo_height()

    # width += 5
    # height += 5

    popup.geometry(f"{width}x{height}")
    popup.mainloop()






def process_data(input_data, windName, file_path)  -> tuple | None:
    # print(input_data, "Processing data")
    spinner1 = spinner.Spinner()
    spinner1.start()

    # Define the column names as 'index' and specific keys from the JSON data
    columns = ['index', 'downloaded', 'id', 'broadcastType', 'status', 'publishedAt', 'gameName', 'title']  # replace 'key1', 'key2' with your specific keys
    # Define the data as the index and values of the specific keys in the JSON data
    data = [[index] + [util_functions.simple_convert_timestamp(item[key]) if key == 'publishedAt' else item[key] for key in columns[1:]] for index, item in enumerate(input_data)]
    # Call the function

    create_popup1(windName, columns, data, input_data, file_path)
# -----------------------------------------------------------------------------------

    listIndexs = [(index[0], input_data[index[0]]) for index in selected_items]
    print("🐍 File: new_mass_gql/tk_get_file_list.py | Line: 440 | undefined ~ listIndexs",listIndexs)
    print("🐍 File: new_mass_gql/tk_get_file_list.py | Line: 440 | undefined ~ selected_items",selected_items)

    # for index in listIndexs:
    #     print(input_data[int(index)].get('title'))
    #     print(input_data[int(index)].get('publishedAt'), '\n')
    spinner1.stop()

    return listIndexs[0] if listIndexs else None
    # BUG if empty close will be an empty [] and errors as it has no indexes[0].
    # WATCH set this to 0 index as haven't implemented multi downloading


def call_tk_file(file_path) -> tuple| None:
    windName = os.path.basename(file_path)
    with open(file_path, 'r') as f:
        jsond = json.load(f)
    return process_data(jsond, windName, file_path)
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

# file = "C:\\Users\\970EVO-Gamer\\AppData\\Local\\Stream-Downloader-Util\\jsons\\algobro.json"
# call_tk_file(file)
# if __name__ == '__main__':
#     call_tk_file(file_path)

# input('exit ................')
