# Get all the links to other wikipedia pages, with Title

from bs4 import BeautifulSoup
import requests

url = 'https://en.wikipedia.org/wiki/Transhumanism'
# get contents from url
content = requests.get(url).content
# get soup
soup = BeautifulSoup(content, 'lxml')  # choose lxml parser
# find all the paragraph tags
p_tags = soup.findAll('p')
# gather all <a> tags
a_tags = []
for p_tag in p_tags:
    a_tags.extend(p_tag.findAll('a'))
# filter the list : remove invalid links
a_tags = [a_tag for a_tag in a_tags if 'title' in a_tag.attrs and 'href' in a_tag.attrs]
# print all links
for i, a_tag in enumerate(a_tags):
    print('[{0}] {1} -> {2}'.format(i, a_tag.get('title'), a_tag.get('href')))
