# demo_attack.py
# Minh họa tấn công vét cạn (Brute-force) lên TinyA5/1
# (Chạy tấn công để minh hoạ máy tính phá khóa nhanh như thế nào)

import time
from core.tiny_a5_1 import TinyA5_1
from core.utils import bits_to_string

def tan_cong():
    print("=" * 60)
    print("MINH HỌA TẤN CÔNG VÉT CẠN (BRUTE-FORCE) LÊN TINYA5/1")
    print("=" * 60)
    
    # 1. Giả lập: Kẻ tấn công biết bản rõ (P) và bản mã (C) bị chặn
    P = [1, 0, 1, 1, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 1]  
    K_bi_mat = [1,0,0,1,0,1, 0,1,0,0,1,1,1,0, 1,0,0,1,1,0,0,0,0]
    
    print(f"[-] Bản rõ P: {bits_to_string(P)}")
    cipher = TinyA5_1(K_bi_mat)
    C_bi_mat = cipher.encrypt(P)
    print(f"[-] Bản mã C: {bits_to_string(C_bi_mat)}")
    print(f"[-] Kẻ tấn công KHÔNG biết khóa bí mật. Bắt đầu dò...\n")
    
    # 2. Bắt đầu quá trình tấn công vét cạn (dò từ 0 đến 2^23)
    bat_dau = time.time()
    
    for i in range(2**23):
        # Chuyển số i thành mảng 23 bit
        khoa_thu = [int(b) for b in format(i, '023b')]
        
        # Dùng khóa thử để mã hóa P
        cipher_thu = TinyA5_1(khoa_thu)
        if cipher_thu.encrypt(P) == C_bi_mat:
            thoi_gian = time.time() - bat_dau
            print(f"[+] TÌM THẤY KHÓA SAU {i+1:,} LẦN THỬ!")
            print(f"[+] Khóa bí mật là: {bits_to_string(khoa_thu)}")
            print(f"[+] Thời gian chạy: {thoi_gian:.3f} giây")
            break

if __name__ == "__main__":
    tan_cong()
