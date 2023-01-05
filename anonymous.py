double = lambda x : x*2
print("The double value is ",double(5))

my_list = [1,2,3,4,5,6,7,8]
new_list = list(filter(lambda x : (x%2 != 0),my_list))
print(new_list)

my_list = [1,2,3,4,5,6,7,8]
new_list = list(map(lambda x : x*2,my_list))
print(new_list)