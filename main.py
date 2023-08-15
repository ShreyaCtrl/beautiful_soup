from bs4 import BeautifulSoup

with open('ps.html', 'r') as f:
    html = f.read()
    # print(html)
    soup = BeautifulSoup(html, 'html.parser')
    print(soup.prettify())