mytuple=(1,2,3,4)
print("the original"+str(mytuple))
list_tuple=list(mytuple)
list_tuple[0],list_tuple[-1]=list_tuple[-1],list_tuple[0]
tuple(list_tuple)

print("the swapped tuple"+str(list_tuple))
