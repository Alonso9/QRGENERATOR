#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
Python program to create qr codes, using qrcode and pillow 
'''

import qrcode
from PIL import Image


#Creating QR code:
text = input("Introduce the text to make QR code: ")
image = qrcode.make(text)

#Generating the image:
imageName = input("Introduce the image name without extension: ") + '.png'

imageFile = open(imageName, 'wb')

#Save the QR image
image.save(imageFile)

#Close the QR image
imageFile.close()

#Open image
sourceimage = './' + imageName
Image.open(sourceimage).show()

