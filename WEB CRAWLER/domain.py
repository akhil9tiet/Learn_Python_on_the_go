# -*- coding: utf-8 -*-
"""
Created on Mon Jun 13 11:18:20 2016

@author: akhgupta
"""

from urllib.parse import urlparse   #Python3
#from urlparse import urlparse           #Python 2


# Get domain name (example.com)
def get_domain_name(url):
    try:
        results = get_sub_domain_name(url).split('.')
        return results[-2] + '.' + results[-1]
    except:
        return ''

# Get sub domain name (name.example.com)
def get_sub_domain_name(url):
    try:
        return urlparse(url).netloc
    except:
        return ''

