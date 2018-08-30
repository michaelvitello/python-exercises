import urllib

def connected(host='http://google.com'):
    try:
        urllib.request.urlopen(host)
        return True
    except:
        return False

print( 'connected' if connected() else 'no internet!' )

# Working but not displaying the right message

# import os, sys

# if os.system("ping google.com") > 0:
#   print("Connected to the Internet")
# else:
#   print("Not connected to the Internet")

