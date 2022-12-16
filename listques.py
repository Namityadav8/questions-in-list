# n=[1,2,3,4,5,2,6]
# in the above list find value 2 , if it iss there replace it with 200, only the first occurate
n=[1,2,3,4,5,2,6]
x= n.index(2)
n.pop(x)
n.insert(x,200)
print(n)