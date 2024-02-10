username=input("USERNAME : ")
password=input("PASSWORD : ")
if username == "weer" and password == "1234":
    print("DONE !!!")
    print("------------------")
    print("Banana     10THB >>>1")
    print("Apple      20THB >>>2")
    print("Chocolate  30THB >>>3")
    userSelected = input(">>>")
    if userSelected == "1":
        amount=int(input("How many? :"))
        print("Total Price :",str(10*amount)+"THB")
    elif userSelected == "2":
        amount=int(input("How many? :"))
        print("Total Price :",str(20*amount)+"THB")
    elif userSelected == "3":
        amount=int(input("How many? :"))
        print("Total Price :",str(30*amount)+"THB")
else:
    print("---ERROR---")