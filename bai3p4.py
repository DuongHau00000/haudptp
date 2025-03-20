dongvb = 0
with open("multiline.txt", "w", encoding="utf-8") as file:
    while True:
        dong = input("Nhập văn bản (hoặc nhập 'STOP' để dừng): ")
        if dong == "STOP":
            break
        file.write(dong + "\n")
        dongvb += 1
print("Số dòng đã ghi vào file multiline.txt:",dongvb)