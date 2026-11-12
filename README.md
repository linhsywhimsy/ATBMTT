# Bài tập lớn: Hệ mã A5/1 và TinyA5/1

## Giới thiệu

Bài tập lớn môn *An toàn và Bảo mật Thông tin*. Nhóm cài đặt hệ mã dòng *A5/1* (dùng trong mạng 2G GSM) và phiên bản thu nhỏ *TinyA5/1* (dùng cho mục đích giảng dạy).

## Cấu trúc thư mục

```text
ATBMTT/
├── core/
│   ├── __init__.py
│   ├── tiny_a5_1.py      # Thuật toán TinyA5/1
│   ├── a5_1.py           # Thuật toán A5/1 tổng quát
│   └── utils.py          # Hàm chuyển đổi text/file <-> bit
├── test/
│   ├── __init__.py
│   └── test_all.py       # Bộ kiểm thử
├── main.py               # Điểm khởi chạy
├── cli.py                # Giao diện dòng lệnh
├── demo_attack.py        # Minh họa tấn công vét cạn
├── README.md             # File này
└── .gitignore

```
## Yêu cầu hệ thống

- *Python 3.10* trở lên.
- *Không cần cài thêm thư viện* (chỉ dùng thư viện chuẩn của Python).

## Hướng dẫn cài đặt và chạy chương trình

*Bước 1: Tải mã nguồn*
Mở Terminal (Linux/Mac) hoặc CMD (Windows), tải code từ GitHub về máy:
git clone https://github.com/linhsywhimsy/ATBMTT.git
cd ATBMTT
(Hoặc bấm nút Code màu xanh trên GitHub -> Download ZIP, giải nén và mở Terminal/CMD tại thư mục vừa giải nén).

*Bước 2: Khởi chạy chương trình*
Tại thư mục gốc của dự án, gõ lệnh:
python main.py
(Nếu dùng máy Mac, có thể dùng lệnh python3 main.py)

*Bước 3: Sử dụng*
Sau khi chạy lệnh trên, màn hình sẽ hiển thị Menu chương trình với 7 chức năng (Mã hóa/giải mã văn bản, Mã hóa/giải mã tệp, Chạy kiểm thử...). Bạn chỉ cần nhập số tương ứng và làm theo hướng dẫn trên màn hình.
github.com

## Cách chạy kiểm thử tự động

Để chạy bộ test tự động kiểm tra tính đúng đắn của thuật toán, hãy mở Terminal/CMD tại thư mục gốc và chạy:
python test/test_all.py
Kết quả mong đợi sẽ hiển thị: Passed: 9. 

## Phân công nhóm

| Thành viên | Công việc |
|---|---|
| Kiều Phương Linh - Leader | TinyA5/1 + phân tích độ an toàn |
| Trần Thu Trang | Bối cảnh + utils.py |
| Trịnh Minh Châu | Mô tả thuật toán + CLI |
| Lê Hoàng Mai | Ví dụ tính tay + bộ kiểm thử |
| Đào Quang Trung | So sánh với RC4 + A5/1 |

## Tài liệu tham khảo

1. Biryukov, A., Shamir, A., & Wagner, D. (2000). *Real Time Cryptanalysis of A5/1 on a PC*. FSE 2000.
2. Golic, J. (1997). *Cryptanalysis of the Alleged A5 Stream Cipher*. EUROCRYPT 1997.
3. Gendrullis, T., Novotny, M., & Rupp, A. (2008). *A Real-World Attack Breaking A5/1 within Hours*. ePrint 2008/147.
4. Gundaram, P. K., Tentu, A. N., & Allu, S. N. (2022). *State Transition Analysis of GSM Encryption Algorithm A5/1*. Journal of Communications Software and Systems.
