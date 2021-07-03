from PIL import Image
import imutils

import os
import numpy as np
import cv2





def trans2ascii(count):

    
    #img = cv2.imread("frame%d.jpg" % count, cv2.IMREAD_GRAYSCALE)
    img = cv2.cvtColor(count, cv2.COLOR_BGR2GRAY)
    img_small = cv2.resize(img, dsize=(80, 80), interpolation=cv2.INTER_LINEAR)
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
video_url = input("경로를 내놔")
vidcap = cv2.VideoCapture(video_url)
#fourcc = cv2.VideoWriter_fourcc(*'MP4V')

#cv2.VideoWriter("reduce_video.mp4", fourcc, 10.0,(64, 64), False)

#vidcap = cv2.VideoCapture("reduce_video.mp4")

if not vidcap.isOpened():
    print('File open failed!')
    cap.release()
    sys.exit()

count = int(0)

while(vidcap.isOpened()):

    ret, image = vidcap.read()
    
    if(ret):
        #resize_image = imutils.resize(image, width=64, height=64)
        #gray = cv2.cvtColor(resize_image, cv2.COLOR_BGR2GRAY)

        #cv2.imwrite("frame%d.jpg" % count, image)

        trans2ascii(image)
        

    #cv2.imwrite("\images\fream"+(count)+".jpg", image)
    #print('asdf')
        count+=1
        
    else:
        break





#어쨋든 한 컷으로다가 저장이 되었으니깐 이걸 다시 영상으로 만드는 그런것도 있어야겠
    
#256 * 256의 문자열 리스트를?음... 일일히 한 128정도로?

#너로 정했
#일단 구현하고 줄이자
#일단 rgb를 다 나누면 좀 그러지니까
#rgb -> 흑백 -> 밝기에 따라 ASCII 대입 -> 출


#C:\Users\t\Desktop\어인야1.png
#0쪽이랑 256
