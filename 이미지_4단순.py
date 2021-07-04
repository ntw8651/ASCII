from PIL import Image
import imutils
from tkinter import *
from tkinter import filedialog
import os
import numpy as np
import cv2


def trans2ascii(count):

    
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



    print(render_image)



    

#Get video
def select():
    global file_path
    file_path = filedialog.askopenfilename(parent=root,initialdir="/",title="선택해!!!!!")
    
    
def transVideo():
    video_url = file_path
    
    vidcap = cv2.VideoCapture(video_url)

    if not vidcap.isOpened():
        print('File open failed!')
        cap.release()
        sys.exit()


    while(vidcap.isOpened()):
        ret, image = vidcap.read()
        
        if(ret):
            trans2ascii(image)
        else:
            break



filepath = str()
root = Tk()



lbl = Label(root, text="input video")
lbl.pack()
btn = Button(root, text="select", command = select)
btn.pack()
btn = Button(root, text="trans", command = transVideo)
btn.pack()

root.mainloop()




#어쨋든 한 컷으로다가 저장이 되었으니깐 이걸 다시 영상으로 만드는 그런것도 있어야겠
    
#256 * 256의 문자열 리스트를?음... 일일히 한 128정도로?

#너로 정했
#일단 구현하고 줄이자
#일단 rgb를 다 나누면 좀 그러지니까
#rgb -> 흑백 -> 밝기에 따라 ASCII 대입 -> 출


#C:\Users\t\Desktop\어인야1.png
#0쪽이랑 256
