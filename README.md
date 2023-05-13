# NexusMods-Name-Sniper
Tells you if usernames on https://nexusmods.com are available

# Setup
1. Install python (https://www.python.org/)
2. Download the entire repository extract it to a folder
3. In the directory of the folder run this command in command terminal: `pip install -r requirements.txt`
4. Open "config.json" and input your "authentication token", tutorial on how to get one below
5. OPTIONAL: Then open "usernames.txt" and input your own usernames separated like I did
6. In the directory of the folder run this command in command terminal: `python3 main.py`

# Getting Authentication Token

1. Go to https://nexusmods.com & create an account if you haven't already (make sure you're logged in for this & on the site itself)
2. Go to inspect element (press Ctrl + Shift + I or right click & press "Inspect")
3. Find "Application" at the top of the window that pops up (if it isnt there, click on the ">>" and click "Application"
4. Under the "Storage" category expand the "Cookies" section & click on the first option
5. Find the cookie with the name "_app_session" and copy the value
6. You now have the authentication token copied to your clipboard
