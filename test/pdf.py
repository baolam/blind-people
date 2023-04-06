import sys
sys.path.append("./")

from src.book.PDF_Manager import PDF_Manager
from src.utils.my_queue import MyQueue
from src.book.Book import Book

pdf = PDF_Manager("Hàm EULER", "2.pdf")
pdf.compile()

def get_paragraph(book : Book, page_num : int, paragraph_num : int):
    return book.pages[page_num].paragraphs[paragraph_num]

# para_2 = get_paragraph(pdf, 1, 3).sentences

def _print(para : MyQueue):
    p = []
    while para.is_empty() == False:
        p.append(para.get())
        para.pop()
    print(p)

# _print(para_2)

from src.book.Manage import Manage
from src.sensor.Sound import Sound

sound = Sound()
manage = Manage(pdf, sound)

sound.service()

def end():
    sound.end_service = True
    sound.clear()
    print("Thoát chương trình")
    sys.exit(0)

try:
    while not manage.end_book:
        # Thiết bị đang có file âm thanh
        # Đang dùng dịch vụ
        # Vòng lặp dùng để duy trì dịch vụ
        while manage.state_from_sound():
            sound.play()
        manage.run()
    end()
except:
    end()
    
sound.clear()