
# covid-19-bot

 - Reddit reply BOT writter in Python, updates users with covid-19 stats.
- The data is fetched from the crowd-sourced db published @ [covid19india.org](https://www.covid19india.org/).  
- You can change the data sources and made it usabe for any country/subreddit.
- [Relavant Thread](http://reddit.com/comments/g1zi21/_/fq8srgb)

## How-to-deploy

### Configure

- Clone/Download this repo. and update the config.py file with your credentials.
-  If using different data sources, update it in fetch_data(), such that it'll return comment body.

### Running
- Launch the bot:
	>python3 bot.py
- Since the bot listens for a stream of comments, it needs to be running all the time, if there's an alternative let me know/open PR. So, make sure that the script is alive at all times.
- Some viable options, if you don't want to run it on your System:
	- Raspberry-pi
	- Heroku
	- Free tiers/credits on AWS/GCP/Azure
	
## To-Do

 - [ ] State-wise Reports  
 - [ ] Testing Data

## Demo
![Example](https://github.com/parshnt/covid-19-bot/raw/master/pics/picture.png)
