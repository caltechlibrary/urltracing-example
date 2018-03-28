
# URL Tracing example

This is a quick and dirty tour of using Python 3's urllib to trace
a list of URLs through to their final redirected address.

## Assumptions

1. you have a file called *starting-urls.txt* with one url per line
2. you are going to output a CSV   list of "Starting URL" and "Final URL"
3. we are doing this with a simple Python 3 script called *urltracer.py*.

## The script

In this script we are using Python 3's urllib package. In particular we're
using two functions from it, _Request_ and _urlopen_.  The first function
formats a URL into a request object (e.g. req variable below) and the second
retrieves a result from the web where, if successful, we output the original
url and final url (i.e. the line with `response.geturl()`). If the response
is not successful then we just return a line with a starting URL and no 
final one.

The useful work is done with the `trace_url(url)` function. The rest of the script
is just looping through our list of URLs and writing the results out.

```python
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
```

## Running the demo

Create a file called *starting-urls.txt* with this content.

```text
    http://resolver.caltech.edu/CaltechAUTHORS:20151202-080822280
    http://resolver.caltech.edu/CaltechAUTHORS:20140805-091335567
    http://resolver.caltech.edu/CaltechAUTHORS:20151218-101224615
    http://resolver.caltech.edu/CaltechAUTHORS:20170726-063707920
    http://resolver.caltech.edu/CaltechAUTHORS:20160414-120131159
    http://resolver.caltech.edu/CaltechAUTHORS:20131105-094857416
    http://resolver.caltech.edu/CaltechAUTHORS:20160303-144825827
    http://resolver.caltech.edu/CaltechAUTHORS:20140710-094352199
    http://resolver.caltech.edu/CaltechAUTHORS:20141105-095608913
    http://resolver.caltech.edu/CaltechAUTHORS:20150701-133700441
```

```shell
    python3 urltracer.py > url-route.csv
```

Where *url-route.csv* looks something like

```csv
    Starting URL, Final URL
    http://resolver.caltech.edu/CaltechAUTHORS:20151202-080822280, https://authors.library.caltech.edu/62529/
    http://resolver.caltech.edu/CaltechAUTHORS:20140805-091335567, https://authors.library.caltech.edu/47962/
    http://resolver.caltech.edu/CaltechAUTHORS:20151218-101224615, https://authors.library.caltech.edu/63064/
    http://resolver.caltech.edu/CaltechAUTHORS:20170726-063707920, https://authors.library.caltech.edu/79370/
    http://resolver.caltech.edu/CaltechAUTHORS:20160414-120131159, https://authors.library.caltech.edu/66168/
    http://resolver.caltech.edu/CaltechAUTHORS:20131105-094857416, https://authors.library.caltech.edu/42246/
    http://resolver.caltech.edu/CaltechAUTHORS:20160303-144825827, https://authors.library.caltech.edu/65034/
    http://resolver.caltech.edu/CaltechAUTHORS:20140710-094352199, https://authors.library.caltech.edu/47131/
    http://resolver.caltech.edu/CaltechAUTHORS:20141105-095608913, https://authors.library.caltech.edu/51286/
    http://resolver.caltech.edu/CaltechAUTHORS:20150701-133700441, https://authors.library.caltech.edu/58741/
```

