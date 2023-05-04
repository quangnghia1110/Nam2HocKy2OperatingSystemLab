def WorstFit(blockSize, blocks, processSize, processes):
    # This will store the block id of the allocated block to a process
    allocation = [-1] * processes
    
    # pick each process and find suitable blocks
    # according to its size and assign to it
    for i in range(processes):
        indexPlaced = -1
        for j in range(blocks):
            # if not occupied and block size is large enough
            if blockSize[j] >= processSize[i]:
                # place it at the first block fit to accommodate process
                if indexPlaced == -1:
                    indexPlaced = j
                # if any future block is larger than the current block where
                # process is placed, change the block and thus indexPlaced
                elif blockSize[indexPlaced] < blockSize[j]:
                    indexPlaced = j
        
        # If we were successfully able to find block for the process
        if indexPlaced != -1:
            # allocate this block j to process i
            allocation[i] = indexPlaced
 
            # Reduce available memory for the block
            blockSize[indexPlaced] -= processSize[i]
 
    print("\nProcess No.\tProcess Size\tBlock no.")
    for i in range(processes):
        print(f"{i+1} \t\t\t {processSize[i]} \t\t\t", end="")
        if allocation[i] != -1:
            print(allocation[i] + 1)
        else:
            print("Not Allocated")
 

# Driver code
if __name__ == "__main__":
    blockSize =  [100, 500, 200, 300, 600]
    processSize = [212, 417, 112, 426]
    blocks = len(blockSize)
    processes = len(processSize)

    WorstFit(blockSize, blocks, processSize, processes)
