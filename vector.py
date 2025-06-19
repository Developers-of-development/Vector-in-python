class vector():
    li  =[] # List for all oprations
    def __init__(self , lis):
        self.li = lis # giving user list value to 
        
    def push_back(self,push_value : any):
        self.li.append(push_value) # adding value at end with it
        return self.li
    
    def pop_back(self): # will reomve last value of your vector
        self.li.pop()
        return self.li
    
    def size(self): # get size of vector
        return len(self.li)
    
    def front(self): # get first value of vector
        return self.li[0]
    
    def back(self): # last value of vector
        return self.li[-1]
    
    def at(self , index : int): # workflow with index bcz vector in this doesn't for direct vec[] use vec.at()
        if index >= len(self.li): #chacking if there index or not
            return "No worth index!"
        else:
            return self.li[index] # return that index value
    
    def ease(self , remove_value : any): # remove value from vector
        if remove_value in self.li:
            return self.li.remove(remove_value)
        else:
            return f"Value {remove_value} not found in the vector"

    def show(self): # shows all value 
        for i in range(len(self.li)):
            if(i != (len(self.li)-1)):
                print(self.li[i] , end=" ")
            else:
                print(self.li[i])

    def In(self , find_value): # find and return value index if avaible
        if find_value in self.li:
            return f"Yes! at index {self.li.index(find_value)}"
        else:
            return "Value not found in vector"
# Complete vector Done with two advance feature!

if __name__ == '__main__':
    vector(lis=[1,2,3,4,5,6])
