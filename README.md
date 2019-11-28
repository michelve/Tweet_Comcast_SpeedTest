# Installation

### install the following modules in terminal
    open terminal and run the following
        pip install speedtest-cli
        pip install twython
        pip install python-oauth2
        pip install python-twitter

### open the script and change the following:
    remember to create the file data.csv
    enter the full path to that file in USER_DATA_FILE_PATH

## How to use
open terminal and run the following 'python /path/to/comcast_speedtest_twitter.py'


## How create a Cron Job and run it automatically
 1. open terminal and type 'crontab -e'
 2. Copy and edit the following (no spaces) --->  5 * * * * /usr/bin/python /path/to/script/comcast_speedtest_twitter.py


credits: I did some edits based on this script - https://gist.github.com/spiermar/37d6e41aa787a70f006d
