from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel

url = 'http://s.cafef.vn/bao-cao-tai-chinh/VNM/IncSta/2017/4/0/0/bao-cao-tai-chinh-cong-ty-co-phan-sua-viet-nam.chn'

connect = urlopen(url)

html_content = urlopen(url).read().decode('utf-8')

# soup = BeautifulSoup(html_content, 'html.parser')

# section = soup.find('section', 'section chart-grid')

# save html to file 2
file = open('itunes.html','wb')
file.writelines(connect)
file.close()
