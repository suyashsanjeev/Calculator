def index(my_list, el):    
    for i in range(len(my_list)):
        if my_list[i] == el:
            return(i)

a = [1,2,3,4,5]
element = 5

print(index(a,element))
