'''In given list find element loaction through the binery search method'''
lst = [5,6,7,8,9,0,1]
lst.sort()
first = 0
last = len(lst)-1
mid = (first+last)//2
item = int(input("Enter item to Search: "))
found = False
while (first<=last and not found):
    mid = (first+last)//2
    if lst[mid] == item:
        print(f"Item Found in the Location {mid}")
        found = True
    else:
        if item < lst[mid]:
            last = mid - 1
        else:
            first = mid + 1
if found == False:
    print("Item not Found")
