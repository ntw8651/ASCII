import inspect

#이미지 영상
import imutils
import cv2



#GUI
from tkinter import *
from tkinter import filedialog

#PIL
import PIL
from PIL import Image, ImageDraw, ImageFont

#그외
import os
import glob
import numpy as np
import textwrap
import natsort #pip install natsort






def trans2ascii(count, number):

    
    #img = cv2.imread("frame%d.jpg" % count, cv2.IMREAD_GRAYSCALE)
    img = cv2.cvtColor(count, cv2.COLOR_BGR2GRAY)
    img_small = cv2.resize(img, dsize=(64, 64), interpolation=cv2.INTER_LINEAR)
    #img_black = img_small.convert('L')


    pix = np.array(img_small)

    count=0
    ascii_image =[]
    ascii_list = ['@', 'O', 'o', '.']
    for row in pix:
        ascii_row = []
        for i in row:#음 어떻게 할가 
            if(i<=64):
                ascii_row.append(ascii_list[0])
            elif(i<=128):
                ascii_row.append(ascii_list[1])
            elif(i<=192):
                ascii_row.append(ascii_list[2])
            elif(i<=256):
                ascii_row.append(ascii_list[3])

            

        ascii_image.append(ascii_row)
    render_image = ''
    for i in ascii_image:
        render_image += str(''.join(i))+'\n'

    make_picture(ascii_image, number)


    #print(render_image)
    
    



def make_picture(text, number):
    image = Image.new("RGB", (640, 1090), color =(255,255,255))
    fnt = ImageFont.truetype("VeraMono.ttf", 17)
    
    textPosX = 0
    textPosY = 0
    count = 0

    text_info = []
    for i in text:
        text_info.append(str(''.join(i)))
                         
    dImage = ImageDraw.Draw(image)
    for p in text_info:
        dImage.text((textPosX,count*17), str(p), font=fnt, fill=(0, 0, 0))
        count+=1
    
    image.save('asciiImage\\'+str(number)+'.jpg')
    print('now:'+str(number))



#Get video
def select():
    global file_path
    file_path = filedialog.askopenfilename(parent=root,initialdir=os.getcwd(),title="선택해!!!!!")
    
    
def transVideo():
    video_url = file_path
    
    vidcap = cv2.VideoCapture(video_url)

    if not vidcap.isOpened():
        print('File open failed!')
        cap.release()
        sys.exit()

    number = 1

    while(vidcap.isOpened()):
        ret, image = vidcap.read()
        
        if(ret):
            global fps
            fps = vidcap.get(cv2.CAP_PROP_FPS)
            trans2ascii(image, number)
            number+=1
        else:
            break

def videoCreate(fps):
    img_array = []
    
    print()
    for filename in natsort.natsorted((glob.glob('asciiImage\*.jpg'))):

        img = cv2.imread(filename)
        height, width, layers = img.shape
        size = (width, height)
        img_array.append(img)

    out = cv2.VideoWriter('asciiVideo.avi', cv2.VideoWriter_fourcc(*'DIVX'), fps, (640, 1090))

    for i in range(len(img_array)):
        out.write(img_array[i])
    out.release()
    print("OK!!! File name is asciiVideo.avi")
    
#asdf = np.empty(shape, dtype=np.unit8)

fps = 30.0
#기본 fps
filepath = str()
root = Tk()




lbl = Label(root, text="input video")
lbl.pack()
btn = Button(root, text="select", command = select)
btn.pack()
btn = Button(root, text="Trans to Ascii", command = transVideo)
btn.pack()
btn = Button(root, text="Create Video", command = lambda: videoCreate(fps))
btn.pack()
root.mainloop()

#


#어쨋든 한 컷으로다가 저장이 되었으니깐 이걸 다시 영상으로 만드는 그런것도 있어야겠
    
#256 * 256의 문자열 리스트를?음... 일일히 한 128정도로?

#너로 정했
#일단 구현하고 줄이자
#일단 rgb를 다 나누면 좀 그러지니까
#rgb -> 흑백 -> 밝기에 따라 ASCII 대입 -> 출


#C:\Users\t\Desktop\어인야1.png
#0쪽이랑 256
