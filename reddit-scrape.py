from lxml import html
import requests

page = requests.get('https://www.reddit.com/r/conservative/')
tree = html.fromstring(page.content)

titles = tree.xpath('//h2 class="imors3-0 euspgB"/text()')
#non_vegan_list = [s.replace('.', '') for s in non_vegan_list]

list_file = open('reddit_data.txt', 'w')
for item in titles:
    list_file.write('%s\n' % item)

print('Success!')