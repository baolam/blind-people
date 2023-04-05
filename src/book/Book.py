from typing import List
from typing import Dict
from ..utils.my_queue import MyQueue


class Paragraph():
    def __init__(self):
        self.sentences = MyQueue()
    
    def add(self, sentences : List[str]):
        queue = MyQueue()
        for sentence in sentences:
            queue.push(sentence)
        self.sentences = queue


class Page():
    FILTER = '?.,!'
    def __init__(self):
        self.paragraphs : Dict[int, Paragraph] = { }
    
    def add(self, paragraph : Paragraph):
        self.paragraphs[len(self.paragraphs) + 1] = paragraph

    def get(self, num : int):
        return self.paragraphs[num]
    
    def paragraph(self, sentences : str):
        sentences = self.build_sens(sentences)
        paragraph = Paragraph()
        paragraph.add(sentences)
        self.add(paragraph)

    def build_sens(self, sentences : str):
        _res = [sentences]
        for char in Page.FILTER:
            _res = self.__char(_res, char)
        res = []
        for j in _res:
            if j != '':
                res.append(j)
        return res

    def __char(self, sentences : List[str], char : str):
        r = []
        for sentence in sentences:
            for _sentence in sentence.split(char):
                r.append(_sentence)
        return r

class Book():
    def __init__(self, name : str):
        self.name = name
        self.pages : Dict[int, Page] = {  }
    
    def add(self, page_num : int, page : Page):
        self.pages[page_num] = page 

    def page(self, page_num : int, allow_creating : bool = False) -> Page:
        # Tiến hành tạo trang khi chưa tồn tại và trả về trang được chỉ định
        _page = self.pages.get(page_num)
        if _page == None and allow_creating:
            self.pages[page_num] = Page()
            _page = self.pages[page_num]
        return _page
    
    def a_paragraph(self, page_num : int, paragraph : Paragraph):
        # Thêm một đoạn văn vào một trang được chỉ định
        page = self.page(page_num)
        page.add(paragraph)
    
# Cấp tổ chức quản lí
# Trang -> Đoạn -> Câu