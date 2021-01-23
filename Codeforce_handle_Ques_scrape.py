from bs4 import BeautifulSoup
import requests

username = input("Enter Your Codeforces Handle : ")

password = input("Enter Your Password : ")

with requests.Session() as s:

	url = "https://codeforces.com/enter?back=%2Fprofile%2Fchints11"


	headers = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'}

	r = s.get(url, headers = headers)

	


	login_data = {
				'action': 'enter',
				'ftaa': 'pg4sgj8y1f1ni3buxy',
				'bfaa': '010a9b5848bf69e68fb8567aa78c4bc3',
				'handleOrEmail': username,
				'password': password,
				'_tta': '115'
				}


	soup = BeautifulSoup(r.content, 'lxml')


	csrf_token = soup.find('meta', {'name' : 'X-Csrf-Token'})['content']


	login_data['csrf_token'] = csrf_token

	r = s.post(url, data = login_data, headers = headers)

	r = s.get("https://codeforces.com/problemset/standings?friendsEnabled=on", headers = headers).text

	soup = BeautifulSoup(r, 'lxml')		

	list_ = soup.find('div', {'style' : 'background-color: white;margin:0.3em 3px 0 3px;position:relative;'}).find('table', class_ = "")

	handle_standings = {}

	flag=0
	
	for handles in list_.find_all('tr'):

		if flag==1:

			standing = handles.td.text.strip()

			names = handles.a.text

			questions = handles.find_all('td')[2].text.strip()

			handle_standings[names] = [standing, questions]

		flag=1

print("********************")

while 1:
	print("Press 1 to show list of friends.")
	print("Press 2 to see the standings and Number of Questions by handle.")
	print("Press 0 to exit")
	print("********************")

	a = input()

	if a=='1':
		for name in list(handle_standings.keys()):
			print(name)
	elif a=='2':
		print("Enter the handle")
		print("--------------------")
		h = input()
		print("--------------------")
		try:
			print("Standings - "+handle_standings[h][0])
			print("Number of questions - "+handle_standings[h][1])
		except:
			print("Please Enter correct handle")		
	elif a=="0":
		break
	else:
		print("Invalid input")	

	print("********************")