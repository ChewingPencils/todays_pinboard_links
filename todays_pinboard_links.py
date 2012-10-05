#!/usr/bin/python
# Title:    pinboard_today.py
# Author:   Sean Korzdorfer
# Date:     2012-10-05
#
# Prints a list of the urls of the days pinboard links formatted in Markdown
#
# NB: This is a script for a keyboard Maestro Macro

# -*- coding: utf-8 -*-
import pinboard
from datetime import date
import sys
import codecs

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
    print '* [' + x['description'] + ']' + '(' + x['href']+ ')'
    if x['extended']:
        print '    * ' + x['extended']

