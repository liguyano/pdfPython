import tkinter as tk
from tkinter import filedialog
import PyPDF2

def merge_pdfs(input_pdfs, output_pdf):
    pdf_merger = PyPDF2.PdfMerger()
    
    for pdf_file in input_pdfs:
        with open(pdf_file, 'rb') as pdf:
            pdf_merger.append(pdf)
    
    with open(output_pdf, 'wb') as output:
        pdf_merger.write(output)

def select_files():
    root = tk.Tk()
    root.withdraw()
    file_paths = filedialog.askopenfilenames(title="选择要合并的PDF文件", filetypes=[("PDF Files", "*.pdf")])
    return file_paths

if __name__ == "__main__":
    input_pdfs = select_files()
    
    if not input_pdfs:
        print("未选择任何文件，退出程序。")
    else:
        output_pdf = "merged_output.pdf"
        merge_pdfs(input_pdfs, output_pdf)
        print("PDF合并完成！")
