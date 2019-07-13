content = ""

def main(stop):
    for i in range(stop):
        with open(".\\text\\" + str(i) + ".txt", "r",encoding="utf-8") as f:
            content += f.read()
    with open("result.txt", "a", encoding="utf-8") as f:
        f.write(content)
        