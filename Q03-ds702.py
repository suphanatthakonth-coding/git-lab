def GCD(a, b):
    n = a if a < b else b 
    gcd = 1
    for i in range(n, 1, -1): #range(start, stop, step)
        if a % i == 0 and b % i == 0:
            gcd = i
            break
    
    return gcd

a = int(input("First Number: "))
b = int(input("Second Number: "))
print("GCD: ", GCD(a, b)) 