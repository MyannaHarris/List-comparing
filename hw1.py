# Check if xs is proper subset of ys
def proper_subset(xs, ys):
    flag = True
    if len(xs) == len(ys):
        flag = False
    while len(xs) and flag == True:
        flag = False
        for i in ys:
            if i == xs[0]:
                flag = True
        xs.pop(0)
    return flag

# Get intersection of xs and ys
def intersect(xs, ys):
    intsect = []
    count = 0
    while len(xs) and count < len(ys):
        flag = False
        y = list(ys)
        while len(y) and flag == False:
            if xs[0] == y[0]:
                intsect.append(xs[0])
                flag = True
                count += 1
            else:
                y.pop(0)
        xs.pop(0)
    return intsect

# Get the objects in xs that do NOT exist in ys
def difference(xs, ys):
    for x in xs:
        for y in ys:
            if y == x:
                xs = [i for i in xs if i != x]
    return xs

# Get cartesian product
def cartesian_product(xs, ys):
    product = []
    for x in xs:
        for y in ys:
            product.append((x,y))
    return product

# Get n generations of the less than relation
def generate_n_recursive_less_thans(n):
    less_thans = []
    if n > 0:
        j = 1
        less_thans.append((0,j))
        temp = list(less_thans)
        while j < n:
            temp2 = list(temp)
            temp = []
            for x,y in temp2:
                less_thans.append((x,y+1))
                less_thans.append((x+1,y+1))
                temp.append((x,y+1))
                temp.append((x+1,y+1))
            j = j + 1
    
    return less_thans



# Check if first list is proper subset of second list
print (proper_subset([1,2], [1,2,3]))
print (proper_subset([2,1], [1,2,3]))
print (proper_subset([1,2], [2,3]))
print (proper_subset([1,2], [1,2]))
print (proper_subset([], []))
print ()

# Get intersection of 2 lists
print (intersect([1,2,3], [2,1,0]))
print (intersect([1,2], [1,2]))
print (intersect([1,2], [3,4]))
print ()

# Get the objects in first list that do NOT exist in 2nd list
print (difference([1,2,3], [2,3,4]))
print (difference([1,2], [1,2]))
print (difference([6,2,1,3,5], [3,2,4]))
print ()

# Get cartesian product
print (cartesian_product([1,2], [3,4]))
print (cartesian_product([1,2], [1,2]))
print ()

# Get n generations of the less than relation
print (generate_n_recursive_less_thans(0))
print (generate_n_recursive_less_thans(1))
print (generate_n_recursive_less_thans(2))
print (generate_n_recursive_less_thans(3))
print (generate_n_recursive_less_thans(4))
print (generate_n_recursive_less_thans(5))
print (generate_n_recursive_less_thans(6))
