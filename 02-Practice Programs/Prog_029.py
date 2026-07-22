# Check whether a student is passed or failed and show their percentage and grade based on marks (A, B, C, D, F).

sub1 = int(input("Enter your english marks:"))
sub2 = int(input("Enter your math marks:"))
sub3 = int(input("Enter your science marks:"))

per = (sub1+sub2+sub3)/300*100

if (sub1 < 0 or sub1 > 100) or (sub2 < 0 or sub2 > 100) or (sub3 < 0 or sub3 > 100):
    print("Invalid Marks!")

elif (sub1<35) or (sub2<35) or (sub3<35):
    print("You are Failed")
    print("Your percentage is", per)
else:
    if (per>=85):
        print("You are passed and you got Grade A")
        print("Your percentage is", per)
    elif (per>=70):
        print("You are passed and you got Grade B")
        print("Your percentage is", per)
    elif (per>=55):
        print("You are passed and you got Grade C")
        print("Your percentage is", per)
    else:
        print("You are passed and you got Grade D")
        print("Your percentage is", per)
