# import random
#
# while True:
#     print('''1.roll the dice  2.exit   ''')
#     user = int(input("What you wanna do \n"))
#     if user == 1:
#         number = random.randint(1,6)
#         print(number)
#     else:
#         break
# import random
#
# number = random.randint(1,10)
# for i in range(0,3):
#     user = int(input("Guess number:"))
#     if user == number:
#         print("Congo....gues is correct")
#         break
# if user != number:
#     print(f"next time {number}")
# import random
# pass_len = int(input("Enter len password: "))
# sample_pass = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_+-=[]\;',./{}|:<>?1234567890"
# rand_pa = "".join(random.sample(sample_pass, pass_len))
# print(rand_pa)

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






