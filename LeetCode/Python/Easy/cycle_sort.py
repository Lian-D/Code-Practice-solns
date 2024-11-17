class Solution(object):
    def cycleSort(self, arr, n):
        i = 0
        while(i < n):
            # intended index for this current value
            correct = arr[i]-1
            print(correct)

            print(str(arr[correct])+" vs "+str(arr[i]))
            if arr[correct] != arr[i]:
                # calling swap function
                self.swap(arr, i, correct)
                print(arr)
            else:
                i = i + 1
        return arr

    def swap(arr, first, second):
        tempVal1 = arr[first]
        arr[first] = arr[second]
        arr[second] = tempVal1

        

 


solution = Solution
print(solution.cycleSort(solution, [2, 6, 4, 3, 1, 5], 5))