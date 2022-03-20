import requests
from bs4 import BeautifulSoup
import pprint

res = requests.get('https://news.ycombinator.com/news')
res2 = requests.get('https://news.ycombinator.com/news?p=2')
soup = BeautifulSoup(res.text,'html.parser')
soup2 = BeautifulSoup(res2.text,'html.parser')

link = soup.select('.titlelink')
subtext = soup.select('.subtext')
link2 = soup2.select('.titlelink')
subtext2 = soup.select('.subtext')

mega_link = link+link2
mega_subtext = subtext+subtext2

def sorting(hnlist):
 return sorted(hnlist,key=lambda k:k['votes'],reverse = True)


def create_custom_hn(link,subtext):
 hn = []
 for ind, item in enumerate(link):
    title = item.getText()
    href = item.get('href', None)
    votes = subtext[ind].select('.score')
    if len(votes):
        points = int(votes[0].getText().replace(' points', ''))
        if points > 99:
         hn.append({'title':title , 'link':href , 'votes' :points})
 return sorting(hn)        
 return hn 
pprint.pprint(create_custom_hn(mega_link,mega_subtext))

