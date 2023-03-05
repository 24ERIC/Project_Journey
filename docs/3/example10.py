from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
from bs4 import BeautifulSoup
try:
    html = urlopen("https://developer.mozilla.org/en-US/docs/Web/HTML/Element/iframe")
except HTTPError as e:
    print(e)
except URLError:
    print("Server down or incorrect domain")
else:
    res = BeautifulSoup(html.read(), "html5lib")
    tag = res.find("iframe")
    print(tag['src']) #URl of iframe ready for scraping