import requests
import re
from urllib.parse import urljoin

target_links = []
url_Adres = "http://google.com"


def get_links(url):
    try:
        if "http://" in url or "https://" in url:
            response = requests.get(url)
            return re.findall('(?:href=")(.*?)"', str(response.content))
        else:
            response = requests.get("http://" + url)
            return re.findall('(?:href=")(.*?)"', str(response.content))
    except requests.exceptions.ConnectionError:
        pass
    except requests.exceptions.InvalidSchema:
        pass
    except requests.exceptions.InvalidURL:
        pass
    except UnicodeError:
        pass


def crawl(url):
    href_links = get_links(url)
    if href_links:
        for link in href_links:
            link = urljoin(url, link)
            if "#" in link:
                link = link.split("#")[0]
            if url_Adres in link and link not in target_links:
                target_links.append(link)
                print("Crawler:" + link)
                crawl(link)


crawl(url_Adres)