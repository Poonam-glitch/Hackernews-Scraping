import requests
from bs4 import BeautifulSoup
import pprint
import pandas as pd

url = 'https://news.ycombinator.com/news'
res = requests.get(url,verify=False)
#res should be 200

soup = BeautifulSoup(res.text, 'html.parser')
#.select-(css selector will give me all the elememts containing score id
links = soup.select('.storylink')
subtext = soup.select('.subtext')

def sort_stories_by_votes(hnlist):
    return sorted(hnlist, key = lambda k:k['votes'], reverse= True)

def custom_data_hn(links,subtext):
    hn = []
    for idx,item in enumerate(links):
        title = links[idx].getText()    #toget the text
        href = links[idx].get('href',None)  #to get the href attribute
        vote = subtext[idx].select('.score')
        if len(vote):
            points = int()
            points = int(vote[0].getText().replace(' points', ' '))
            if points > 99:
                hn.append({'title': title,'link': href,'votes': points})

    df = pd.DataFrame(data = hn)
    df.to_csv('hackernews',header=True,index=False)
    return sort_stories_by_votes(hn)

pprint.pprint(custom_data_hn(links,subtext))


