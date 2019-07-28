#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 28 09:06:53 2019

@author: bruno
"""

import fitz


doc = fitz.open('Extra/Accounts.pdf') # open document
pages = len(doc) 
page = doc.loadPage(13)
links = page.getLinks()
text_dict = page.getText('dict')
text_blocks = [block for block in text_dict['blocks'] if block['type'] == 0] # Texts
img_block = [block for block in text_dict['blocks'] if block['type'] == 1] # Images



links= []
Raw_Extraction = []

for line in text_blocks:
    lines = line['lines']
    for chunk in lines:
        bbox = chunk['bbox']
        span = chunk['spans']
        for text in span:
            text = text['text']
            Raw_Extraction.append(text)

count = Raw_Extraction.count("www.")
counter = count + 1

for link in range(count):
    indexOfLastX = Raw_Extraction.index("www.")
    indexOfFirstY = Raw_Extraction.index("com")
    links.append(Raw_Extraction[indexOfLastX + 0:indexOfFirstY] + ["com"])
    Raw_Extraction.remove('www.')
    Raw_Extraction.remove('com')

print(links)
print(count)
