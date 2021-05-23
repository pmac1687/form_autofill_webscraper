from bs4 import BeautifulSoup
from requests_html import HTMLSession
from urllib.parse import urljoin

session = HTMLSession()

def get_all_forms(url):
    """Returns all form tags found on a web page's `url` """
    # GET request
    res = session.get(url)
    # for javascript driven website
    # res.html.render()
    soup = BeautifulSoup(res.html.html, "html.parser")
    return soup.find_all("form")




if __name__ == "__main__":
    url = 'https://9milesmedia.com'
    forms = get_all_forms(url)
    for i in forms:
        #print(i)
        if 'class' in i.attrs:
            print(i['class'])