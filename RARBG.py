from tkinter import Tk, messagebox, StringVar, Label, Entry, Button, ttk
from bs4 import BeautifulSoup
import time, os, pyperclip, requests, tkinter.ttk
import os

rarbg_path = '%s\\eliasbenb' %  os.environ['APPDATA']

def rarbg():
    def rarbg_callback():
        rarbg_domain = rarbg_domain_entry.get()
        rarbg_category = rarbg_category_entry.get()
        rarbg_clipboard = rarbg_clipboard_combobox.get()
        rarbg_link = rarbg_domain + 'rssdd.php?category=' + rarbg_category
        try:
            rarbg_request = requests.get(rarbg_link)
        except:
            messagebox.showinfo("RARBG Scraper @eliasbenb", "Something is wrong with the domain/category you inputed.\nMake sure that the domain ends with trailing '/'")

        rarbg_source = rarbg_request.content
        rarbg_soup = str(BeautifulSoup(rarbg_source, 'lxml'))

        rarbg_clean_soup = rarbg_soup.replace('<', ' ')
        rarbg_clean_soup = rarbg_clean_soup.replace('>', ' ')
        rarbg_clean_soup = rarbg_clean_soup.split(' ')

        rarbg_clean_soup = str([i for i in rarbg_clean_soup if i.startswith('magnet')])
        rarbg_clean_soup = rarbg_clean_soup.replace('magnet:?', '\nmagnet:?')
        rarbg_clean_soup = rarbg_clean_soup.replace("', '", "")
        rarbg_clean_soup = rarbg_clean_soup.replace("['", "")
        rarbg_clean_soup = rarbg_clean_soup.replace("']", "")
        rarbg_clean_soup = rarbg_clean_soup.replace(r"\n", "")
        rarbg_magnets = "==== Made by @eliasbenb ====" + rarbg_clean_soup

        if rarbg_clipboard == "Yes":
            pyperclip.copy(rarbg_magnets)
            messagebox.showinfo("RARBG Scraper @eliasbenb", "Magnets links successfully copied to clipboard")
        else:
            pass
        
        rarbg_timestr = time.strftime(" %Y%m%d%H%M%S")
        rarbg_file_name = "RARBG Results " + rarbg_timestr + ".txt"
        with open(rarbg_file_name,'w') as rarbg_w1:
            for magnet in rarbg_magnets:
                rarbg_w1.write(magnet)
        print(rarbg_magnets)

        messagebox.showinfo("RARBG Scraper @eliasbenb", "Magnet links successfully exported to local directory")

    def rarbg_load_config():
        rarbg_domain_entry.delete(0,tkinter.END)
        rarbg_category_entry.delete(0,tkinter.END)
        with open(rarbg_path+"\\rarbg_config.env", "r") as rarbg_r1:
            rarbg_saved_config = [line.rstrip('\n') for line in rarbg_r1]
        rarbg_domain_entry.insert(0,rarbg_saved_config[0])
        rarbg_category_entry.insert(0,rarbg_saved_config[1])
        rarbg_clipboard_combobox.insert(0, rarbg_saved_config[2])

    def rarbg_save_config():
        rarbg_domain = rarbg_domain_entry.get()
        rarbg_category = rarbg_category_entry.get()
        rarbg_clipboard = rarbg_clipboard_combobox.get()
        with open(rarbg_path+"\\rarbg_config.env", "w") as rarbg_w2:
            rarbg_w2.write(rarbg_domain+'\n'+rarbg_category+'\n'+rarbg_clipboard)
    
    rarbg_app = Tk()

    rarbg_domain_text = StringVar()
    rarbg_domain_label = Label(rarbg_app, text="Enter RARBG Domain Link:")
    rarbg_domain_label.place(relx=.5, rely=.1, anchor="center")
    rarbg_domain_entry = Entry(rarbg_app, textvariable=rarbg_domain_text)
    rarbg_domain_entry.place(relx=.5, rely=.20, anchor="center")

    rarbg_category_text = StringVar()
    rarbg_category_label = Label(rarbg_app, text="Enter Category String:")
    rarbg_category_label.place(relx=.5, rely=.35, anchor="center")
    rarbg_category_entry = Entry(rarbg_app, textvariable=rarbg_category_text)
    rarbg_category_entry.place(relx=.5, rely=.45, anchor="center")

    rarbg_clipboard_label = Label(rarbg_app, text="Copy the Magnets to Clipboard?")
    rarbg_clipboard_label.place(relx=.5, rely=.60, anchor="center")
    rarbg_clipboard_combobox = ttk.Combobox(rarbg_app, values=['Yes', 'No'])
    rarbg_clipboard_combobox.place(relx=.5, rely=.70, anchor="center")

    rarbg_ok_button = Button(rarbg_app, text = "OK", command = rarbg_callback)
    rarbg_ok_button.place(relx=.5, rely=.91, anchor="center")

    rarbg_load_config_button = Button(rarbg_app, text = "Load Config", command = rarbg_load_config)
    rarbg_load_config_button.place(relx=0.2, rely=0.5, anchor="center")

    rarbg_save_config_button = Button(rarbg_app, text = "Save Config", command = rarbg_save_config)
    rarbg_save_config_button.place(relx=0.8, rely=0.5, anchor="center")
    
    rarbg_app.title('RARBG @eliasbenb')
    rarbg_app.iconbitmap(rarbg_path+'\\icon.ico')
    rarbg_app.geometry('500x225')
    
    rarbg_app.mainloop()