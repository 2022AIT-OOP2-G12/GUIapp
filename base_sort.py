import numpy as np
import json

def Base_Sort(rr, gr, br):

    x = int(rr)
    y = int(gr)
    z = int(br)
    start = 1000000000000000000
            
    fg = 0
    fb = 0
    fr = 0

    img_name = ""

    j=0

    json_open = open('./Data/data_base.json', 'r')
    json_load = json.load(json_open)

    for v in json_load.values():
        #ここを変えました。
        x = int(rr)
        y = int(gr)
        z = int(br)
        path = str(v['path'])
        b = int(v['b'])
        g = int(v['g'])
        r = int(v['r'])
        wi = int(v['x'])
        hi = int(v['y'])

        x = x * wi * hi
        y = y * wi * hi
        z = z * wi *hi

        sumg = int(abs(g-y))
        sumb = int(abs(b-z))
        sumr = int(abs(r-x))
        sumall = int(sumg + sumb + sumr)

        if(start>=sumall):
            start = sumall
            fg = sumg
            fb = sumb
            fr = sumr
            img_name = str(path)

        # print(sumg)
        # print(y)
        # print(sumb)
        # print(z)
        # print(sumr)
        # print(x)
        # print(sumall)
        # print("----------------")
        # print(img_name)
        # print(path)
        # print(sumall)
        # print(start)
        # print("----------------")
        
        j=j+1
        
    data = {
        "path": str(img_name),
        'g': str(fg),
        'b': str(fb),
        'r': str(fr)
    }

    path2 = "./Data/data_out.json"
    json_file2 = open(path2, mode = "w")
    json.dump(data, json_file2, ensure_ascii=False)
    json_file2.close()

    with open('./Data/data_out.json') as f:
        jsn = json.load(f)

if __name__ == "__main__":
    Base_Sort(255,0,0)
