###########################################################################

#                  

# This code uses the Y cordinates of the page to extract each row in a table and append them to a list

# The Y cordinate is the bbox[1]

# Created on 27th June, 2019. 
# @author: Bruno



###########################################################################

#import neccesary packages
import fitz
import numpy as np 
import json
import csv
import math
import codecs
from statistics import mode
from collections import Counter


doc = fitz.open('myfile.pdf') # open document
pages = len(doc) 
page = doc.loadPage(8)
text_dict = page.getText('dict')
text_blocks = [block for block in text_dict['blocks'] if block['type'] == 0] # Texts
img_block = [block for block in text_dict['blocks'] if block['type'] == 1] # Images

#convert the dict to a json file
# This is not necessary But can be useful in some ways
with open('data_to_json.json', 'w') as f:
    json.dump(text_blocks, f)
    print('good')



num_of_col = 5


# Declare the list variables

top_bbox = []
left_bbox = []
bottom_bbox = []
right_bbox = []

size_chunk = []

text_chunks = []
table_chunks = []

get_rows = []
row_index = []

row_chunks = []

Chunks_of_rows = []

# read the json file
with open('data_to_json.json', 'r') as data_file:
    text_data = json.load(data_file)

    # get the bounding boxes and X and Y cordinates of the of the texts(letters) in files
    for block in text_data:
        top = block['bbox'][0] 
        left = block['bbox'][1] # Y
        bottom = block['bbox'][2] # X
        right = block['bbox'][3]
   
        top_bbox.append(top)
        left_bbox.append(left)
        bottom_bbox.append(bottom)
        right_bbox.append(right)

        top_bbox.sort()
        left_bbox.sort()
        bottom_bbox.sort()
        right_bbox.sort()

        print(left)
# get the text sizes
for line in text_blocks:
    lines = line['lines']
    for chunk in lines:
        bbox = chunk['bbox']
        span = chunk['spans']
        for size in span:
            text = size['size']
            size_chunk.append(text) 

# get the  size mode
size_mode = mode(size_chunk)
# print(size_mode)

def get_text_chunks():
    # This function Extractes only the Texts in a page
# get Chunk of texts
    for line in text_blocks:
        lines = line['lines']
        for chunk in lines:
            bbox = chunk['bbox']
            span = chunk['spans']
            # print(span)
            for size in span:
                sizes = size['size']
                if sizes > size_mode or sizes < size_mode:
                    for text in span:
                        text = text['text']
                        text_chunks.append(text)
get_text_chunks()
# This function Extracts the Tables in a page
# print(text_chunks)
def get_table_chunks():
    
    for line in text_blocks:
        lines = line['lines']
        for chunk in lines:
            bbox = chunk['bbox']
            span = chunk['spans']
            # print(span)
            for size in span:
                sizes = size['size']
                if sizes == size_mode:
                    for table in span:
                        table = table['text']
                        table_chunks.append(table)
get_table_chunks()

# get rows using the Y cordinates
for line in text_blocks:
        lines = line['lines']
        for chunk in lines:
            bbox = chunk['bbox']
            span = chunk['spans']
            row = bbox[1]
            row_chunks.append(row)

# The Y cordinates
row_chunk = Counter(row_chunks)        
for k,v in row_chunk.items():
    # print(k,v)
    pass
len_of_data = (len(row_chunk))
print(len_of_data)


for i in row_chunk:
    get_rows.append(i)

# append the rows into chunks and seperate them
# These rows are more than necessary for a page so that there won't be a case were they are not enough

rows1, rows2, rows3, rows4, rows5, rows6, rows7, rows8, rows9, rows10 = ([] for i in range(10))

rows11, rows12, rows13, rows14, rows15, rows16, rows17, rows18, rows19, rows20 = ([] for i in range(10))

rows21, rows22, rows23, rows24, rows25, rows26, rows27, rows28, rows29, rows30 = ([] for i in range(10))

rows31, rows32, rows33, rows34, rows35, rows36, rows37, rows38, rows39, rows40 = ([] for i in range(10))

rows41, rows42, rows43, rows44, rows45, rows46, rows47, rows48, rows49, rows50 = ([] for i in range(10))

rows51, rows52, rows53, rows54, rows55, rows56, rows57, rows58, rows59, rows60 = ([] for i in range(10))

rows61, rows62, rows63, rows64, rows65, rows66, rows67, rows68, rows69, rows70 = ([] for i in range(10))

rows71, rows72, rows73, rows74, rows75, rows76, rows77, rows78, rows79, rows80 = ([] for i in range(10))

rows81, rows82, rows83, rows84, rows85, rows86, rows87, rows88, rows89, rows90 = ([] for i in range(10))

rows91, rows92, rows93, rows94, rows95, rows96, rows97, rows98, rows99, rows100 = ([] for i in range(10))

rows101, rows102, rows103, rows104, rows105, rows106, rows107, rows108, rows109, rows110 = ([] for i in range(10))

# compare to see if any Y cordinate match with the text in the text_block
def get_table_rows(row_indexes, row_list):
    for line in text_blocks:
        lines = line['lines']
        # print(lines)
        for chunk in lines:
            bbox = chunk['bbox']
            try:
                if row_indexes == chunk['bbox'][1]:
                    span = chunk['spans']
                    # print(span)
                    for size in span:
                        sizes = size['size']
                        if sizes == size_mode:
                            for table in span:
                                table = table['text']
                                row_list.append(table)
            except(IndexError, TypeError):
                print('Opps!')
    return

# Run the function Code
def Extractor():
    try:

        get_table_rows(get_rows[1], rows1)
        get_table_rows(get_rows[2], rows2)
        get_table_rows(get_rows[3], rows3)
        get_table_rows(get_rows[4], rows4)
        get_table_rows(get_rows[5], rows5)
        get_table_rows(get_rows[6], rows6)
        get_table_rows(get_rows[7], rows7)
        get_table_rows(get_rows[8], rows8)
        get_table_rows(get_rows[9], rows9)
        get_table_rows(get_rows[10], rows10)
        get_table_rows(get_rows[11], rows11)
        get_table_rows(get_rows[12], rows12)
        get_table_rows(get_rows[13], rows13)
        get_table_rows(get_rows[14], rows14)
        get_table_rows(get_rows[15], rows15)
        get_table_rows(get_rows[16], rows16)
        get_table_rows(get_rows[17], rows17)
        get_table_rows(get_rows[18], rows18)
        get_table_rows(get_rows[19], rows19)
        get_table_rows(get_rows[20], rows20)
        get_table_rows(get_rows[21], rows21)
        get_table_rows(get_rows[22], rows22)
        get_table_rows(get_rows[23], rows23)
        get_table_rows(get_rows[24], rows24)
        get_table_rows(get_rows[25], rows25)
        get_table_rows(get_rows[26], rows26)
        get_table_rows(get_rows[27], rows27)
        get_table_rows(get_rows[28], rows28)
        get_table_rows(get_rows[29], rows29)
        get_table_rows(get_rows[30], rows30)
        get_table_rows(get_rows[31], rows31)
        get_table_rows(get_rows[32], rows32)
        get_table_rows(get_rows[33], rows33)
        get_table_rows(get_rows[34], rows34)
        get_table_rows(get_rows[35], rows35)
        get_table_rows(get_rows[36], rows36)
        get_table_rows(get_rows[37], rows37)
        get_table_rows(get_rows[38], rows38)
        get_table_rows(get_rows[39], rows39)
        get_table_rows(get_rows[40], rows40)
        get_table_rows(get_rows[41], rows41)
        get_table_rows(get_rows[42], rows42)
        get_table_rows(get_rows[43], rows43)
        get_table_rows(get_rows[44], rows44)
        get_table_rows(get_rows[45], rows45)
        get_table_rows(get_rows[46], rows46)
        get_table_rows(get_rows[47], rows47)
        get_table_rows(get_rows[48], rows48)
        get_table_rows(get_rows[49], rows49)
        get_table_rows(get_rows[50], rows50)
        get_table_rows(get_rows[51], rows51)
        get_table_rows(get_rows[52], rows52)
        get_table_rows(get_rows[53], rows53)
        get_table_rows(get_rows[54], rows54)
        get_table_rows(get_rows[55], rows55)
        get_table_rows(get_rows[56], rows56)
        get_table_rows(get_rows[57], rows57)
        get_table_rows(get_rows[58], rows58)
        get_table_rows(get_rows[59], rows59)
        get_table_rows(get_rows[60], rows60)
        get_table_rows(get_rows[61], rows61)
        get_table_rows(get_rows[62], rows62)
        get_table_rows(get_rows[63], rows63)
        get_table_rows(get_rows[64], rows64)
        get_table_rows(get_rows[65], rows65)
        get_table_rows(get_rows[66], rows66)
        get_table_rows(get_rows[67], rows67)
        get_table_rows(get_rows[68], rows68)
        get_table_rows(get_rows[69], rows69)
        get_table_rows(get_rows[70], rows70)
        get_table_rows(get_rows[71], rows71)
        get_table_rows(get_rows[72], rows72)
        get_table_rows(get_rows[73], rows73)
        get_table_rows(get_rows[74], rows74)
        get_table_rows(get_rows[75], rows75)
        get_table_rows(get_rows[76], rows76)
        get_table_rows(get_rows[77], rows77)
        get_table_rows(get_rows[78], rows78)
        get_table_rows(get_rows[79], rows79)
        get_table_rows(get_rows[80], rows80)
        get_table_rows(get_rows[81], rows81)
        get_table_rows(get_rows[82], rows82)
        get_table_rows(get_rows[83], rows83)
        get_table_rows(get_rows[84], rows84)
        get_table_rows(get_rows[85], rows85)
        get_table_rows(get_rows[86], rows86)
        get_table_rows(get_rows[87], rows87)
        get_table_rows(get_rows[88], rows88)
        get_table_rows(get_rows[89], rows89)
        get_table_rows(get_rows[90], rows90)
        get_table_rows(get_rows[91], rows91)
        get_table_rows(get_rows[92], rows92)
        get_table_rows(get_rows[93], rows93)
        get_table_rows(get_rows[94], rows94)
        get_table_rows(get_rows[95], rows95)
        get_table_rows(get_rows[96], rows96)
        get_table_rows(get_rows[97], rows97)
        get_table_rows(get_rows[98], rows98)
        get_table_rows(get_rows[99], rows99)
        get_table_rows(get_rows[100], rows100)
        get_table_rows(get_rows[101], rows101)
        get_table_rows(get_rows[102], rows102)
        get_table_rows(get_rows[103], rows103)
        get_table_rows(get_rows[104], rows104)
        get_table_rows(get_rows[105], rows105)
        get_table_rows(get_rows[106], rows106)
        get_table_rows(get_rows[107], rows107)
        get_table_rows(get_rows[108], rows108)
        get_table_rows(get_rows[109], rows109)
        get_table_rows(get_rows[110], rows110)
    except :
        pass

    return

Extractor()

# Joining all the extracted rows to one list to remove the empty ones
Splited_rows = [rows1, rows2, rows3, rows4, rows5, rows6, rows7, rows8, rows9, rows10, rows11, rows12, rows13, rows14, rows15,
                rows16, rows17, rows18, rows19, rows20, rows21, rows22, rows23, rows24, rows25, rows26, rows27, rows28, rows29, rows30,
                rows31, rows32, rows33, rows34, rows35, rows36, rows37, rows38, rows39, rows40, rows41, rows42, rows43, rows44, rows45,
                rows46, rows47, rows48, rows49, rows50, rows51, rows52, rows53, rows54, rows55, rows56, rows57, rows58, rows59, rows60,
                rows61, rows62, rows63, rows64, rows65, rows66, rows67, rows68, rows69, rows70, rows71, rows72, rows73, rows74, rows75,
                rows76, rows77, rows78, rows79, rows80, rows81, rows82, rows83, rows84, rows85, rows86, rows87, rows88, rows89, rows90,
                rows91, rows92, rows93, rows94, rows95, rows96, rows97, rows98, rows99, rows100, rows101, rows102, rows103, rows104, 
                rows105, rows106, rows107, rows108, rows109, rows110


]


# remove empty rows
Extracted_row = list(filter(None, Splited_rows))

# See the output
for i in Extracted_row:
    print(i)



