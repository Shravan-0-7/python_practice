#listOperations.py

nums=[]
for i in range (0,10):
    x=int(input(f"Enter the {i}th Element ")) #accepts element from user 10 times for list
    nums.append(x)

print("sum of last 4 elements is: ",nums[-1]+nums[-2]+nums[-3]+nums[-4] )

diff = max(nums)-min(nums)
print("difference between max and min of nums is: ",diff)   #will print max-min

nums.insert(5,(nums[4]/3 ))   #this function will insert 1/3 of fourth element at 6th position
print("After inserting element: ",nums)

