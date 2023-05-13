import requests as Requests, time as Time, json as JSON

Usernames = open("usernames.txt", "r").readlines()
Config = open("config.json", "r").read()
APIUrl = "https://users.nexusmods.com/api/check_username?username="

AuthToken = JSON.loads(Config)["token"]

Cookies = {"_app_session": AuthToken}

for Username in Usernames:
	Username = "".join(Username.split())
	
	Response = Requests.get(url = f"{APIUrl}{Username}", cookies = Cookies)	
	ResponseTable = JSON.loads(Response.text)

	if Response.status_code == 200:
		if (ResponseTable["is_username_taken"] == False and ResponseTable["is_username_restricted"] == False):
			print(f"{Username} is valid!")
		else:
			print(f"{Username} not valid.")

		Cookies = {"_app_session": Response.cookies["_app_session"]}
	elif Response.status_code == 429:
		print("Ratelimited, waiting 1 minute.")
		Time.sleep(60)
	elif Response.status_code == 401:
		print("Invalid authorization token provided.")
		break
	else:
		print("Unknown error occured.")
		break
		
	Time.sleep(1.5)
