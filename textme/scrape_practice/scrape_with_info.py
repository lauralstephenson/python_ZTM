#This file scrapes HackerNews for their top rated stories
#import Beautiful Soup web scraper library
from bs4 import BeautifulSoup
#import requests lets you grab HTML files
import requests
#need pretty print
import pprint

res = requests.get("https://news.ycombinator.com/news")
#the second page:
res = requests.get("https://news.ycombinator.com/news?p=2")
#now we want to clean it up and ONLY receive highly rated news
#using BeautifulSoup's HTML parser
soup = BeautifulSoup(res.text, "html.parser")
#use a CSS selector to grab HTML element for, say, a or div
#grabbing the score class to get the scores
#we want the links and the score if over 100
#using .titleline, not .storylink titleline>a because the link is 
#inside the first <a> tag under the titleline element
links = soup.select(".titleline")
subtext = soup.select(".subtext")
links2 = soup.select(".titleline")
subtext2 = soup.select(".subtext")

mega_links = links + links2
mega_subtext = subtext + subtext2

def sort_stories_by_votes(hnlist):
      #sorting votes using a lambda 
      # because a dictionary needs to be sorted into a list
      return sorted(hnlist, key= lambda k:k["votes"], reverse=True)
#make HackerNews pretty
def create_custom_hn(links, subtext):
      hn = []
#retreive the title index
      for idx, item in enumerate(links):
            title = item.getText()
            href = item.get("href", None)
            vote = subtext[idx].select(".score")
            if len(vote):
                  points = int(vote[0].getText().replace(" points",""))
                  if points > 99:
                  #print(points)<--to test
                        hn.append({"title": title, "link": href, "votes": points})
      return sort_stories_by_votes(hn)

pprint.pprint(create_custom_hn(mega_links, mega_subtext))

#stuff can do in soup
#print(soup)<--this prints the entire thing in HTML
#print(soup.body)<--this prints only the body
#print(soup.contents)<--this prints only the contents
#print(soup.find.all("div"))<--this prints only the divs
#print(soup.find.all("a"))<--this prints only the links, which is quite useful
#print(soup.a)<--this prints only the first "a" tag
#print(soup.find)<--find finds the first thing
#print(soup.find("a"))<--finds the first "a" tag




