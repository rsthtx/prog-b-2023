my_string = "Hej og velkommen til programmering"
print(my_string)

first_letter = my_string[0]
print(first_letter)

last_letter = my_string[-1]
print(last_letter)

# String slice
part_of_string = my_string[4:10]
print(part_of_string)
# - from beginning to index
print(my_string[:10])
# - from index to end
print(my_string[8:])

# extract every second letter in string
every_second_letter_list = []
for n in range(0,len(my_string), 2):
    ch = my_string[n]
    every_second_letter_list.append(ch)

every_second_letter = "".join(every_second_letter_list)
print(every_second_letter_list)
print(every_second_letter)

# extract every second letter in string easy method
every_second_letter_easy = my_string[::2]
print(every_second_letter_easy)

# slice using index skip
print(my_string[8::3])

reversed_version_of_string = my_string[::-1]
print(reversed_version_of_string)

print(my_string)
my_string_as_list_of_chars = list(my_string)
print(my_string_as_list_of_chars)
