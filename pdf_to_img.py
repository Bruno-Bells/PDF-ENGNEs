import os
import fitz 
import random, string


directory = os.fsencode("Dataset")

for file in os.listdir(directory):
     x = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(16))
     filename = os.fsdecode(file)
     try:
         if filename.endswith(".pdf"): 
             pdffile = 'Dataset/'+ filename
             output = os.path.splitext(filename)[0]
             doc = fitz.open(pdffile)
             for i in range(len(doc)):
                 page = doc.loadPage(i) #number of page
                 pix = page.getPixmap()
                 output_name = f"image_Dataset/{i}{output}{x}.png"
                 pix.writePNG(output_name)
     except RuntimeError:
        print(filename)
             
        continue
     else:
         continue
