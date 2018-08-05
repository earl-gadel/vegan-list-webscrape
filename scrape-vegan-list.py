from lxml import html
from lxml import etree
import requests

page = requests.get('https://www.peta.org/living/food/animal-ingredients-list/')
tree = html.fromstring(page.content)

non_vegan_list = tree.xpath('//b/text()')
non_vegan_list = [s.replace('.', '') for s in non_vegan_list]

list_file = open('the_list.txt', 'w')
for item in non_vegan_list:
    list_file.write('%s\n' % item)

print('Success!')