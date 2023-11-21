import re

if __name__ == '__main__':
    conut = 0
    with (open("out.txt", 'r+', encoding='utf-8') as readFile,
          open("oo.txt", 'w+', encoding='utf-8') as outFile):
        line1 = "  "
        li = 0
        while li < 4351:
            li += 1
            line1 = readFile.readline()
            line1 = line1.replace("\n", "")
            line1 = line1.replace("获取后续课程更新","")
            if re.match(r'^[A-Za-z0-9()]', line1):
                outFile.write("\n")
                conut = 0
            elif conut > 2:
                outFile.write("\n")
                conut = 0
            elif "公众号" in line1 or "考研上岸" in line1:
                continue
            conut += 1
            outFile.write(line1)
            print(line1, end="")
