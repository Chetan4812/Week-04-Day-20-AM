# Max and Min
nums = [23, 45, 12, 67, 34]
max_val = nums[0]
min_val = nums[0]

for n in nums:
    if n > max_val:
        max_val = n
    if n < min_val:
        min_val = n

# Frequency Count
freq = {}
for n in nums:
    if n in freq:
        freq[n] += 1
    else:
        freq[n] = 1

print(max_val)
print(min_val)
print(freq)
