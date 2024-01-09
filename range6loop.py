def print_numbers():
    for i in range(1, 6):
        # outer loop
        for j in range(0,i+1):
            print("*", end=" ")
        print('\n')

print_numbers()

