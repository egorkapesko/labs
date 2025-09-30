input_string = input("Введите строку: ")

compressed_string = ""

count = 1

for i in range(1, len(input_string)):
    if input_string[i] == input_string[i - 1]:
        count += 1
    else:
        compressed_string += input_string[i - 1] + str(count)
        count = 1

compressed_string += input_string[-1] + str(count)

print("Сжатая строка:", compressed_string)
