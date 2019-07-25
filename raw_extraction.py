# -*- coding: utf-8 -*-
"""
Created on Thu Jul 25 11:43:10 2019

@author: Bruno Odinukweze
"""
import fitz


doc = fitz.open('elysian.pdf') # open document
pages = len(doc) 
page = doc.loadPage(8)
text_dict = page.getText('dict')
text_blocks = [block for block in text_dict['blocks'] if block['type'] == 0] # Texts
img_block = [block for block in text_dict['blocks'] if block['type'] == 1] # Images


Raw_Extraction = []
for typ in text_blocks:
    for line in text_blocks:
        lines = line['lines']
        for chunk in lines:
            bbox = chunk['bbox']
            span = chunk['spans']
            for text in span:
                text = text['text']
                Raw_Extraction.append(text)

print(Raw_Extraction)