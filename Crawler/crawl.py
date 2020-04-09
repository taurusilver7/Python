#!/usr/bin/env python
import requests


def request(url):
    try:
        return requests.get("https://" + url)
    except requests.exceptions.ConnectionError:
        pass


target_url = "10.0.2.11/phpMyAdmin/"

with open("/root/Downloads/wordlist.txt", "r") as wordlist_file:
    for line in wordlist_file:
        word = line.strip()
        test_url = target_url + "/" + word
        response = request(test_url)
        if response:
            print("[+] Discovered URL >> " + test_url)