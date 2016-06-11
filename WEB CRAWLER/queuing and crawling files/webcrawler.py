# -*- coding: utf-8 -*-
"""
Created on Sat Jun 11 15:50:40 2016

# WEB CRAWLER
@author: akhgupta
"""

import os

#Each website you will crawl will be a seperate project
def create_project_dir(directory):
    if not os.path.exists(directory):
        print('Creating Project'+ directory)
        os.makedirs(directory)

#Create Queue and Crawled files
def create_data_files(project_name,base_url):
    queue= project_name + '/queue.txt'
    crawled= project_name + '/crawled.txt'
    
    if not os.path.isfile(queue):
        write_file (queue, base_url)
    if not os.path.isfile(crawled):
        write_file(crawled, '')

#Create a new file
def write_file(path,data):
    f=open(path,'w')
    f.write(data)
    f.close()
    