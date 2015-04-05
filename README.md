# twitterdisplay
First stab at a webapp and GitHub repo.

Simple Twitter home timeline display. The Python script fetches the last 20 tweets from your timeline and writes the data to csv, the javascript file reads the csv and updates the html. 

It's purely to display the timeline, there are no controls to tweet, favourite, etc... All the links, tags and usernames are clickable and open in a new tab.

Only tested in Chrome.

##Requirements
* [tweepy](https://github.com/tweepy/tweepy)
* jqery
* [twitter-highlights-js](https://github.com/egermano/twitter-highlights-js)

##Instructions
* Copy index.html, tweets.js, and style.css to your server. 
* Download twitter-highlights-js and copy jquery.twitterParsing.js to the server folder - update script path in tweets.js.
* Copy tweets.py to wherever you want to run it from. Edit tweets.py and add your Twitter credentials, edit path to server folder where the csv will be written (alternatively, copy the example/tweets.csv to the server folder if you only want to test).
* Add a cron job that runs tweets.py every minute.
* Open index.html

##Screenshot
![alt tag](http://i.imgur.com/LtoyoVF.png)
