import cv2
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Load the image
img = cv2.imread('bee1.jpg')
img = img[-1000:,:1000]
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2GRAY)

height, width = img_gray.shape
row_Black_count = []
for row in range(1,height):
    black_Count = 0
    for px in range(1,width):
       if (img_gray[row,px] < 10):
        black_Count+=1
    row_Black_count.append(black_Count)
#print(row_Black_count)
row_Black_count_array=np.array(row_Black_count)
uniq_blackpxcount,freq_blakpxcount = np.unique(row_Black_count_array[row_Black_count_array > 100], return_counts=True)
#print('==================================================================\n These are the frequencies')
#print(np.asarray(((uniq_blackpxcount,freq_blakpxcount))))
blackpixeldf=pd.DataFrame({'blackpxcount':uniq_blackpxcount,'Frequency':freq_blakpxcount})
blackpixeldf=blackpixeldf.sort_values(by=['Frequency'],ascending=False)
print(blackpixeldf.head(20))
#plt.imshow(img_gray)
#plt.show()