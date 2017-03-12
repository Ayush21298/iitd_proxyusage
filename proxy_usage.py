import os
from bs4 import BeautifulSoup
from getpass import getpass
import requests

# getting username and password

username = raw_input("Enter the username : ")
print username
password = getpass("Enter the password : ")

# building request header

headers = {'Referer':'https://oauth.iitd.ac.in/login.php?response_type=code&client_id=C7o6R5kXQxjshCLt1bFkU9YOnIKMbyzN&state=xyz'}

# building data to be sent

values = {'username':username, 'password':password, 'submit':''}

# building query string parameters

params = {'response_type':'code', 'client_id':'C7o6R5kXQxjshCLt1bFkU9YOnIKMbyzN', 'state':'xyz' }

# importing IITD CA certificate :

os.environ['REQUESTS_CA_BUNDLE'] = os.getcwd() + "/CCIITD-CA.crt"

# creating a new session instance

session=requests.Session()

# establishing connection

url = 'https://oauth.iitd.ac.in/authorize.php?response_type=code&client_id=C7o6R5kXQxjshCLt1bFkU9YOnIKMbyzN&state=xyz'

r = session.post(url,data=values, params=params, allow_redirects=False, headers=headers, )
redirect = r.headers['Location']
response = session.get(redirect, allow_redirects=False)
result = session.get('https://track.iitd.ac.in/data_usage.php')

#getting the html elements

soup = BeautifulSoup(result.text,'html.parser')

#Building print base

l = soup.find_all("td",align="right")
x=[]
for h in l:
	x+=[h.text]
print "\n\n\n\n"
for i in range (4):
	print x[i]," : ",x[i+4]