import requests
from bs4 import BeautifulSoup
import sqlite3
URL="https://weworkremotely.com/categories/remote-programming-jobs"
conn=sqlite3.connect("../jobs.db")
c=conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS jobs(title TEXT,link TEXT)''')
res=requests.get(URL)
soup=BeautifulSoup(res.text,'html.parser')
jobs=soup.select(".jobs article")
for job in jobs:
    title=job.select_one('span.title')
    link="https://weworkremotely.com"+job.find('a')['href']
    if title:
        c.execute("INSERT INTO jobs(title,link)VALUES(?,?)", (title.text, link))
conn.commit()
conn.close()
