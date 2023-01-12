import cv2
import pathlib
import numpy as np
import json

def Sort(r, g, b):

    x = int(r)
    y = int(g)
    z = int(b)

    start = 1000000000
            
    fg = 0
    fb = 0
    fr = 0

    sumg = 0
    sumb = 0
    sumr = 0

    count = 0

    input_dir = "images"
    input_list = list(pathlib.Path(input_dir).glob('**/*.jpg'))


    for i in range(len(input_list)):
        img_file_name = str(input_list[i])
        img_np = np.fromfile(img_file_name, dtype=np.uint8)
        img = cv2.imdecode(img_np, cv2.IMREAD_COLOR)
        g_hight, g_width, g_channel = img.shape


        for x in range(g_width):
            for y in range(g_hight):
                color = img[y, x,:]
                b = color[0]
                g = color[1]
                r = color[2]
                        #print(vv_img[y, x, :])
                        
                sumg = int(abs(g-y) + sumg)
                sumb = int(abs(b-z) + sumb)
                sumr = int(abs(r-x) + sumr)
                sumall = int(sumg + sumb + sumr)
            
        #print(sumg)
        #print(sumb)
        #print(sumr)
        #print(sumall)
        #print("----------------")

        if(start>sumall):
            start = sumall
            fg = sumg
            fb = sumb
            fr = sumr
            count = i

    data = {
        "path": str(input_list[count]),
        'g': str(fg),
        'b': str(fb),
        'r': str(fr)
    }

    path2 = "./Data/data.json"
    json_file2 = open(path2, mode = "w")
    json.dump(data, json_file2, ensure_ascii=False)
    json_file2.close()

    with open('./Data/data.json') as f:
        jsn = json.load(f)

    #print(jsn["path"])
    #print(type(jsn["path"]))
    #cv2.imwrite('god2.jpeg', god_img)

if __name__ == "__main__":
    Sort(200,200,200)
