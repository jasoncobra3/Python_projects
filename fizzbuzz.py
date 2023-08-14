def fizzbuzz(n):
    for i in range (n+1):
        if (i%5==0 and i%3==0):
            print("FIZZBUZZ")
        elif (i%5==0):
            print("BUZZ")
        elif (i%3==0):
            print("FUZZ")
        else:
            print(i)

n=int(input("Enter the number:"))
fizzbuzz(n)