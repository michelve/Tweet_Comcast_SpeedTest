#!/usr/bin/python
import os
import sys
import csv
import datetime
import time
from twython import Twython

#################################
####      Installtion        ####
#################################
# install the following modules in terminal

        # pip install speedtest-cli
        # pip install twython
        # pip install python-oauth2
        # pip install python-twitter

# Change the data file location path in USER_DATA_FILE_PARH


def test():

        #run speedtest-cli
        print 'Running speed test. Please wait ...'

        a = os.popen("speedtest-cli --simple").read()

        print 'Speed test done.'

        lines = a.split('\n')
        print a
        ts = time.time()
        date =datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

        if "Cannot" in a:
                p = 100
                d = 0
                u = 0
        #extract the values for ping down and up values
        else:
                p = lines[0][6:11]
                d = lines[1][10:14]
                u = lines[2][8:12]
        print date,p, d, u

        #save the data to file for local network plotting
        USER_DATA_FILE_PARH="/path/to/data.csv"

        out_file = open(USER_DATA_FILE_PARH, 'a')
        writer = csv.writer(out_file)
        writer.writerow((ts*1000,p,d,u))
        out_file.close()

        # Enter your twitter app information here
        APP_KEY=""
        APP_SECRET=""
        OAUTH_TOKEN=""
        OAUTH_TOKEN_SECRET=""

        twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

        #try to tweet if speedtest couldn't connect.
        if "Cannot" in a:
                try:
                        tweet="Hey @Comcast @ComcastCares why is my internet down? I pay for 75down\\10up in Lake Worth FL? #comcastoutage #comcast"
                        twitter.update_status(status=tweet)
                except:
                        pass

        # send tweet if download speed is very slow
        elif eval(d)<50:
                print "Trying to tweet message. Please wait ..."
                try:
                        tweet="Hey @Comcast why is my internet speed " + str(int(eval(d))) + "down\\" + str(int(eval(u))) + "up when I pay for 75down\\10up in Lake Worth FL? @ComcastCares @xfinity #comcast #speedtest"
                        twitter.update_status(status=tweet)
                except Exception,e:
                        print str(e)
                        pass
        return

if __name__ == '__main__':
        test()
        print 'Task completed'
