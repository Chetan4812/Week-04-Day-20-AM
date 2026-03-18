#sample data
data = [("a", 10), ("b", 25), ("c", 15)]

my_dict = {}
highest_key = None
max_val = -float('inf')
for k, v in data:
    my_dict[k] = v
    if my_dict[k] > max_val:
        max_val = my_dict[k]
        highest_key = k

print(highest_key)
