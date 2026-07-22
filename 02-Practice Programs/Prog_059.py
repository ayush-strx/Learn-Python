# Create a function that takes three subject marks and prints the percentage.
def check(sub1,sub2,sub3):
    per = (sub1+sub2+sub3)/300*100
    print(per)

sub1 = int(input("Enter the Math marks:"))
sub2 = int(input('Enter the Science marks:'))
sub3 = int(input("Enter the English marks:"))

check(sub1,sub2,sub3)
