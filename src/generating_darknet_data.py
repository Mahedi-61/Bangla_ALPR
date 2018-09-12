with open("/home/mahedi/Desktop/train.txt", "w") as file:
    for i in range(1, 447):
        if (i < 10):
            file.write("data/obj/0000" + str(i) + ".png\n")

        elif(i < 100):
            file.write("data/obj/000" + str(i) + ".png\n")
        
        else:
            file.write("data/obj/00" + str(i) + ".png\n")


