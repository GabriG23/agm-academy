
def square_area(l):
    return l * l

def rect_area(b, h):
    return b * h

def conversion_C_F(c, f1 = 1.8, f2 = 32):
    return c * f1 + f2

def sum_numbers(numbers):
    return sum(i for i in numbers if i % 2 == 0)

def reverse_order(text):
    return text[::-1]

def remove_len_5(text): # return only the strings with length > 5
    return [s for s in text if len(s) > 5]

def max_number(numbers):
    return max(numbers)

def longest_string(strings):
    return max(strings, key=len)

def string_conversion(num):
    return str(num)

def int_conversion(string):
    return int(string)

def numbers_converter(strings):
    return [int(s) for s in strings]

def strings_converter(numbers):
    return [str(n) for n in numbers]

def number_splitter(num):
    return [int(s) for s in str(num)]