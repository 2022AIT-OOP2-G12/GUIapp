import cv2
import pathlib
import numpy as np
import json

def Base():
            
    fg = 0
    fb = 0
    fr = 0

    input_dir = "static/images"
    input_list = list(pathlib.Path(input_dir).glob('**/*.jpg'))
    img_name = ""
    data_sum = {}
    j=0

    for i in range(len(input_list)):
        sumg = 0
        sumb = 0
        sumr = 0
        img_file_name = str(input_list[i])
        img_np = np.fromfile(img_file_name, dtype=np.uint8)
        img = cv2.imdecode(img_np, cv2.IMREAD_COLOR)
        g_hight, g_width, g_channel = img.shape
        print("---------------------------------------------------------")
        print(img_file_name)


        for m in range(g_width):
            for n in range(g_hight):
                color = img[n, m,:]
                b = color[0]
                g = color[1]
                r = color[2]
                        
                sumg = int(abs(g) + sumg)
                sumb = int(abs(b) + sumb)
                sumr = int(abs(r) + sumr)
                #print(abs(r-x))

        fg = sumg
        fb = sumb
        fr = sumr
        img_name = str(img_file_name)
        c = m * n
        print(fr/c)
        print(fg/c)
        print(fb/c)

        data_plus = {
        "path": str(img_name),
        'g': str(fg),
        'b': str(fb),
        'r': str(fr),
        'x': str(m),
        'y': str(n)
        }

        data_sum[j]=data_plus

        path2 = "./Data/data_base.json"
        json_file2 = open(path2, mode = "w")
        json.dump(data_sum, json_file2, ensure_ascii=False)
        json_file2.close()

        with open('./Data/data_base.json') as f:
            jsn = json.load(f)

        j=j+1

    #print(jsn["path"])
    #print(type(jsn["path"]))
    #cv2.imwrite('god2.jpeg', god_img)

if __name__ == "__main__":
    Base()
