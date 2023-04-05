from typing import List

from .Book import Book, Paragraph
from ..sensor.Sound import Sound
from ..utils.tts import tts
from ..utils.log import log


class Manage:
    def __init__(self, book : Book, sound : Sound):
        self.book = book
        self.sound = sound

        self.page_num = 1
        self.paragraph_num = 1
        self.__mem_finish = False
        self.end_book = False

        self.pages = {  }
        self.sound.update_fcallback(
            self.callback_finish_content
        )

        # Khởi tạo thông tin cần thiết
        self.initalize()
    
    def prepare(self) -> List[str]:
        # Kết quả trả về là tập các file âm thanh
        # Xây dựng tiền tố folder
        if self.should_tts():
            return self.get_sound_files()
        
        fold = '{}/{}'.format(self.page_num, self.paragraph_num)

        paragraph = self.get_paragraph()
        temp = []
        sound_files = []

        while paragraph.sentences.is_empty() == False:
            sen = paragraph.sentences.get()
            paragraph.sentences.pop()
            temp.append(sen)

            # Thêm file âm thanh
            sound_files.append(
                tts(sen, fold)
            )

        for sen in temp:
            paragraph.sentences.push(sen)
        
        return sound_files
    
    def should_tts(self) -> bool:
        return self.pages[self.page_num] \
            [self.paragraph_num]["tts"]

    def get_sound_files(self):
        return self.pages[self.page_num] \
            [self.paragraph_num]["sound_files"]
    
    def load_to_sound_service(self):
        # Tải file âm thanh vào dịch vụ chơi file âm thanh
        if self.should_tts() == False:
            self.pages[self.page_num] \
                [self.paragraph_num]["sound_files"] = self.prepare()
            self.pages[self.page_num] \
                [self.paragraph_num]["tts"] = True
            
        self.sound.content.lazy_update(
            self.prepare()
        )

    def initalize(self):
        for page_num, page_content in self.book.pages.items():
            temp = {  }
            for par_num, __ in page_content.paragraphs.items():
                temp[par_num] = {
                    "tts" : False,
                    "sound_files" : []
                }
            self.pages[page_num] = temp

    def run(self):
        # Gọi thủ tục này để đẩy nội dung vào dịch vụ
        if self.end_book:
            return
        
        self.load_to_sound_service()
        self.__mem_finish = True

    def get_paragraph(self) -> Paragraph:
        return self.book.pages[self.page_num].paragraphs[self.paragraph_num]

    def callback_finish_content(self):
        # Hàm này được gọi từ dịch vụ chơi âm thanh nhằm xác định kết thúc một gói âm
        if not self.__mem_finish:
            return

        m = len(self.pages)

        paragraphs = self.pages[self.page_num]
        n = len(paragraphs)

        if self.paragraph_num < n:
            log("Cập nhật đoạn")
            self.paragraph_num += 1        
        elif self.paragraph_num >= n:
            log("Cập nhật trang")
            self.page_num += 1
            self.paragraph_num = 1
        elif self.page_num == m:
            log("Hoàn thành")
            self.end_book = True
        
        self.__mem_finish = False
    
    def state_from_sound(self):
        # Trạng thái từ âm thanh
        # True nghĩa là đang trong quá trình hoạt động
        # False nghĩa là đã kết thúc
        return self.__mem_finish