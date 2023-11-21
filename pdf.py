import PyPDF2

def extract_pages(input_path, output_path, start_page, end_page):
    with open(input_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        pdf_writer = PyPDF2.PdfWriter()

        # 循环从起始页到结束页
        for page_number in range(start_page - 1, end_page):
            print(page_number)
            page = pdf_reader.pages[page_number]
            pdf_writer.add_page(page)

        with open(output_path, 'wb') as output_file:
            pdf_writer.write(output_file)

# 示例用法：截取第3页到第5页
#input_file = r"D:\OneDrive - jxstnu.edu.cn\筆記\日語\N036 人教版高中必修1-3更新\日本語総まとめ N3 語彙. Nihongo So-matome N3 Vocabulary (佐々木 仁子, 松本 紀子, Hitoko Sasaki, Noriko Matsumoto) (Z-Library).pdf"
#input_file = r"E:\OneDrive - Cloud\book\24肖秀荣八套卷.pdf"
input_file = r"D:\OneDrive - jxstnu.edu.cn\筆記\計算機\考研c语言\c语言题库\【真题】灰灰考研C语言练习册A.pdf"
output_file = 'ha.pdf'
start_page = 53
end_page = 59
print("all done")
extract_pages(input_file, output_file, start_page, end_page)

