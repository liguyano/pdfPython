import sys

import easyocr
reader = easyocr.Reader(['ch_sim', 'en'])  # 加载模型，支持中文和英文
#result = reader.readtext('test.png')  # 读取图片
def prosess_bar(i,hint="progress:"):
	print("\r", end="")
	print("{0} {1:.2f}%: ".format(hint,i), "▋" * (int(i) // 2), end="")
	sys.stdout.flush()
if __name__ == '__main__':
	for i in range(113):
			result = reader.readtext('images/{0}.png'.format(i))  # 读取图片
			prosess_bar(i * 100 / 113, "converted: ")
			with open("out.txt", 'a+',encoding='utf-8') as file:
				for x in range(len(result)):
					file.write(result[x][1])
					file.write("\n")






