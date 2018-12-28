# Get all the "References"

from bs4 import BeautifulSoup
import requests

url = 'https://en.wikipedia.org/wiki/Transhumanism'
# get contents from url
content = requests.get(url).content
# get soup
soup = BeautifulSoup(content, 'lxml')  # choose lxml parser
# find all the references
ref_tags = soup.findAll('span', {'class': 'reference-text'})
# iterate through the ResultSet
for i, ref_tag in enumerate(ref_tags):
    # print text only
    print('[{0}] {1}'.format(i, ref_tag.text))
