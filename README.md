# HTMLParser
Basic web scraping and HTML parsing using BeautifulSoup in Python


## Installing the BeautifulSoup
For the Debian or Ubuntu Linux, we can install like below:
```
$ apt-get install python2-bs4 #python2
$ apt-get install python3-bs4 #python3
```
Or, we can install using pip like:

```
$ pip2 install bs4 #python2
$ pip3 install bs4 #python3
```

## Installing the urllib
We can install using pip as follows:
```
$ pip2 install urllib #python2
$ pip3 install urllib #python3
```
## Loading the HTML Page
To load the URL page as an HTML file, we have to use the code snippets.
```
html_file = urllib.request.urlopen(self.url).read()
```
### Making the HTML Soup
After loading the HTML file, we have to make the soup using BeautifulSoup. Let's use the following code for it.
```
html_soup = BeautifulSoup(html_file, 'html.parser')
```
