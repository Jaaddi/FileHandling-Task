def average_calculator(filename):
    f = open(filename, 'r')
    A = f.read().strip().split('\n')
    f.close()
    l_c = 0
    n_c = 0
    for i in A:
        l_c += len(i)
    for j in A:
        n_c += 1
    print("Average : ",l_c/n_c)
filename = 'names.txt'
average_calculator(filename)
