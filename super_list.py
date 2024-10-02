#Extending List
class SuperList(list):
    pass
    #code
#index through list using 
#special dunder method
#modify __len__ to come up with 1000
#no matter what using inheritance
    def __len__(self):
        return 1000 

super_list1 = SuperList()

print(len(super_list1))
super_list1.append(5)
print(super_list1[0])
print(issubclass(SuperList, list))