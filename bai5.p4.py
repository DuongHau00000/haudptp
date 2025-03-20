try:
    with open("multiline.txt", "r", encoding="utf-8") as nd_file:
        tl = nd_file.read()
    with open("copy.txt", "w", encoding="utf-8") as nn_file:
        nn_file.write(tl)
    print("Nội dung đã thành công từ multiline.txt sang copy.txt.")
except FileNotFoundError:
    print("Lỗi: file multiline.txt không tồn tại.")
