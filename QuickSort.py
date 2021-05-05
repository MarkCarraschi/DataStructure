class QuickSort:

    def sum(self, list):
        total = 0

        for element in list:
            total+= element
        
        return total
     
    def recursion_sum(self, list):

        if len(list) == 1:
            return list[0]
        else:
            return list[0] + self.recursion_sum(list[1:])
            

if __name__ == '__main__':
        
    array = [10, 20, 30]
    # print(sum(array))

    obj_quicksort = QuickSort()

    print(obj_quicksort.recursion_sum(array))