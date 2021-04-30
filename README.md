# Website Blocker

This is a very helpful program for students who want to focus on their studies and don’t want any other distractions like social media.

**Note:** This program only runs on **windows**!

## Host file
A hosts file which is used by operating systems to map a connection between an IP address and domain names before going to domain name servers. This file is a simple text file with the mapping of IPs and domain names.


## How do we block websites?

Every operating system has a host file and it’s on this file where we are going to add a list of websites we want to block by redirecting them to 127.0.0.1 (localhost).

We will add website URLs to the host file and mapping them to the localhost thus preventing you from accessing the real site during working hours.

Instead of adding `www.facebook.com` we are going to add `127.0.0.1 www.facebook.com`, therefore whenever a user tries to access the website during working hours will be directed to the localhost.

Therefore we need to add those sites to the host files during working hours and removing them immediately when it’s going home time.


## Pre requisites

- [Python](https://www.python.org/downloads/) - 3.8.4 or up


## Run

- Download the project, open terminal window as **ADMIN** and go to folder with 'web?blocker.py' and type:

```
python web_blocker.py
```

You will be prompt to say yes (you do want to block websites) or not (it will unblock all websites).

