amount = int(input("Enter Your Amount:"))

print("----------------Currency Notes Calculator------------")
print("1 - 100 Rupee Notes")
print("2 - 200 Rupee Notes")
print("3 - 500 Rupee Notes")

notes = int(input("Enter Your Choice:"))

if notes == 1:
    a  = (print(" Total notes:", amount//100))
    print(a)
    
    remain = (amount%100)
    print("Remaining Amount:", remain)

elif notes == 2:
    a  = (print(" Total notes:", amount//200))
    print(a)
    
    remain = (amount%200)
    print("Remaining Amount:", remain)

elif notes == 3:
    a  = (print(" Total notes:", amount//500))
    print(a)
    
    remain = (amount%500)
    print("Remaining Amount:", remain)

else:
    print("Choice is invalid.")
