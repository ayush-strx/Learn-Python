# Print numbers from 1 to 20, but skip 10. using while loop.

i = 1
while i<=20:
    if i == 10:
        i+=1
        continue
    print(i)
    i+=1
    