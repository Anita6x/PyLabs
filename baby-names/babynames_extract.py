import re

with open("baby2008.html") as file:
    content = file.read()

names = re.findall(r'<td>([A-Za-z]+)</td>', content)

def bubble_sort(names):
    n = len(names)
    for i in range(n):
        for j in range(0, n - i - 1):
            if names[j].lower() > names[j + 1].lower():
                names[j], names[j + 1] = names[j + 1], names[j]
    return names

sorted_names = bubble_sort(names)

with open("sorted_babynames.txt", "w") as f:
    for index, name in enumerate(sorted_names):
        f.write(f"{index}: {name}\n")

print("Sorted names have been saved to sorted_babynames.txt")


def binary_search(names, target):
    low = 0
    high = len(names) - 1

    target = target.lower()

    while low <= high:
        mid = (low + high) // 2
        mid_val = names[mid].lower()

        if mid_val == target:
            return mid
        elif mid_val < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1

name_to_find = "Emily"
position = binary_search(sorted_names, name_to_find)

if position != -1:
    print(f"{name_to_find} found at index {position}")
else:
    print(f"{name_to_find} not found")
