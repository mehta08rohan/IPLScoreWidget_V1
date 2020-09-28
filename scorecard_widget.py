from tkinter import *
from tkinter.font import Font
import requests
from bs4 import BeautifulSoup 

def getScore():
    txtlist=[]
    URL = "https://www.cricbuzz.com/"
    r = requests.get(URL) 
    soup = BeautifulSoup(r.content, 'html5lib')
    team1 = soup.find('div', attrs = {'class':'cb-hmscg-bwl-txt cb-ovr-flo'})
    team2 = soup.find('div', attrs = {'class':'cb-hmscg-bat-txt'})
    for i in team1:
        txtlist.append(i.text)
    for i in team2:
        txtlist.append(i.text)
    return '  '.join(txtlist)


    
    

root = Tk()

root.wm_attributes('-transparentcolor','white')
root.config(bg='white')

myfont = Font(size=20)

currentScore = Label(root,text=getScore(),font=myfont,bg='yellow')

currentScore.pack()


while True:
    currentScore.config(text=getScore())
    currentScore.update()
