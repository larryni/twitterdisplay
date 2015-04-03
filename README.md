# twitterdisplay
Simple html5 Twitter display, probably only runs in Chrome.

##Requirements
* [tweepy](https://github.com/tweepy/tweepy)
* jqery
* [twitter-highlights-js](https://github.com/egermano/twitter-highlights-js)

##Instructions
* Copy index.html, tweets.js, and style.css to your server. 
* Download twitter-highlights-js and copy jquery.twitterParsing.js to the server folder - update script src in index.html.
* Copy tweets.py to wherever you want to run it from. Edit tweets.py and add your Twitter credentials, edit path to server folder where the csv will be written (alternatively, copy the example/tweets.csv to the server folder if you only want to test).
* Add a cron job that runs tweets.py every minute.
* Open index.html

##Screenshot
![alt tag](http://i.imgur.com/LtoyoVF.png)
