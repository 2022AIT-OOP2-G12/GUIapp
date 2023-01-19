import cv2
import pathlib
import numpy as np
import json

def Sort(r, g, b):
    start = 1000000000000000000
            
    fg = 0
    fb = 0
    fr = 0

    input_dir = "static/images"
    input_list = list(pathlib.Path(input_dir).glob('**/*.jpg'))
    img_name = ""

    for i in range(len(input_list)):
        sumall = 0
        sumg = 0
        sumb = 0
        sumr = 0
        img_file_name = str(input_list[i])
        img_np = np.fromfile(img_file_name, dtype=np.uint8)
        img = cv2.imdecode(img_np, cv2.IMREAD_COLOR)
        g_hight, g_width, g_channel = img.shape


        for m in range(g_width):
            for n in range(g_hight):
                color = img[n, m,:]
                b = color[0]
                g = color[1]
                r = color[2]
                #print(img[n, m,:])
                        
                sumg = int(abs(g-y) + sumg)
                sumb = int(abs(b-z) + sumb)
                sumr = int(abs(r-x) + sumr)
                sumall = int(sumg + sumb + sumr)
                #print(abs(r-x))
            
        # print(sumg)
        # print(y)
        # print(sumb)
        # print(z)
        # print(sumr)
        # print(x)
        # print(sumall)
        # print("----------------")

        if(start>=sumall):
            start = sumall
            fg = sumg
            fb = sumb
            fr = sumr
            img_name = str(img_file_name)
        # print(img_name)
        # print(img_file_name)
        # print(sumall)
        # print(start)
        # print("----------------")
    data = {
        "path": str(img_name),
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
    Sort(34,34,34)
    print("----------------")
    print("----------------")
    print("----------------")
    Sort(204,0,0)
