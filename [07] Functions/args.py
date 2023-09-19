# args#
# *args - non keyword arguments
def add(*nums):
    sum = 0
    for n in nums:
        sum += n
    return sum


print("Sum:", add(3, 6))
print("Sum:", add(1, 2, 3, 4, 5, 6))
print("Sum:", add(10, 2, 3, 5, 4))
