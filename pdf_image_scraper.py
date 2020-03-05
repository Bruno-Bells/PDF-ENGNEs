#import neccesary packages
import fitz
import random, string

# Extract images from a pdf file

doc = "Bruno.pdf" # path to pdf file
doc = fitz.open(doc)
pno = doc.loadPage(6)
text = pno.getText('dict')# dict format of the file
blocks = text["blocks"]
imgblocks = [b for b in blocks if b["type"] == 1]
textblocks = [t for t in blocks if t["type"] == 0]
x = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(16))

if imgblocks:
   for index, img in enumerate(imgblocks):
       img_name = "obinna_img/%s-%s.%s" % (x, index, img['ext'])
       with open(img_name, 'wb') as f:
            f.write(img['image'])
