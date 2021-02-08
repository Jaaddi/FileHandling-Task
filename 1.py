def four_index(filename):
    f = open(filename, 'r')
    A = f.read().strip().split('\n')
    f.close()
    counter = 0
    for i in A:
        counter += 1
    for j in range(0, counter):
        print(A[j][:4])
filename = 'names.txt'
four_index(filename)
