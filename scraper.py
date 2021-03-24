#!/usr/bin/python3

from bs4 import BeautifulSoup
import requests
import re

#This URL will be the URL that your login form points to with the "action" tag.
POSTLOGINURL = 'https://care.oneplansoftware.co.uk/family-login.php'

#This URL is the page you actually want to pull down with requests.
REQUESTURL = 'https://care.oneplansoftware.co.uk/family-view-rota.php'

loginPayload = {
    'email': 'stuart@stuncal.co.uk',
    'password': '123456',
    'subform': 'login'
}

rotaPayload = {
  'sdatefield': '25/03/2021',
  'edatefield': '26/03/2021',
  'subform': 'changeDate',
  'allService': ''
}

with requests.Session() as session:
    post = session.post(POSTLOGINURL, data=loginPayload)
    result = session.post(REQUESTURL, data=rotaPayload)
    #print(result.content)   #or whatever else you want to do with the request data!

    # Save the content
    content = result.content

    #Create soup
    soup = BeautifulSoup(content, features="lxml")
    #print(soup.prettify)
    table_body=soup.find('tbody')
    #rows=table_body.find_all('tr', class_='success')
    rows=table_body.find_all('tr')

    for row in rows:
        cols=row.find_all('td')
        cols=[x.text.strip() for x in cols]
        print(cols)
