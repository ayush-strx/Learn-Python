# Print numbers from 1 to 20, but skip the numbers 5, 10, and 15 using continue.

for i in range(1,21):
    if (i==5) or (i==10) or (i==15):
        continue
    print(i)