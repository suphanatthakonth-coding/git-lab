#method1
def random_text(t):
    a = t[1::2] + t[0::2]
    return a
t = input("Please enter a string: ").strip()
print("The plus one cypher: ", random_text(t))

#method2
t = input("Please enter a string: ").strip()
a = t[-1] + t[1:-1] + t[0]
print("The plus one cypher: ",a)