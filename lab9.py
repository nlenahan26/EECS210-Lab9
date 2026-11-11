# Name: Nathan Lenahan
# KUID: 3178995
# Lab session: Wednesday 11AM
# Lab #9
# Description: The program determines whether an undirected graph is connected or not.
# Collaborators: None
# Outside sources: None

#This function is similar to Lab 3, but now it will keep running until the user inputs a square matrix
def get_square_matrix(ints=False):
    """ 
    Takes a square matrix of numbers from the user. Each row can be 
    separated by commas and/or spaces. Automatically ends after the last row.

    If ints=False, the function returns a matrix of strings. 
    If ints=True, they will be cast to int instead
    """
    print("Enter your matrix:")
    matrix = []

    x = input()
    #If blank line, try again
    if not x.strip():
        return get_square_matrix(ints=ints)

    items = x.replace(",", " ").split()
    length = len(items)
    matrix = []

    #Save the first row
    if not ints:
        matrix.append(items)
    else:
        try:
            row = [int(entry) for entry in items]
            matrix.append(row)
        except ValueError:
            print("Error: all entries must be numbers! Try again:")
            #If first row is bad, try again
            return get_square_matrix(ints=ints)

    #Get the rest of the rows
    while True:
        x = input()
        items = x.replace(",", " ").split()
        if len(items) != length:
            print("Error: row lengths are mismatched! Try again:")
            continue  # re-try the line
        if not ints:
            matrix.append(items)
        else:
            try:
                row = [int(entry) for entry in items]
                matrix.append(row)
            except ValueError:
                print("Error: all entries must be numbers! Try again:")
                continue  # re-try the line
        #Check if matrix has been completed (is square)
        if len(matrix) == length:
            return matrix

#Helper function to print a 2-D matrix
def print_matrix(m):
    n = len(m)
    # Create labels (a, b, c, ...)
    labels = [chr(ord('a') + i) for i in range(n)]
    
    # Print top header row
    print("  ", end="")  # space for corner
    for label in labels:
        print(label, end=" ")
    print()
    
    # Print each row with its corresponding label
    for i, row in enumerate(m):
        print(labels[i], end=" ")  # row label
        for item in row:
            print(item, end=" ")
        print()

def main():
    M_R = get_square_matrix(ints=True)
    print("Got: ")
    print_matrix(M_R)

if __name__ == "__main__":
    main()
