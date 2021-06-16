from bs4 import BeautifulSoup
import urllib.request

class HTMLParser:
    
    def __init__(self, url=None):
        self.url = url
    
    def get_html(self):
        html_file = None
        try:
            html_file = urllib.request.urlopen(self.url).read()
        except:
            print("Error in get_html()! Check the URL.")
        return html_file

    def get_soup(self, html_file):
        html_soup = None
        try:
            html_soup = BeautifulSoup(html_file, 'html.parser')
        except:
            print("Exception in get_soup()! Check the html_file.")
        return html_soup

def print_top_available_stackoverflow_job_posts(html_soup, selector_head, selector_tail):
    post_count = 0
    
    try:
        for i in range(1, 11):
            try:
                selector = selector_head + str(i) + selector_tail
                job_post_html = html_soup.select(selector)[0]
                job_post_soup = HTMLParser().get_soup(str(job_post_html))
                job_title = job_post_soup.a['title']
                print(job_title)
                post_count +=1
            except:
                pass
    except:
        pass

    return post_count

if __name__ == '__main__':
    url = 'https://stackoverflow.com/jobs'
    html_parser = HTMLParser(url)
    html_file = html_parser.get_html()
    html_soup = html_parser.get_soup(html_file)

    selector_head = '#content > div.js-search-container.search-container.mbn24 > div > div.grid--cell.fl1.br.bc-black-2 > div > div.listResults > div:nth-child('
    selector_tail = ') > div:nth-child(2) > div.grid--cell.fl1 > h2 > a'
    post_count = print_top_available_stackoverflow_job_posts(html_soup, selector_head, selector_tail)
    print("Total Available Job Post in First Page: ", post_count)
