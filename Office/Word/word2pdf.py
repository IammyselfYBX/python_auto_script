# 将文件夹路径改成实际文件位置
# 把这个python文件放到里面运行
#
from win32com.client import Dispatch
from os import walk

wdFormatPDF = 17


def doc2pdf(input_file):
    word = Dispatch('Word.Application') # WPS改为Kwps.Application
    doc = word.Documents.Open(input_file)
    doc.SaveAs(input_file.replace(".doc", ".pdf"), FileFormat=wdFormatPDF)
    doc.Close()
    word.Quit()


if __name__ == "__main__":
    doc_files = []
    directory = "D:\\BaiduNetdiskDownload" #改成实际文件位置
    for root, dirs, filenames in walk(directory):
        for file in filenames:
            if file.endswith(".doc") or file.endswith(".docx"):
                doc2pdf(str(root + "\\" + file))

