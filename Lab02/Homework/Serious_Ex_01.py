# Part 1: Scrape all songs’ names and artists from the iTunes top songs and save them into a xlsx file
# => phải vào được link chart songs => lấy được các đường link
from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel
from youtube_dl import YoutubeDL
# Connect the website
url = 'https://www.apple.com/itunes/charts/songs/'

# Create a connection
connect = urlopen(url)
# data = connect.read()
html_content = urlopen(url).read().decode('utf-8')

# save html to file
# Neu su dung write() thi file la file chua decode
# neu su dung writelines() thi file la duong link url
# f = open ('dantri.html', 'wb')
# f.write(data)
# f.close()

# save html to file 2
# file = open('itunes.html','wb')
# file.writelines(connect)
# file.close()


soup = BeautifulSoup(html_content, 'html.parser')

section = soup.find('section', 'section chart-grid')


# Part 01
# 3. Extract data
li_list = section.find_all('li')
file_excel = []
for li in li_list:
    file_excel.append(
        {
            'song' : (li.h3.string),
            'artist' : (li.h4.string)
        }
    )
pyexcel.save_as(records=file_excel, dest_file_name="itunes.xlsx")


# Part 02
li_list = section.find_all('li')
search = {
    'default_search':'ytsearch',
    'maxdownload':1
}
dl = YoutubeDL(search)
for li in li_list:
    dl.download(li.h3.string)