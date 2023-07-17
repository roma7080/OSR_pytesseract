from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = "C:/Program Files/Tesseract-ocr/tesseract.exe"

result = pytesseract.image_to_string(Image.open('C:/DriveD/temp/CodesList.jpeg'),lang='eng')

list = result.split('\n')
listnew = []

for item in list:
    listnew.append(item.split())

listnew.pop(0)

x=0
while x<len(listnew):
    if not listnew[x]:
        listnew.pop(x)
    x+=1

x=0
with open('C:/DriveD/temp/Lab/result.txt','w') as file:
    while x < len(listnew):
        file.write(listnew[x][0]+'    '+listnew[x][1]+'\n')
        x += 1
    file.truncate()