# this function takes a string message as a parameter,
# performs Run Length Encoding on the string,
# and returns a new string representing the compressed message.


def RLE_compress(message):
    code_list = list(message)
    print_list = []
    counter = 0
    for i in range(len(code_list)-1):
        counter += 1
        if code_list[i] != code_list[i+1]:
            print_list.append(code_list[i])
            print_list.append(counter)
            counter = 0
    print_list.append(code_list[len(code_list)-1])
    print_list.append(counter+1)
    for letter in print_list:
        print(letter, end="") 
    return ""

# TEST CODE:
print(RLE_compress("AABBBAAAABBBBBAAAAAABBBBBBB"))
print(RLE_compress("AACCCCBBBBBAAAAAAAXFFFFFFFF"))
print(RLE_compress("AACCCCBBBBBAAAAAAAXFFFFFFFFD"))
print(RLE_compress("AACCCCBBBBBAAAAAAAXFFFFFFFFDD"))
print(RLE_compress("AACCCCBBBBBAAAAAAAXFFFFFFFFDDD"))
print(RLE_compress("ABCDEF"))
print(RLE_compress("FFFFFFFFFFFFFFFFFFF"))
print(RLE_compress("F"))
print(RLE_compress("F????"))
print(RLE_compress("Mmmmmmmmmm sooooo goooooood!"))
print(RLE_compress("Booooooooooooo, hisssssssss"))