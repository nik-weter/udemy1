from bs4 import BeautifulSoup
import requests
from PIL import Image
from io import BytesIO
import re
import os


def start_search():

    search = input("Enter search request")
    param = {"q": search}

    dir_name = search.replace(" ", "_").lower()

    if not os.path.isdir(dir_name):
        os.mkdir("./scrapped_images/"+dir_name)

    r = requests.get("http://www.bing.com/images/search", params=param)

    soup = BeautifulSoup(r.text, "html.parser")
    links = soup.find_all('a', {"class": "thumb"})

    for item in links:
        try:
            img_obj = requests.get((item.attrs["href"]))
            print("Getting ", item.attrs["href"])
            title = item.attrs["href"].split("/")[-1]
            s = re.search( r'.*\.[A-Za-z]{3,4}$', title)
            if s is None:
                print(s, title)
                continue

            img = Image.open(BytesIO(img_obj.content))
            img.save("./scrapped_images/" + dir_name + "/" + title, img.format)
        except:
            print("Couldn't download image")
    start_search()
start_search()