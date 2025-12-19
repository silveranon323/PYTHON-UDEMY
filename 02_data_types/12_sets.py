#Sets are similar to lists but are unordered and cannot contains duplicate values.

my_set={1,2,3,4,5,1,2}

print(my_set)
print(len(my_set))

for x in my_set:
    print(x)

my_set.discard(3)  # removes a element from the set
print(my_set) # clears the set
my_set.add(6) # adds an element to the set

print(my_set)

my_set.update([1,2,3]) #




