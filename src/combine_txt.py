import os

def main(stop):
    content = ""
    res = ""
    for i in range(stop):
        if os.path.isfile(".\\text\\" + str(i) + ".txt"):
            with open(".\\text\\" + str(i) + ".txt", "r",encoding="utf-8") as f:
                res = f.read()
                if res.endswith("转换失败！"):
                    content += "\n"
                    content += res
                    content += "\n"
                else:
                    content += res
        else:
            content += "\n"
            content += str(i) + "转换失败！"
            content += "\n"
            
    with open("result.txt", "a", encoding="utf-8") as f:
        f.write(content)

if __name__ == "__main__":
    stop = int(input("输入文件数目："))
    main(stop)
        