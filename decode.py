import cv2
from pyzbar.pyzbar import decode

img = cv2.imread('2.png')
code = decode(img)

for barcode in decode(img) : 
    Data = barcode.data.decode('utf-8')
    print("Decode QR code : " + Data)