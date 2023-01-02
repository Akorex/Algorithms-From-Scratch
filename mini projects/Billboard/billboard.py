"""
This is a python web scraping project which saves the billboard Hot 100 as a file.
It also prints the chart history of artists
"""

# import dependencies
from bs4 import BeautifulSoup
import requests
import sys
import os
from datetime import date

save_path = os.getcwd() + "\Billboard"
today = date.today().strftime("%d %b, %Y")

def query_user():
    print("Welcome to the Billboard Hot 100 and Chart History programme. \n")
    print("What service do you want? 1. Hot 100 \t 2. Billboard 200  \n 3.Chart History \n")
    user_input = input("== ")

    return user_input


def get_hot100():
    url = "https://www.billboard.com/charts/hot-100"
    print("You have selected Hot 100. Please wait while we gather the Hot 100 information.\n")
    
    # get the entries
    bill = requests.get(url).text
    soup = BeautifulSoup(bill, "html.parser")
    entries = soup.find_all("div", class_="o-chart-results-list-row-container")

    # open and write into the file
    f = open(os.path.join(save_path, f"Hot 100, retrieved {today}.txt"), "w")
    f.write(f"The Hot 100 list for {today} is: \n\n")

    for entry in entries:
        entry_rank = entry.find("span", class_="c-label").text.strip()
        entry_title = entry.find("h3", class_="c-title").text.strip()
        entry_artist = entry.find("span", class_="a-no-trucate").text.strip()

        f.write(f"{entry_rank}.")
        f.write(f"{entry_title} by ")
        f.write(entry_artist.replace("&", "and"))
        f.write("\n\n")

    f.close()
    print(f"Hot 100 file saved successfully. Find it in the billboard folder...")


def get_hot200():
    url = "https://www.billboard.com/charts/billboard-200"
    print("You have selected Hot 200. Please wait while we gather the Hot 200 information.\n")
    
    # get the entries
    bill = requests.get(url).text
    soup = BeautifulSoup(bill, "lxml")
    entries = soup.find_all("div", class_="o-chart-results-list-row-container")

    # open and write into the file
    f = open(os.path.join(save_path, f"Hot 200, retrieved {today}.txt"), "w")
    f.write(f"The Hot 200 list for {today} is: \n\n")
   
    for entry in entries:
        entry_rank = entry.find("span", class_="c-label").text.strip()
        entry_title = entry.find("h3", class_="c-title").text.strip()
        entry_artist = entry.find("span", class_="a-no-trucate").text.strip()

        f.write(f"{entry_rank}. ")
        f.write(f"{entry_title} by ")
        f.write(entry_artist.replace("&", "and"))
        f.write("\n\n")

    f.close()
    print(f"Hot 100 file saved successfully. Find it in the billboard folder...")


def get_charthistory():
    print("Please enter the name of the artist: \n")
    user_input = input("> ")

    artist = user_input.lower().replace(" ", "-")
    url = "https://www.billboard.com/music/"+artist

    print("Gathering Chart History Information")
    
    # get the history & entries
    bill = requests.get(url).text
    soup = BeautifulSoup(bill, "html.parser")
    entries = soup.find_all("div", class_="o-chart-results-list-row")


    f = open(os.path.join(save_path, f"{user_input}, retrieved {today}.txt"), "w")
    f.write(f"The Chart History for {user_input} is: \n\n")    

    for entry in entries:
        entry_title = entry.find("h3", class_ = "c-title").text.strip()
        entry_artists = entry.find("span", class_ = "c-label").text.strip()

        f.write(f"{entry_title} by ")
        f.write(f"{entry_artists} ")
        f.write("\n\n")

   
    f.write(f"and more at {url}")
    f.close()

    print(f"Chart History for {user_input} is saved successfully.")


if __name__ == "__main__":
    user_input = query_user()

    if user_input == "1":
        get_hot100()
        sys.exit()
    
    if user_input == "2":
        get_hot200()
        sys.exit()

    if user_input == "3":
        get_charthistory()
        sys.exit()


    print("You have chosen a wrong option. Programme will now exit\n")
    sys.exit("Bye")
