# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 15:51:50 2023

@author: HP
"""
import cv2

data_b = "C:/Users/HP/Dallen/lab/thesis/Thesis_Me/b.png"
data_a = "C:/Users/HP/Dallen/lab/thesis/Thesis_Me/a.png"
video_path = 'C:/Users/HP/Dallen/lab/video/20221024/a/20273214_20221024_Hands_FingerTapping_L_L.mp4'

cap = cv2.VideoCapture(video_path)
if not cap.isOpened():
    print("Cannot open camera")
    exit()

target_frame_numbers = [1000, 1001]

for frame_number in target_frame_numbers:
    cap.set(cv2.CAP_PROP_POS_FRAMES, frame_number)
    ret, frame = cap.read()
    if not ret:
        print("Cannot receive frame")
        break
    cv2.imshow('oxxostudio_frame{}'.format(frame_number), frame)
    cv2.waitKey(0)
    # 构建保存文件的完整路径和文件名
    save_path = "C:/Users/HP/Dallen/lab/thesis/Thesis_Me/{}.png".format(frame_number)
    cv2.imwrite(save_path, frame)
    
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()

cv2.destroyAllWindows()


def Hash_Value(data):
    
    img = cv2.imread(data)
    img=cv2.resize(img,(8,8),interpolation=cv2.INTER_CUBIC)
    print(img)
    # img=cv2.resize(img,(200,200))
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    print(gray)
    cv2.imshow("img", img)
    cv2.imshow("gray", gray)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    ## =========== Total 為像素和初始值等於0 ===========
    Total = 0
    ahash_str = ''
    for i in range(8):                  #累加求像素之和
        for j in range(8):
            Total = Total + gray[i,j]
    avg = Total / 64                     #平均灰度
    print("avg = ",avg)
    ## =========== 灰度大於平均值為1；反之為0 ===========
    for i in range(8):                  
            for j in range(8):
                if  gray[i,j]>avg:
                    ahash_str=ahash_str+'1'
                else:
                    ahash_str=ahash_str+'0'
    print("ahash_str = ", ahash_str)
    return ahash_str

def cmpHash(hash1,hash2):              
    n=0                                #n表示漢明距離初始值為0
    if len(hash1)!=len(hash2):         #hash長度不同則返回-1代表傳參出錯
        return -1
    for i in range(len(hash1)):        #for迴圈逐一判斷
        if hash1[i]!=hash2[i]:         #不相等則n+1，最終為相似度
           n=n+1
    print(n)
    return n

# hash1 = Hash_Value(data_a)
# hash2 = Hash_Value(data_b)
# cmpHash(hash1,hash2)