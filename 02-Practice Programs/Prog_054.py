# Create a function that prints all even numbers from 1 to 20.

def even():
    for i in range(1,21):
        if i%2!=0 :
            continue
        print(i)

even()