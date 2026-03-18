num = 121
temp = num
reverse = 0

while temp > 0:
    digit = temp % 10
    reverse = reverse * 10 + digit
    temp //= 10

is_palindrome = (num == reverse)

print(reverse)
print(is_palindrome)
