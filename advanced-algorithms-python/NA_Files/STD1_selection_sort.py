'''SELECTION SORT
    input: unsorted list
    output: sorted list
    Implements bubble sort with integral swap
'''
def selection_sort(A):                             #This function sorts an array with selection sort
	for i in range(len(A)-1):                      #loop through input array
		min = i                                    #set smallest value to cursor
		for j in range(i+1, len(A)):               #loop through divided array, unsorted section
			if A[j] < A[min]:                      #if any element is less than the min in sorted section
				min = j                            #set new min
		A[i], A[min] = A[min], A[i]                #swap new minimum with old minimum
	print(A)                                       #print sorted array

b = [120,6,8,20,0,1,5,38,3,-1,-2,-3]               #initialize a list A
selection_sort(b)                                  #run selection sort on A