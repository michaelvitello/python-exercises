#------------1st Option, using urlib------------#

import urllib

def connected(host='http://google.com'):
    try:
        urllib.request.urlopen(host)
        return True
    except:
        return False

print( 'connected' if connected() else 'no internet!' )


#------------2nd Option WIP-------------------#
# Working (registering a ping) but can't find a way to display the string

# import os, sys

# if os.system("ping google.com") > 0:
#   print("Connected to the Internet")
# else:
#   print("Not connected to the Internet")

