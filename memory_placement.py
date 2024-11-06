# First Fit
def first_fit(blocks, files):
    print("\nFirst Fit Allocation:")
    allocation = [-1] * len(files)
    for i in range(len(files)):
        for j in range(len(blocks)):
            if blocks[j] >= files[i]:
                allocation[i] = j
                blocks[j] -= files[i]
                break
    print_allocation(files, allocation)

# Best Fit
def best_fit(blocks, files):
    print("\nBest Fit Allocation:")
    allocation = [-1] * len(files)
    for i in range(len(files)):
        best_idx = -1
        for j in range(len(blocks)):
            if blocks[j] >= files[i]:
                if best_idx == -1 or blocks[j] < blocks[best_idx]:
                    best_idx = j
        if best_idx != -1:
            allocation[i] = best_idx
            blocks[best_idx] -= files[i]
    print_allocation(files, allocation)


# Worst Fit
def worst_fit(blocks, files):
    print("\nWorst Fit Allocation:")
    allocation = [-1] * len(files)
    for i in range(len(files)):
        worst_idx = -1
        for j in range(len(blocks)):
            if blocks[j] >= files[i]:
                if worst_idx == -1 or blocks[j] > blocks[worst_idx]:
                    worst_idx = j
        if worst_idx != -1:
            allocation[i] = worst_idx
            blocks[worst_idx] -= files[i]
    print_allocation(files, allocation)


# Next Fit
def next_fit(blocks, files):
    print("\nNext Fit Allocation:")
    allocation = [-1] * len(files)
    j = 0  # Start from the first block
    for i in range(len(files)):
        allocated = False
        for _ in range(len(blocks)):
            if blocks[j] >= files[i]:
                allocation[i] = j
                blocks[j] -= files[i]
                allocated = True
                j = (j + 1) % len(blocks)  # Move to the next block after allocation
                break
            j = (j + 1) % len(blocks)
        if not allocated:
            print(f"Not enough memory to allocate file {i+1}")
    print_allocation(files, allocation)

# Print Table
def print_allocation(files, allocation):
    print("File Number\tFile Size\tBlock Number")
    for i, file_size in enumerate(files):
        block_number = allocation[i] if allocation[i] != -1 else "Not Allocated"
        print(f"{i+1}\t\t{file_size}\t\t{block_number}")


def main():
    blocks = [100, 500, 200, 300, 600]  
    files = [212, 417, 112, 426]  

    print("Blocks:", blocks)
    print("Files:", files)

    first_fit(blocks.copy(), files)
    best_fit(blocks.copy(), files)
    worst_fit(blocks.copy(), files)
    next_fit(blocks.copy(), files)

main()
