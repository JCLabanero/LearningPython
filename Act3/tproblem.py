num_blocks = int(input("Enter a number: "))

height = 0
blocks_in_current_layer = 1
total_blocks = 0

while total_blocks < num_blocks:
    height += 1
    total_blocks += blocks_in_current_layer
    blocks_in_current_layer += 1

if total_blocks > num_blocks:
    height -= 1

print(f"The height of the pyramid is {height}.")
