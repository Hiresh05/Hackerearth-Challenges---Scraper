from  bs4 import BeautifulSoup
import requests
from selenium import webdriver
import pandas as pd 
import csv

driver = webdriver.Chrome("C:/chromedriver_win32/chromedriver.exe")
driver.get('https://www.hackerearth.com/challenges/')
res = driver.execute_script("return document.documentElement.outerHTML")
driver.quit()
soup = BeautifulSoup(res, 'lxml')

box = soup.find('div', {'class': 'upcoming challenge-list'})
all_hack = box.find_all('div', {'class': 'challenge-card-modern'})
box1 = soup.find('div', {'class': 'previous modern challenge-list'})
all_hack1 = box1.find_all('div', {'class': 'challenge-card'})
box2 = soup.find('div', {'class': 'ongoing challenge-list'})
all_hack2 = box2.find_all('div', {'class': 'challenge-card-modern'})

print('Upcoming Challenges')
print('')
u = []
p = []
o = []
rowlist = [["Challenge phase","Challenge Type","Challenge Name","Date","Description","Time"]]
for sno,hackathon in enumerate(all_hack,1):
    u_type = hackathon.find('div', {'class': 'challenge-type'}).text.replace('\n', '').strip()
    u_name = hackathon.find('div', {'class': 'challenge-name'}).text.replace('\n', '').strip()
    u_date = hackathon.find('div', {'class': 'date'}).text.replace('\n', '').strip()
 
    print(sno)
    print(u_type)
    print(u_name)
    print(u_date)

    u.append("Upcoming Challenges")
    u.append(u_type)
    u.append(u_name)
    u.append(u_date)
    u.append("N/A")
    u.append("N/A")

rowlist.append(u)

print('Previous Challenges')
print('')
for sno1,hackathon1 in enumerate(all_hack1,1):
    p_name = hackathon1.find('div', {'class': 'challenge-name'}).text.replace('\n', '').strip()
    p_description = hackathon1.find('div', {'class': 'challenge-desc'}).text.replace('\n', '').strip()

    print(sno1)
    print(p_name)
    print(p_description)

    p.append("Previous Challenges")
    p.append("N/A")
    p.append(p_name)
    p.append("N/A")
    p.append(p_description)
    p.append("N/A")
    
rowlist.append(p)
    

print('Ongoing Challenges')
print('')
for sno2,hackathon2 in enumerate(all_hack2,1):
    o_type = hackathon2.find('div', {'class': 'challenge-type'}).text.replace('\n','').strip()
    o_name = hackathon2.find('div', {'class': 'challenge-name'}).text.replace('\n','').strip()
    o_time = hackathon2.find('div', {'class': 'challenge-list-meta'}).text.replace('\n','').strip()

    print(sno2)
    print(o_type)
    print(o_name)
    print(o_time)

    o.append("Ongoing Challenges")
    o.append(o_type)
    o.append(o_name)
    o.append("N/A")
    o.append("N/A")
    o.append(o_time)

rowlist.append(o)

print(rowlist)

with open('Hackerearth.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(rowlist) 