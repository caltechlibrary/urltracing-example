#!/usr/bin/env python3

# Import what we need in order to make our requests and track the responses
from urllib.request import Request, urlopen

def trace_url(url):
    req = Request(url)
    with urlopen(req) as response:
        # Our resolved url
        return url + ', ' + response.geturl()
    # We didn't move, e.g. the URL returned an error like a 404 or 401
    return url + ','

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
        print(trace_url(line))



