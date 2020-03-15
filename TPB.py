from tkinter import Tk, messagebox, StringVar, Label, Entry, Button, ttk
from bs4 import BeautifulSoup
import time, os, pyperclip, requests

def tpb():
    def tpb_callback():
        tpb_domain = tpb_domain_entry.get()
        tpb_category = tpb_category_entry.get()
        tpb_clipboard = tpb_clipboard_combobox.get()
        tpb_rssLink = tpb_domain + 'rss/' + tpb_category
        try:
            tpb_request = requests.get(tpb_rssLink)
            if tpb_request.status_code == 200:
                print(tpb_request.status_code)
        except:
            messagebox.showinfo("TPB Scraper @eliasbenb", "Something is wrong with the domain/category you inputed.\nMake sure that the domain ends with trailing '/'")

        tpb_request = requests.get(tpb_rssLink)
        tpb_source = tpb_request.content
        tpb_soup = str(BeautifulSoup(tpb_source, 'lxml'))

        tpb_cleanSoup = tpb_soup.replace('<', ' ')
        tpb_cleanSoup = tpb_cleanSoup.replace('>', ' ')
        tpb_splitSoup = tpb_cleanSoup.split(' ')

        tpb_magnets = str([i for i in tpb_splitSoup if i.startswith('magnet')])
        tpb_magnets = tpb_magnets.replace('magnet:?', '\nmagnet:?')
        tpb_magnets = tpb_magnets.replace("', '", "")
        tpb_magnets = tpb_magnets.replace("['", "")
        tpb_magnets = tpb_magnets.replace("']", "")
        tpb_magnets = tpb_magnets.replace(r"\n", "")
        tpb_magnets = "==== Made by @eliasbenb ====" + tpb_magnets

        if tpb_clipboard == "Yes":
            pyperclip.copy(tpb_magnets)
            messagebox.showinfo("TPB Scraper @eliasbenb", "Magnets links successfully copied to clipboard")
        else:
            print("Magnets not copied to clipboard")

        timestr = time.strftime(" %Y%m%d%H%M%S")
        tpb_filename = "TPB Results " + timestr + ".txt"
        print(tpb_filename)
        with open(tpb_filename,'w') as f:
            for item in tpb_magnets:
                f.write(item)
        
        messagebox.showinfo("TPB Scraper @eliasbenb", "Magnet links successfully exported to local directory")

    tpb_app = Tk()

    tpb_domain_text = StringVar()
    tpb_domain_label = Label(tpb_app, text="Enter TPB Domain Link:")
    tpb_domain_label.place(relx=.5, rely=.1, anchor="center")
    tpb_domain_entry = Entry(tpb_app, textvariable=tpb_domain_text)
    tpb_domain_entry.place(relx=.5, rely=.20, anchor="center")

    tpb_category_text = StringVar()
    tpb_category_label = Label(tpb_app, text="Enter Category Number:")
    tpb_category_label.place(relx=.5, rely=.35, anchor="center")
    tpb_category_entry = Entry(tpb_app, textvariable=tpb_category_text)
    tpb_category_entry.place(relx=.5, rely=.45, anchor="center")

    tpb_clipboard_label = Label(tpb_app, text="Copy the Magnets to Clipboard?")
    tpb_clipboard_label.place(relx=.5, rely=.60, anchor="center")
    tpb_clipboard_combobox = ttk.Combobox(tpb_app, values=['Yes', 'No'])
    tpb_clipboard_combobox.place(relx=.5, rely=.70, anchor="center")

    tpb_domain_label.pack()
    tpb_domain_entry.pack()
    tpb_category_label.pack()
    tpb_category_entry.pack()
    tpb_clipboard_label.pack()
    tpb_clipboard_combobox.pack()

    tpb_ok_button = Button(tpb_app, text = "OK", command = tpb_callback)
    tpb_ok_button.place(relx=.5, rely=.91, anchor="center")

    tpb_app.title('TPB @eliasbenb')
    tpb_app.iconbitmap(r'icon.ico')
    tpb_app.geometry('500x225')
    tpb_app.mainloop()