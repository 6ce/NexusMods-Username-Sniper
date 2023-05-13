# NexusMods-Name-Sniper
Tells you if usernames on https://nexusmods.com are available

# Setup
1. Install python (https://www.python.org/)
2. Download the entire repository extract it to its own folder (you can use this to extract it: https://www.win-rar.com/)
3. In the directory of the folder run this command in command terminal: `pip install requests`
4. Open "config.json" and input your "authentication token" like this: https://ibb.co/RhSnfqy, tutorial on how to get one below
5. Then open "usernames.txt" and input your own usernames separated like I did (you'll need something like https://code.visualstudio.com/ to edit it correctly). If you want, you can just copy the contents of "usernames_example.txt" into "usernames.txt" (its just a bunch of 3 character combinations)
7. In the directory of the folder run this command in command terminal: `python main.py`

# Getting Authentication Token
1. Go to https://nexusmods.com & create an account if you haven't already (make sure you're logged in for this & on the site itself)
2. Go to inspect element (press Ctrl + Shift + I or right click & press "Inspect")
3. Find "Application" at the top of the window that pops up (if it isnt there, click on the ">>" and click "Application"
4. Under the "Storage" category expand the "Cookies" section & click on the first option
5. Find the cookie with the name "_app_session" and copy the value
6. You now have the authentication token copied to your clipboard

# Disclaimer
Due to ratelimiting, this is pretty slow and can take a fuck ton of time to generate you a username
