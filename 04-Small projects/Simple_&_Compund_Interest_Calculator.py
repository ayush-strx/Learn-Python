print("Enter Your Choice No.(1-Simple Interest/2-Compund Interest)")

i = float(input("Enter choice number:"))

if i == 1:
    p = float(input("Enter Principal Amount:"))
    r = float(input("Enter Rate of Interest:"))
    t = float(input("Enter Years:"))

    si = (p*r*t)/100
    print("Simple Interest is:", si)
else:
    p = float(input("Enter Principal Amount:"))
    r = float(input("Enter Rate of Interest:"))
    t = float(input("Enter Years:"))

    ci = p * (1 + r / 100) ** t
    print("Compund Interest is:", ci)
