def FirstFit(block_Size, blocks, process_Size, proccesses):
    # code to store the block id of the block that needs to be allocated to a process
    allocate = [-1] * proccesses
    # Any process is assigned with the memory at the initial stage

    # find a suitable block for each process
    # the blocks are allocated as per their size

    for i in range(proccesses):
        for j in range(blocks):
            if block_Size[j] >= process_Size[i]:
                # assign the block j to p[i] process
                allocate[i] = j
                block_Size[j] -= process_Size[i]
                break

    print("Process No.\t    Process Size \t\tBlock No.")

    for i in range(proccesses):
        print(str(i + 1) + "\t\t\t" + str(process_Size[i]) + "\t\t\t", end=" ")

        if allocate[i] != -1:
            print(allocate[i] + 1)
        else:
            print("Not Allocated")


# Driver code
if __name__ == "__main__":
	block_Size =  [100, 500, 200, 300, 600]
	process_Size = [212, 417, 112, 426]
	m = len(block_Size)
	n = len(process_Size)

	FirstFit(block_Size, m, process_Size, n)