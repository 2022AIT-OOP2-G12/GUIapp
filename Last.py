import cv2
import pathlib
import numpy as np

input_dir = "images"
input_list = list(pathlib.Path(input_dir).glob('**/*.jpg'))

for i in range(len(input_list)):
    img_file_name = str(input_list[i])
    img_np = np.fromfile(img_file_name, dtype=np.uint8)
    img = cv2.imdecode(img_np, cv2.IMREAD_COLOR)
    g_hight, g_width, g_channel = img.shape

    sumg = 0
    sumb = 0
    sumr = 0

    for x in range(g_width):
            for y in range(g_hight):
                g, b, r = img[y, x]
                #print(vv_img[y, x, :])
                
            sumg = abs(g) + sumg
            sumb = abs(b) + sumb
            sumr = abs(r) + sumr
    
    print(sumg)
    print(sumb)
    print(sumr)

            
#cv2.imwrite('god2.jpeg', god_img)
