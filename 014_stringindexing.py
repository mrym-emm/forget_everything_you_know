"""
indexing = accessing elemts of a sequence using [] (indexing operators)
          [start : end : step]
"""

credit_number = "1234-9021-2938-1929"

# print(credit_number[0])
# print(credit_number[0:4])
# print(credit_number[5:]) # everything from index 5 till end of string
#
# print(credit_number[-1])
#
# print(credit_number[::2])
#
# x = "12345"
#
# print(x[::2])

# last 4 digits

last_digits = (credit_number[-4:])

print(f"XXXX-XXXX-XXXX-{last_digits}")

# reverse credit number
reverse = credit_number[::-1]
print(f"{reverse}")


