from pprint import pprint

from bs4 import BeautifulSoup

# with open('ps.html', 'r') as f:
#     html = f.read()
#     # print(html)
#     soup = BeautifulSoup(html, 'html.parser')
    # print(soup.prettify())

with open('home.html', 'r') as html_file:
    content = html_file.read()
    soup = BeautifulSoup(content, 'lxml')
    # here we are finding the first h5 tag only
    h5_data = soup.find('h5')
    print(h5_data)
    # here we are finding all the h5 tags
    h5_data = soup.find_all('h5')
    print('the h5 headings are: ')
    for h5 in h5_data:
        print(h5.text)
    div_class_cards = soup.find_all('div', class_='card')
    print('the divs with class card are: ')
    for card in div_class_cards:
        course_heading = card.h5.text
        course_desc = card.p.text
        course_price = card.a.text.split()[-1]
        print(f'{ course_desc} Title : {course_heading} and Cost : {course_price}')
        print()
        # pprint(card)
    # pprint(div_class_cards)