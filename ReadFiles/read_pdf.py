from io import StringIO
from urllib.request import urlopen
from pdfminer.pdfinterp import PDFResourceManager, process_pdf
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams


def readPDF(pdfFile):
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, laparams=laparams)

    process_pdf(rsrcmgr, device, pdfFile)
    device.close()

    content = retstr.getvalue()
    retstr.close()
    return content


# 웹 상의 PDF 문서 읽기
url = 'http://pythonscraping.com/pages/warandpeace/chapter1.pdf'
pdfFile = urlopen(url)
# pdfFile = open('./warandpeace.pdf', 'rb')  # 로컬 파일의 경우
outputString = readPDF(pdfFile)
print(outputString)
pdfFile.close()
