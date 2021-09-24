from webbot import Browser
from bs4 import BeautifulSoup
import time
import sys

def is_exchange_online_checkbox(tag):
    title = tag.get("title")
    return tag.name == "div" and title is not None and "Exchange Online" in title

def search_user(web, user_id):
    web.click(tag="input",id="SearchBox47",css_selector='input[placeholder="Durchsuchen der Liste der aktiven Benutzer "]')
    for i in range(200):
        web.type(web.Key.DELETE)
        web.type(web.Key.BACKSPACE)
    web.type(user_id)
    web.type(web.Key.ENTER)
    time.sleep(2)

def open_apps_of_user(web, user_id):
    web.click(text=user_id,tag="span")
    time.sleep(6)
    web.click(text="Lizenzen und Apps")
    time.sleep(2)
    web.click(text="Apps")
    time.sleep(2)

def ensure_exchange_online(web, user_id):
    soup = BeautifulSoup(web.get_page_source(), "html.parser")
    checkbox = soup.body.find(is_exchange_online_checkbox)
    if checkbox is None:
        print(f"Error: Exchange Online option not available for {user_id}", file=sys.stderr)
        return
    exchange_online_enabled = "is-checked" in checkbox.get("class")
    if not exchange_online_enabled:
        web.click(text="Exchange Online")
        print(f"Enabling Exchange online for {user_id}")
    else:
        print(f"Exchange online already active for {user_id}")

def save_and_close(web):
    web.click(text="Änderungen speichern")
    web.click(css_selector='button[aria-label="Schließen"')

web = Browser()

web.go_to("https://admin.microsoft.com/adminportal/home#/users")
input("Press enter after logging in... ")

filename = sys.argv[1]
with open(filename, "r") as file:
    user_ids = file.read().split('\n')[:-1]

for user_id in user_ids:
    search_user(web, user_id)
    open_apps_of_user(web, user_id)
    ensure_exchange_online(web, user_id)
    save_and_close(web)
