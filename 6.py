def perfect_length_name(l):
    counter = 0
    f = open('names.txt', 'r') 
    A = f.read().strip().split()
    f.close()
    for i in A:
        counter += 1
    for i in range(0, counter):
        if l == len(A[i]):
            print(A[i])
perfect_length_name(5)
