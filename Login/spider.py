#!/usr/bin/env python
import requests
import re
import urlparse

target_url = "http://10.0.2.11/mutillidae/"
target_links = []

def links(url):
    response = requests.get(url)
    return re.findall('(?:href=")(.*?)"', response.content)

def crawl(url):
    href_links = links(url)
    for link in href_links:
        link = urlparse.urljoin(url, link)

        if "#" in link:
            link = link.split("#")[0]

        if target_url in link and link not in target_links:
            target_links.append(link)
            print(link)
            crawl(link)

crawl(target_url)
