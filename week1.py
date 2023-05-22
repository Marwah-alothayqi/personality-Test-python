
Name=input("Enter your name!") #user name

print("Welcome "+Name)
print("From the menu below choice your favorite number to do a personality Test,"
           " which reveals your personality Traits.")

#Tuples
numbers=("Then your number personality reveals that you are known for a great sense of humor",0)

#Dictionary
numbers1={"one": "Then your number personality reveals that you embody leadership qualities",
         "tow": "Then your number personality reveals that you are an emotional and intuitive individual",
         "three": "Then your number personality reveals that you are outgoing and the life of any party",
         "four": "Then your number personality reveals that you are a reliable, sincere, dependable kind of individual",
         "five": "Then your number personality reveals that you are filled high level of enthusiasm, excitement, and energy"}

#List
numbers2=["Then your number personality reveals that you are a caring and gentle individual",
          "Then your number personality reveals that you are calm, cool, and collected kind of individual",
          "Then your number personality reveals that you are a lover of stability. You have quite a powerful personality",
          "Then your number personality reveals that you are a charismatic, compassionate, confident, friendly,living-in-the-present kind of individual"]

for i in range(0,10):
    print(i)

num=int(input("Write Your Choice!"))
if num==0:
     print(numbers[0])


elif num==1:
     print(numbers1["one"])
elif num==2:
     print(numbers1["tow"])
elif num==3:
     print(numbers1["three"])
elif num==4:
     print(numbers1["four"])
elif num == 5:
    print(numbers1["five"])


elif num == 6:
    print(numbers2[0])
elif num == 7:
    print(numbers2[1])
elif num == 8:
    print(numbers2[2])
elif num == 9:
    print(numbers2[3])
else:
    print("Please choice number from the menu")




