# File to visualize json data

import json
import os
import threading
import tkinter as tk
import webbrowser
from datetime import datetime
from tkinter import IntVar, Radiobutton, messagebox, ttk

import funcs
import spinner
from utility_dir import util_functions

# # from ..utility_dir import util_functions

# # to make the file work as a stand alone
# sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
# import funcs
# import spinner
# from utility_dir import util_functions

json_dir = f"{util_functions.get_appdata_dir()}/jsons"

# FEATURE Make a Class ????.


style_theme_names = (
    "winnative",
    "clam",
    "alt",
    "default",
    "classic",
    "vista",
    "xpnative",
)


selected_items = []


# [] Super Twitch ONLY data window
def create_popup1(
    windowName, columns, processed_data, rawdata, file_path, **visual_only
):
    global Main_bg
    Main_bg = "#191825"
    global selected_items
    popup = tk.Tk()
    popup.overrideredirect(False)
    popup.title(windowName)
    popup.minsize(1350, 500)
    style = ttk.Style(popup)
    style.theme_use("alt")
    style.configure(
        "Treeview", background="#191825", fieldbackground="#191825", foreground="white"
    )

    # style.configure("TButton", background=[("pressed", "red"), ("active", Main_bg)], foreground='white')

    # style.configure("Treeview", background="#0b0b13", foreground="white")
    tree = ttk.Treeview(popup, style="Treeview")
    popup.configure(
        bg="#191825",
        highlightbackground="#296D8F",
        highlightcolor="#0b0b13",
        highlightthickness=5,
        height=min(len(processed_data), 17),
    )
    frame1 = tk.Frame(
        popup,
        bg="#191825",
    )  # borderwidth=3, highlightthickness=1, highlightbackground='yellow')
    frame2 = tk.Frame(
        popup, bg="#191825", borderwidth=3
    )  # , highlightthickness=1, highlightbackground='violet')
    frame3 = tk.Frame(
        popup,
        bg=Main_bg,
    )  # borderwidth=3, highlightthickness=1, highlightbackground='white')
    frame4 = tk.Frame(
        popup,
        bg="#191825",
        borderwidth=3,
        highlightbackground="yellow",
        relief="raised",
    )
    frame2_subframe = tk.Frame(frame2, relief="sunken")

    style1 = ttk.Style()
    style1.configure("new.TNotebook", background=Main_bg, foreground="#272525")
    notebook = ttk.Notebook(frame4, style="new.TNotebook")  # , width=400)
    tab1 = tk.Frame(notebook, bg=Main_bg)
    tab2 = tk.Frame(notebook, bg=Main_bg)

    notebook.add(tab1, text="General", compound="center")
    notebook.add(tab2, text="Change Status", compound="center")

    explainer_lable = tk.Label(
        frame2,
        text=(
            "Selection/s made by clicking on a Vod/s with Mouse (Multi Hold Shift)\n"
            "Use 'Make Selection-Close' (Right) Button to make selection,"
            "\nSelection will be the first item in the list"
        ),
        bg="#191825",
        fg="white",
        font=("Calibri", 10, "bold"),
        highlightcolor="white",
        justify="left",
        relief="sunken",
        borderwidth=3,
        padx=5,
        pady=2,
        state="active",
        activebackground="silver",
    )
    # -----------------------------------------------------------------------------------

    tree = ttk.Treeview(
        frame1, columns=columns, show="headings", height=min(len(processed_data), 17)
    )
    # tree.grid(row=1, column=1, sticky='nsew')

    vsb = ttk.Scrollbar(frame3, orient="vertical", command=tree.yview, style="")
    # vsb.grid(row=1, column=2, sticky='nsw')
    tree.configure(yscrollcommand=vsb.set)

    columns_tree = list(columns.keys())
    tree["columns"] = columns_tree
    for col in columns_tree:
        tree.heading(col, text=col)
        if col == "Index":
            tree.column(col, width=20, stretch=tk.NO, anchor="w")
        elif col == "Dld Status":
            tree.column(col, width=75, stretch=tk.YES, anchor="center")
        elif col == "Date":
            tree.column(col, width=75, stretch=tk.YES, anchor="center")
        elif col == "Vod Length":
            tree.column(col, width=75, stretch=tk.YES, anchor="center")
        elif col == "Current Status":
            tree.column(col, width=80, stretch=tk.YES, anchor="center")
        elif col == "Storage type":
            tree.column(col, width=75, stretch=tk.NO, anchor="center")
        elif col == "Vod Id":
            tree.column(col, width=75, stretch=tk.YES, anchor="center")
        elif col == "Stream Category":
            tree.column(col, minwidth=90, stretch=tk.YES)
        elif col == "Title":
            tree.column(col, minwidth=200, width=500, stretch=tk.YES, anchor="w")
        else:
            tree.column(col, width=100, stretch=tk.YES)

    for item in processed_data:
        tree.insert("", "end", values=item)
    # -----------------------------------------------------------------------------------

    title_lable = tk.Label(
        frame4,
        text=(f'Vods List for : {windowName.split('.')[0].title()}'),
        bg="#191825",
        # fg="#296d8f",
        # highlightcolor="red",
        justify="center",
        font=("Arial", 14),
        relief="raised",
        highlightbackground="#096597",
        # highlightthickness=16,
        border=3,
        state="disabled",
        disabledforeground="#dedbd2",
        activebackground="red",
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
                title="QUITTING!!",
                message="No Selection has Been Made,\nAre you Sure you want to proceed?",
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
        highlightcolor="yellow",
        background="#4895ef",
        foreground="white",
        activebackground="#00ff00",
        activeforeground="black",
        underline=5,
        relief="groove",
        overrelief="ridge",
        pady=7,
        cursor="star",
        # style="TButton"
    )

    def delete_item():
        global selected_items
        for i in tree.selection():
            selected_item = tree.item(i)["values"]
            if selected_item in selected_items:
                selected_items.remove(selected_item)
        count_var.set(f"Selection List: {len(selected_items)}")

        selections_listbox.delete(0, tk.END)
        for items in selected_items:
            selections_listbox.insert(
                tk.END,
                f"# {items[0]}    {days_ago_simple(items[2])} :Days ago    {items[-2]}    {items[-1]}",
            )

        # print(selected_items)

    delete_btn = tk.Button(
        frame4,
        text="Delete selected Item from list",
        command=delete_item,
        height=1,
        width=13,
        font=("calabri", 9, "bold", "italic"),
        highlightcolor="yellow",
        background="#5e1d1d",
        foreground="white",
        activebackground="#df0000",
        activeforeground="white",
        underline=0,
        relief="groove",
        overrelief="ridge",
        pady=2,
    )

    def clear_item():
        selected_items.clear()
        count_var.set(f"Selection List: {len(selected_items)}")
        selections_listbox.delete(0, tk.END)

    clear_btn = tk.Button(
        frame4,
        text="Clear Selected List",
        command=clear_item,
        height=1,
        width=13,
        font=("calabri", 8, "bold", "italic"),
        highlightcolor="yellow",
        background="#29292c",
        foreground="#ff7272",
        activebackground="#df0000",
        activeforeground="white",
        underline=0,
        relief="groove",
        overrelief="ridge",
        pady=1,
        cursor="cross",
    )
    # new_win = Toplevel()
    # new_win.title('Set Item Downloaded')

    def set_item_downloaded(rawdata, file_path, selected_resolution):
        question = messagebox.askyesno(
            "Change Item Downloaded Status",
            f"Set Item/s to '{resolutions[selected_resolution.get()]}' Download status ?",
        )
        if selected_items is []:
            if question is False:
                print("User Closed Window")
        elif question is True:
            items_selected = []
            for i in selected_items:
                items_selected.append(i[0])
            for i in items_selected:
                selected_value = resolutions[selected_resolution.get()]
                rawdata[i]["downloaded"] = (
                    False if selected_value == "False" else selected_value
                )

            # Update the data for the Treeview
            data = [
                [index]
                + [
                    util_functions.simple_convert_timestamp(item[key])
                    if key == "publishedAt"
                    else util_functions.decode_seconds_to_hms(item[key])
                    if key == "lengthSeconds"
                    else item[key]
                    for key in list(value for value in columns.values())[1:]
                ]
                for index, item in enumerate(rawdata)
            ]

            # Clear all existing items in the Treeview
            for item in tree.get_children():
                tree.delete(item)

            # Insert updated data into the Treeview
            for item in data:
                tree.insert("", "end", values=item)
            with open(file_path, "w") as f:
                json.dump(rawdata, f, indent=4)
            selected_items.clear()

    set_downloaded_btn = tk.Button(
        tab2,
        text='Set Item/s to "Downloaded"',
        command=lambda: set_item_downloaded(rawdata, file_path, x),
        height=1,
        width=13,
        font=("Arial", 9, "bold"),
        highlightcolor="yellow",
        background="#4895ef",
        foreground="white",
        activebackground="#FECD1A",
        activeforeground="black",
        underline=0,
        relief="groove",
        overrelief="ridge",
        pady=2,
        cursor="exchange",
    )

    selections_listbox = tk.Listbox(
        frame2_subframe,
        highlightbackground="#242c53",
        selectbackground="#191825",
        height=4,
        width=120,
        justify="left",
        bg="#191825",
        fg="white",
        activestyle="underline",
    )
    selections_listbox.pack(fill="both")

    # tree.bind('<ButtonRelease-1>', delete_item)

    def days_ago_simple(timestamp):
        """
        Returns:
            int of days ago
        """
        dt = datetime.strptime(timestamp, "%Y-%m-%d")
        now = datetime.now()
        difference = now - dt
        return difference.days

    def select_items(_):
        global selected_items

        # print(selected_items)
        for i in tree.selection():
            # print(i)
            # print(tree.item(i)['values'])
            selected_item = tree.item(i)["values"]
            if selected_item in selected_items:
                selected_items.remove(selected_item)
                selected_items.append(selected_item)
            else:
                selected_items.append(selected_item)
            # selected_items.append(tree.item(i)['values'])
        # print(selected_items, "\n")
        selections_listbox.delete(0, tk.END)
        for items in selected_items:
            selections_listbox.insert(
                tk.END,
                f"# {items[0]}    {days_ago_simple(items[2])} :Days ago    {items[-2]}    {items[-1]}",
            )
        count_var.set(f"Selection List: {len(selected_items)}")

    tree.bind("<<TreeviewSelect>>", select_items)

    open_appdata_btn = tk.Button(
        tab1,
        text="Open Folder",
        underline=5,
        justify="center",
        font=("Calabri", 8),
        relief="raised",
        overrelief="groove",
        command=lambda: os.startfile(json_dir),  # NOTE gets link from File arg.
        height=1,
        width=9,
        highlightcolor="red",
        background="#4361ee",
        foreground="white",
        activebackground="#003554",
        activeforeground="white",
        pady=3,
    )

    # Create a StringVar() variable
    count_var = tk.StringVar()
    count_var.set(f"Selection List: {len(selected_items)}")
    list_name_label = tk.Label(
        frame2,
        textvariable=count_var,
        font=("Arial", 8, "bold"),
        bg="#1B192B",
        fg="White",
        padx=2,
        highlightbackground="#453303",
        highlightthickness=2,
    )
    explainer_lable.pack(side="right", anchor="e", fill="y")
    list_name_label.pack(
        anchor="nw",
        pady=1,
        fill="both",
    )

    def open_in_browser():
        for vods in selected_items:  # selected_items:
            webbrowser.open(f"www.twitch.tv/videos/{vods[6]}")

    open_twitch_btn = tk.Button(
        tab1,
        text="Open Vod's in Browser",
        font=("Arial", 7, "bold"),
        command=open_in_browser,
        bg="#4361ee",
        fg="#fdfdfd",
        underline=14,
        overrelief="ridge",
        activebackground="#003554",
        activeforeground="white",
        pady=2,
        padx=5,
    )
    open_twitch_btn.pack(side="top", padx=5, pady=3)

    def on_close():
        close_conf = messagebox.askyesno(title="CLOSE?", message="Close Window?")
        if close_conf:
            selected_items.clear()
            count_var.set(f"Selection List: {len(selected_items)}")
            selections_listbox.delete(0, tk.END)
            popup.destroy()

    # Change the behavior of the close button
    popup.protocol("WM_DELETE_WINDOW", on_close)
    # -----------------------------------------------------------------------------------

    frame2_subframe.pack(fill="both")
    # frame2_subframe.grid()

    frame1.grid(row=1, column=1, sticky="nsew")
    tree.pack(side="left", fill="both", anchor="ne", expand=True)
    vsb.pack(side="left", fill="y", anchor="nw", expand=True, padx=2)

    frame2.grid(row=2, column=1, sticky="nsew")

    frame3.grid(row=1, column=2, sticky="nsew")

    frame4.grid(row=1, column=3, sticky="nsew", rowspan=2)

    # -----------------------------------------------------------------------------------
    open_appdata_btn.pack(side="top", fill="both", padx=5, pady=2)

    title_lable.pack(side="top", fill="x", padx=5, pady=2)
    # -----------------------------------------------------------------------------------

    style = ttk.Style()
    style.configure("Line.TSeparator", background="#44296e")
    sep = ttk.Separator(frame4, orient="horizontal", style="Line.TSeparator")
    sep.pack(side="top", fill="x", padx=10, pady=10, expand=False)
    # -----------------------------------------------------------------------------------

    notebook.pack(side="top", fill="both", expand=True, anchor="nw")

    # -----------------------------------------------------------------------------------
    style = ttk.Style()
    style.configure("Line.TSeparator", background="#44296e")
    sep = ttk.Separator(frame4, orient="horizontal", style="Line.TSeparator")
    sep.pack(side="top", fill="x", padx=10, pady=10, expand=False)
    # -----------------------------------------------------------------------------------

    if not visual_only:
        resolutions = ["1080p", "720p", "480p", "360p", "160p", "False"]
        x = IntVar()
        for index in range(len(resolutions)):
            radiobutton = Radiobutton(
                tab2,
                bg="#191825",
                fg="#0576A7",
                activebackground="#191825",
                activeforeground="#00ff95",
                highlightbackground="yellow",
                # selectcolor='aqua',
                anchor="w",
                text=resolutions[index],  # adds text to radio buttons
                variable=x,  # groups radiobuttons together if they share the same variable
                value=index,  # assigns each radiobutton a different value
                padx=1,  # adds padding on x-axis
                font=("Impact", 12),
                compound="left",  # adds image & text (left-side)
                # style="switch",
            )
            radiobutton.pack(fill="both", anchor="w")

    set_downloaded_btn.pack(side="top", fill="x", padx=1, pady=5)
    # -----------------------------------------------------------------------------------

    make_selec_btn.pack(side="bottom", fill="x", padx=1, pady=2)

    delete_btn.pack(fill="x", side="bottom", padx=1, pady=2)

    clear_btn.pack(side="bottom", fill="x", padx=1, pady=2)

    popup.grid_columnconfigure(1, weight=1)
    popup.grid_rowconfigure(1, weight=1)

    popup.update_idletasks()

    width = popup.winfo_width()
    height = popup.winfo_height()

    if visual_only:
        make_selec_btn.config(text="Exit", command=popup.destroy, cursor="")
        set_downloaded_btn.pack_forget()
        explainer_lable.pack_forget()
        title_lable.config(text=f'New Vods for : {windowName.split('.')[0].title()}')
        # tree.config(selectmode="none")
        # clear_btn.pack_forget()
        # clear_btn.pack_forget()
        # delete_btn.pack_forget()
        # selections_listbox.pack_forget()
        # frame2_subframe.pack_forget()
        # list_name_label.pack_forget()
        # frame4.pack_forget()

    popup.geometry(f"{width}x{height}")
    popup.mainloop()


def process_data(input_data, windName, file_path, **kwargs) -> tuple | None:
    spinner1 = spinner.Spinner()
    spinner1.start()
    columns = {
        "Index": "index",
        "Dld Status": "downloaded",
        "Date": "publishedAt",
        "Vod Length": "lengthSeconds",
        "Current Status": "status",
        "Storage type": "broadcastType",
        "Vod Id": "id",
        "Stream Category": "gameName",
        "Title": "title",
    }
    data = [
        [index]
        + [
            util_functions.simple_convert_timestamp(item[key])
            if key == "publishedAt"
            else util_functions.decode_seconds_to_hms(item[key])
            if key == "lengthSeconds"
            else item[key]
            for key in list(value for value in columns.values())[1:]
        ]
        for index, item in enumerate(input_data)
    ]

    if kwargs:
        create_popup1(
            windName, columns, data, input_data, file_path, visual_only=kwargs["arg1"]
        )
    else:
        create_popup1(windName, columns, data, input_data, file_path)

    listIndexs = [(index[0], input_data[index[0]]) for index in selected_items]
    spinner1.stop()
    return listIndexs[0] if listIndexs else None
    # FIX if empty close will be an empty [] and errors as it has no indexes[0]| error handling on the call but still not ideally what i want.
    # WATCH set this to 0 index as haven't implemented multi downloading


def call_tk_file(file_path) -> tuple | None:
    windName = os.path.basename(file_path)
    with open(file_path, "r") as f:
        jsond = json.load(f)
    return process_data(jsond, windName, file_path)


def call_tk_data(data):
    windName = data[0].get("displayName")
    kwargs = {"arg1": True}
    t1 = threading.Thread(target=process_data, args=(data, windName, ""), kwargs=kwargs)
    t1.start()
    return


def call_as_solo():
    appdata_dir = rf"{util_functions.get_appdata_dir()}\jsons"
    list_files = []
    for files in os.listdir(appdata_dir):
        list_files.append(files)
    chosen_dir = rf'{appdata_dir}\{funcs.multi_choice_dialog('Open:', list_files)}'
    return call_tk_file(chosen_dir)


# file = "C:\\Users\\970EVO-Gamer\\AppData\\Local\\Stream-Downloader-Util\\jsons\\algobro.json"
# with open(file, 'r') as f:
#     data = json.load(f)

# call_tk_data(data)
# call_tk_file(file)
# if __name__ == '__main__':
#     call_tk_file(file_path)

# input('exit ................')
