n = int(input("Enter an odd number: "))

if n % 2 == 0:
    print("Magic matrix is possible only for odd numbers.")
else:
    magic = [[0 for _ in range(n)] for _ in range(n)]

    # Start position 
    row = 0
    col = n // 2

    for num in range(1, n * n + 1):
        magic[row][col] = num

        # Save current position
        new_row = (row - 1) % n
        new_col = (col + 1) % n

        # If the next cell is already filled, move down
        if magic[new_row][new_col] != 0:
            row = (row + 1) % n
        else:
            row = new_row
            col = new_col

    # Print Magic Square
    print("\nMagic Matrix:")
    for r in magic:
        print(r)

    # Magic Sum
    magic_sum = n * (n * n + 1) // 2
    print("\nMagic Sum:", magic_sum)