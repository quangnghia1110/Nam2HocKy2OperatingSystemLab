from collections import defaultdict

print("Enter the number of frames: ", end="")
capacity = int(input())
f, fault = [], 0
page_count = defaultdict(int)
print("Enter the reference string: ", end="")
s = list(map(int, input().strip().split()))
print("\nString|Frame →\t", end='')
for i in range(capacity):
    print(i, end=' ')
print("Fault\n   ↓\n")
for i in s:
    if i not in f:
        if len(f) < capacity:
            f.append(i)
        else:
            min_count = min(page_count.values())
            min_pages = [k for k, v in page_count.items() if v == min_count]
            min_page = f.index(min(set(f) & set(min_pages)))
            del page_count[f[min_page]]
            f[min_page] = i
        fault += 1
        page_count[i] += 1
        pf = 'Yes'
    else:
        page_count[i] += 1
        pf = 'No'
    print("   %d\t\t" % i, end='')
    for x in f:
        print(x, end=' ')
    for x in range(capacity - len(f)):
        print(' ', end=' ')
    print(" %s" % pf)

print("\nTotal requests: %d\nTotal Page Faults: %d\nFault Rate: %0.2f%%" % (len(s), fault, (fault / len(s)) * 100))
