from tkinter import filedialog

import PyPDF2

def extract_text_from_pdf(pdf_path):
    text = ""
    with open(pdf_path, "rb") as file:
        pdf_reader = PyPDF2.PdfReader(file)
        num_pages = len(pdf_reader.pages)

        for page_num in range(num_pages):
            page = pdf_reader.pages[page_num]
            text += page.extract_text()

    return text
def open_file_dialog():
    # 打开文件选择框
    file_path = filedialog.askopenfilename(title="选择文件")

    # 返回选择的文件路径
    return file_path
if __name__ == "__main__":
    pdf_path =open_file_dialog()
    extracted_text = extract_text_from_pdf(pdf_path)
    with open("qt.txt", "w", encoding="utf-8") as output_file:
        output_file.write(extracted_text)
    print(extracted_text)
