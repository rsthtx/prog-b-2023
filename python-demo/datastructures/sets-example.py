my_string = "Hej og velkommen til programmering"
print(my_string)

set_of_chars = set(my_string)
print(set_of_chars)

my_other_string = "Glædelig jul og godt nytår"
print(my_other_string)

my_other_string_as_set = set(my_other_string)
print(my_other_string_as_set)

common_letters = set_of_chars.intersection(my_other_string_as_set)
print(common_letters)
print(list(common_letters))


sorted_common_letters = sorted(list(common_letters))
print(sorted_common_letters)

# reverse sorted
every_second_common_letter_in_reverse_sorted_order_as_upper_case = "".join((sorted_common_letters[::-2])).upper()
print(every_second_common_letter_in_reverse_sorted_order_as_upper_case)