from .Book import Book
from PyPDF2 import PdfReader

class PDF_Manager(Book):
    def __init__(self, name: str, source_file):
        super().__init__(name)

        fin = open(source_file, "rb")
        self.__reader = PdfReader(fin)

    def __pre(self, text):
        return text.replace('\r', '').replace('\n', '#').replace('. ', '.') \
            .replace(', ', ',').replace(' .', '.').lower()

    def compile(self):
        num = 1
        for page in self.__reader.pages:
            _page = self.page(num, True)
            text = page.extract_text()
            text = self.__pre(text)
            # Kỹ thuật tách đoạn dùng ký tự đặc biệt
            for para in text.split('.#'):
                # Dòng lệnh này dùng để nối các dòng trong một đoạn
                para = para.replace('#', ' ')
                _page.paragraph(para)
            num += 1
            break