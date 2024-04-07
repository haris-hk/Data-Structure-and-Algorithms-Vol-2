 
# Decrypts the data using the logic of the Karatsuba algorithm.
# Args:
#   data: List of list consisting leaves
# Returns:
#   A tuple containing the original two numbers.

def reverse_karatsuba(data) -> tuple:
    if type(data[-1]) == tuple and type(data[0]) == tuple:
        return int(str(data[-1][0]) + str(data[0][0])), int(str(data[-1][1]) + str(data[0][1]))
    
    if type(data[-1]) == list:
        x = reverse_karatsuba(data[-1])
    else:
        x = data[-1]
    if type(data[0]) == list:
        y = reverse_karatsuba(data[0])
    else:
        y = data[0]
    
    return reverse_karatsuba((y, x))




    


# This function reads data from a specified file and decrypt data using the logic of the Karatsuba algorithm.
# Args:
#   filename: The name of the file containing input data.
# Returns:
#   A list of tuples, each tuple representing coordinates (x, y).


def main(filename) -> list[tuple[int, int]]:
    with open (filename) as f :
        lines = f . readlines ()
    input = []
    lines.pop(0)
    for line in lines :
        if isinstance(line, int) == True:
            rnge = line
            next
        if isinstance(line, int) == False:    
            tokens = eval(line)
            input.append( reverse_karatsuba(tokens))
    
    return input


data = main('input_decrypt.txt')

print(data)
