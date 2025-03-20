chu = input("Nhập đoạn văn bản: ")
with open("output.txt", "w", encoding="utf-8") as file:
    file.write(chu)
print("Nội dung được lưu vào file output.txt thành công.")


