lst = [1,2,3,4,5,7,85,9]
lst.sort()
first = 0
last = len(lst) - 1
mid = (first+last)//2
item = int(input("Enter your number to search: "))
found = False
while (first <= last and not found):
    mid = (first+last)//2
    if lst[mid] == item:
        print(f"Item Found in the {mid}th position")
        found = True
    else:
        if item < lst[mid]:
            last = mid - 1
        else:
            first = mid + 1
if found == False:
    print("Not Found")


