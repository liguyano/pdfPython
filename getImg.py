import fitz
import tkinter as tk
from tkinter import filedialog
def pdf_image(pdfPath, imgPath, zoom_x, zoom_y, rotation_angle):
    # 打开PDF文件
    pdf = fitz.open(pdfPath)
    # 逐页读取PDF
    for pg in range(0, pdf.page_count):
        page = pdf[pg]
        # 设置缩放和旋转系数
        trans = fitz.Matrix(zoom_x, zoom_y).prerotate(rotation_angle)
        pm = page.get_pixmap(matrix=trans, alpha=False)
        # 开始写图像
        pm._writeIMG(imgPath + str(pg) + ".png",format=1,jpg_quality=100)
    pdf.close()
def select_files():
    root = tk.Tk()
    root.withdraw()
    file_paths = filedialog.askopenfilenames(title="选择要提取的PDF文件", filetypes=[("PDF Files", "*.pdf")])
    return file_paths
input_file=select_files()
print("filename:{}".format(str(input_file)))
pdf_image(input_file[0]
          , r"images/", 10, 10, 0)
