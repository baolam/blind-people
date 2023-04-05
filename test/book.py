import sys
sys.path.append("./")

from src.book.Book import *

tren_hanh_trinh_tu_hoc = Book("Trên hành trình tự học")
page_1 = tren_hanh_trinh_tu_hoc.page(1, True)
page_1.paragraph("Đầu tiên, tôi xin gửi đến bạn một lời cảm ơn, vì đã chọn đọc quyển sách này thay vì vô vàn những quyển sách khác, trong cách cửa tiệm sách, và trên cả giá sách nhà bạn")
page_1.paragraph("Độc giả thân mến, điều gì đã đưa bạn đến với quyển sách này? Khi viết lời nói đầu, tôi đang tò mò tự hỏi người đọc quyển sách này sẽ là ai.")

page_2 = tren_hanh_trinh_tu_hoc.page(2, True)
page_2.paragraph("Ban đầu, tôi khởi sự bằng việc đọc sách chuyên cần trở lại.")
page_2.paragraph("Lấy đó làm động lực, tôi dần sử dụng việc tự học làm công cụ để phát triển chính mình. Tôi bước chân dần ra thế giới, tìm hiểu cuộc sống và phong tục của những vùng miền, dân tộc khác nhau.")

print(tren_hanh_trinh_tu_hoc.pages)
print(page_1.paragraphs)
print(page_2.paragraphs)

print(page_1.paragraphs[1].sentences)
print(page_1.paragraphs[2].sentences)

print(page_1.paragraphs[1].sentences.get())
print(page_1.paragraphs[2].sentences.get())