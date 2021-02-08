def smaller_name(filename):
    counter = 0
    index = 0
    f = open(filename, 'r')
    A = f.read().strip().split('\n')
    f.close()
    smaller = len(A[0])
    for i in A:
        counter += 1
    for i in range(0, counter):
        if smaller > len(A[i]):
            smaller = len(A[i])
            index = i
    print("Smaller Name in the file is :",A[index])
    print("Length of Smaller Name is :",smaller)
    print("Index of Smaller Name is : ",index)
filename = "names.txt"
smaller_name(filename)
