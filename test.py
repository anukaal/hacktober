
count = 0
w = int(input("Enter the no.of test cases required."))
for m in range(w):
    n = int(input("The number of students in the class"))
    t = int(input("The cancellation threshold"))
    a =[]
    print("Enter The Time Of students Entering the class")
    for x in range(n):
       b = int(input())
       a.append(b)
    for i in range(n):
        if a[i] <= 0:
           count += 1
        if count >= t:
            print("NO")
        else:
	    print("YES")
