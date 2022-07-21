import requests
from bs4 import BeautifulSoup

#get the dad jokes

#website with dad jokes
source = requests.get('https://www.thepresentfinder.co.uk/blog/60-bad-dad-jokes_73891843.htm').text

#defining my parser
soup = BeautifulSoup(source, 'html5lib')

#all the jokes plus extra junk
jokes = soup.find_all("p")

#viewing just text and adding it to a list
unedited_joke_list = []
for joke in jokes:
    joke_text = joke.text
    unedited_joke_list.append(joke_text)

#filtering out most of the junk. every joke starts with a number, so using isnumeric to pull those out 
edited_joke_list = []
for joke in unedited_joke_list:
    if joke[0].isnumeric() == False:
        continue
    else:
        edited_joke_list.append(joke)

#two non-jokes started with a number, so brute force removing them from the list
edited_joke_list.pop(0)
edited_joke_list.pop(0)

#finally trimming the number and spaces off of the beggining of the jokes and I have the list of jokes I need
joke_list = []
for joke in edited_joke_list:
    joke_list.append(joke[3:])
