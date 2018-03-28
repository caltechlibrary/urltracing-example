
# URL Tracing example

This is a quick and dirty tour of using Python 3's urllib to trace
a list of URLs through to their final redirected address.

## Assumption

1. you have a file called *starting-urls.txt* with one url per line
2. you are going to output a CSV formated list of starting url and final url
3. we are doing this with a simple Python 3 script.

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

