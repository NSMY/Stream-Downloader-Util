# Global variable to hold the selected items
import json
import os
import tkinter as tk

selected_items = []

def create_popup(windowName, content):
    global selected_items
    popup = tk.Tk()
    popup.overrideredirect(False)
    popup.title(windowName)
    popup.configure(bg="#0b0b13", takefocus=1, borderwidth=0, border=False)

    # Calculate the maximum length of the content
    max_length = max(len(value) for value in content)

    listbox = tk.Listbox(popup, selectmode='MULTIPLE', justify='left', width=max_length, height=30, font="Calibri", background="#0b0b13", foreground='white', activestyle='underline', takefocus=1)
    for value in content:
        listbox.insert(tk.END, f" {value}")
    listbox.grid(row=0, column=0, sticky='nsew')  # Use grid instead of pack

    # Function to get the selected item(s)
    def get_selection(event):
        global selected_items
        # Get the index of the clicked item
        clicked_index = listbox.nearest(event.y)

        # Get the text of the clicked item
        clicked_item = listbox.get(clicked_index)

        # If the item is already in the list, remove it
        if clicked_item in selected_items:
            selected_items.remove(clicked_item)
        # Otherwise, add it to the list
        else:
            selected_items.append(clicked_item)

    # Bind the function to the listbox
    listbox.bind("<ButtonRelease-1>", get_selection)

    # Set the window size
    button1 = tk.Button(popup, text="Close", command=lambda: popup.quit(), height=1, width=4, highlightcolor='yellow', background='#296d8f', foreground='white', activebackground='red', activeforeground='white')
    button1.grid(row=1, column=0, sticky='se')  # Use grid and place at bottom right

    # Configure the grid weights
    popup.grid_columnconfigure(0, weight=1)
    popup.grid_rowconfigure(0, weight=1)

    # Update the window to calculate the size of the content
    popup.update_idletasks()

    # Get the width and height of the content
    width = popup.winfo_width()
    height = popup.winfo_height()

    # Add some padding
    width += 5
    height += 5

    # Set the window size
    popup.geometry(f"{width}x{height}")
    popup.mainloop()

    # Destroy the window
    popup.destroy()






file = "C:\\Users\\970EVO-Gamer\\AppData\\Local\\Stream-Downloader-Util\\jsons\\klean.json"
winName = os.path.basename(file)
with open(file, 'r') as f:
    jsond = json.load(f)
list1 = [('{:5}    {:25}    {:20}    {:30}    {:45}    {:25}'.format("Index", "Downloaded", "Vod Style", "VodID", "Game Name", "Title"))]
for index, items in enumerate(jsond):

    list0 = items['title']
    list2 = items['id']
    list3 = items['gameName']
    list4 = items['broadcastType']
    list5 = items['downloaded']
    llist = ('{:7}    {:25}    {:15}    {:25}    {:40}    {:25}'.format(index, f"Downloaded:  {list5}", list4, list2, list3, list0))
    list1.append(f'{llist}')
create_popup(winName, list1)
lists = [items.split() for items in selected_items]
listIndexs = [index[0] for index in lists]
print("🐍 File: new_mass_gql/tessettt.py | Line: 196 | undefined ~ hhe",listIndexs)
