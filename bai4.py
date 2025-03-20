try:
    with open("multiline.txt", "r", encoding="utf-8") as file:
        nd = file.read()
    if nd == "":
        print("File trống.")
    else:
        sdong = nd.count("\n") + 1 if nd else 0
        sotu = len(nd.split())
        sokt = len(nd)
        #ket quả
        print("Số dòng:",sdong)
        print("Số từ:",sotu)
        print("Số ký tự:",sokt)
except FileNotFoundError:
    print("Lỗi!: file multiline.txt không tồn tại!")
