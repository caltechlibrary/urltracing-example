#!/usr/bin/env python3

# Import what we need in order to make our requests and track the responses
from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError

def trace_url(url):
    req = Request(url)
    response = None
    status_code = ""
    reason = ""
    final_url = ""
    try: 
        response = urlopen(req)
        finalURL = response.geturl()
        status_code = str(response.status)
    except HTTPError as e:
        status_code = str(e.code)
    except URLError as e:
        status_code = str(e.reason)

    return url + ',' + final_url + ', ' + status_code

#
# Main workflow
#

# Read in the list of URLs to track from a file called "starting-urls.txt"
with open('starting-urls.txt', mode = 'r', encoding = 'utf-8') as f:
    src = f.read()

# Split "src" into a list of urls, one per line
print("Starting URL, Final URL")
for line in src.split('\n'):
    if len(line) > 0:
        print(trace_url(line.strip()))



