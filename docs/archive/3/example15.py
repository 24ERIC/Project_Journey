"""
python3 ./example15.py
"""


from urllib.request import urlopen

url = "http://olympus.realpython.org/profiles/aphrodite"

page = urlopen(url)

# print(page)

html_bytes = page.read()

html = html_bytes.decode("utf-8")

print(html)