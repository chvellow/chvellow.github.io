# array
print("Array pertama")
print("")

buah =["Anggur", "Apel", "Pisang", "Nanas", "Jeruk", "Mangga"]
print(buah[2])


print("")
print("")

buah[4]= "Durian"
print(buah[4])


print("")
print("")

buah.append("mata kucing")
buah.insert(3, "bola")
print(buah)


print("")
print("")
# membuat list
todo_list=[
    "belajar python",
    "bljr mtk",
    "bljr sulap",
    "bljr bahasa",
    "bljr masak",
    "bljr lukis",
    "bljr gitar"
]
del todo_list[2]
print(todo_list)
print("")
print("")


todo_list.remove("bljr mtk")
print(todo_list)
print(todo_list[1:3])
print(todo_list + todo_list)
print(todo_list * 5)