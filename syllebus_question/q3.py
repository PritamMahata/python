# input 3 number and print which is large and which is small
print("Enter 3 number")
list = [0,0,0]
for i in range(0,3):
    list[i] = int(input())
print("Maximun number is ", max(list))
print("Minimun number is ", min(list))