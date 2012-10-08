#!/usr/bin/python
# -*- coding: utf-8 -*-

# Title:    pinboard_today.py
# Author:   Sean Korzdorfer
# Date:     2012-10-05
#
# Prints a list of the urls of the days pinboard links formatted in Markdown
#
# NB: This is a script for a keyboard Maestro Macro

import pinboard
from datetime import date
import sys
import codecs

def contains(list, filter):
    for x in list:
        if filter(x):
            return True
    return False


# Set stdout to Unicode
sys.stdout = codecs.getwriter('utf8')(sys.stdout)

pinuser = "dogsolitude"
pinpasswd = "p7CAjT3ZqiveE"

# Create a day object for today
today = date.today()

# Connect to pinboard api
try:
    p = pinboard.open(pinuser, pinpasswd)

except (RuntimeError, TypeError, NameError):
    print 'Could not retrieve Pinboard links from the API'

# Get a list of dictionaries from pinboard api
todays_posts = p.posts(date=today)


# Print out only the key/value pairs we're interested in

for x in todays_posts:
    desc = '* [' + x['description'] + ']'
    url = '(' + x['href']+ ')'
    if contains(x['tags'], lambda y: y == u'\xa1'):
        print desc + url + " @2ndLook"
    else:
        print desc + url
    if x['extended']:
        print '    * ' + x['extended']