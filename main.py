import requests as Requests, time as Time, json as JSON ## imports

Usernames = open("usernames.txt", "r").readlines() ## turn all usernames into an array of usernames
Config = open("config.json", "r").read() ## read the config file
APIUrl = "https://users.nexusmods.com/api/check_username?username=" ## declare the api url

AuthToken = JSON.loads(Config)["token"] ## get the authentication token

Cookies = {"_app_session": AuthToken} ## create cookies table for the request

for Username in Usernames:
	Username = "".join(Username.split()) ## remove all whitespace from the username
	
	Response = Requests.get(url = f"{APIUrl}{Username}", cookies = Cookies)	## make the request
	ResponseTable = JSON.loads(Response.text) ## convert the json response into an actual table

	if Response.status_code == 200: ## if the request was a success
		if (ResponseTable["is_username_taken"] == False and ResponseTable["is_username_restricted"] == False): ## check if the username is available and if the username is not restricted
			print(f"{Username} is valid!") ## if it is print that its valid
		else: ## this means its either unavailable or the username is restricted
			print(f"{Username} not valid.") ## if it isnt print that its invalid

		Cookies = {"_app_session": Response.cookies["_app_session"]} ## update cookies table with new authentication token so we dont reuse the same one over and over
	elif Response.status_code == 429: ## if the request was ratelimited
		print("Ratelimited, waiting 1 minute.")
		Time.sleep(60) ## wait 60 seconds (im not sure if thats long enough but im gonna keep it how it is)
	elif Response.status_code == 401: ## if the request had a bad authentication token
		print("Invalid authorization token provided.")
		break ## stop loopin thru all the usernames
	else: ## idk wtf happened
		print("Unknown error occured.")
		break ## stop loopin thru all the usernames
		
	Time.sleep(1.5) ## wait 1.5 seconds so i dont get ratelimited
