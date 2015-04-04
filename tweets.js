$(document).ready(function () {

    // Check csv file for tweets and display them, refresh every 5 seconds
    setInterval(function (file) {
        // fetch text file
        $.get('tweets.csv', function (data) {
            //split on new lines
            var tweets = data.split('\n');

            var div = $('.wrapper')[0];
            $(div).empty(); // clear wrapper, or refreshed content will get appended
            
            for (var i = 0; i < tweets.length - 1; i++) { // -1 as the last line in csv is empty
                var array = tweets[i].split("\t"); // tab delimited csv file
                var displayname = array[0],
                    username = "@" + array[1],
                    avatar = array[2],
                    postedtime = array[3].split(" ")[1], // .split() to display time only
                    text = array[4].replace(/\\/g, ""), // .replace() to remove escape chars
                    medialink = array[5];
                
                var singletweet = '<div class="tweetcontainer">\
                                    <div class="avatar" id="avatar"><img src="' + avatar + '"></div>\
                                    <div class="tweet">\
                                        <div class="head"><span class="displayname" id="displayname">' + displayname + '</span> <span class="username" id="username">' + username + '</span> posted at <span class="postedtime" id="postedtime">' + postedtime + '</span></div>\
                                        <div class="text" id="text">' + text + '</div>\
                                        <div class="mediaembed" id="mediaembed"><img src="' + medialink + '"></div>\
                                    </div>\
                                </div>';
                
                $(div).append(singletweet);
                $('.text, .username').twitterParsing;
                
                // todo: $('.mediaembed').hide(); when medialink is empty
               
            }
            
        });
        
    }, 5000);

});