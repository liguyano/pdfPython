import sys
import os
import easyocr

reader = easyocr.Reader(['ch_sim', 'en'])  # 加载模型，支持中文和英文


# result = reader.readtext('test.png')  # 读取图片
def prosess_bar(i, hint="progress:"):
    print("\r", end="")
    print("{0} {1:.2f}%: ".format(hint, i), "▋" * (int(i) // 2), end="")
    sys.stdout.flush()


if __name__ == '__main__':
    filenames = []
    open("out.txt", 'w', encoding='utf-8').close()
    for dirpath, dirnames, filenames in os.walk('./images'):
        print(len(filenames))
        length = len(filenames)
        for i, filename in enumerate(filenames):
            b = str(os.path.join(dirpath, filename)).replace('\\', '/')
            prosess_bar(i * 100 / len(filenames), "converted: ")
            result = reader.readtext(b)  # 读取图片
            with open("out.txt", 'a+', encoding='utf-8') as file:
                for x in range(len(result)):
                    file.write(result[x][1])
                    file.write("\n")
