def print_multiplication_table(n):
    
    print("results in row display")
    for i in range(1, n+1):
        for j in range(1, n+1):
            print(f"{i} x {j} = {i*j}", end="\t") #results in row display
        print() #empty print statement is called to move to the next line
    
    print("results in column display")

    for i in range(1, n+1):
        for j in range(1, n+1):
            print(f"{j} x {i} = {j*i}", end='\t') #results in column display
        print() #empty print statement is called to move to the next line

print_multiplication_table(5)

