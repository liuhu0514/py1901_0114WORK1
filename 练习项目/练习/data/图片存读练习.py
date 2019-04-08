# with open("C:/Users/Administrator/Desktop/图片1.jpg","rb") as file:
#     a = file.read()
#     print(a)

with open("C:/Users/Administrator/Desktop/图片1.jpg", "rb") as file:
    with open("./data/1.jpg", "wb") as file1:
        file1.write(file.read())
