# Python program to find maximum contiguous subarray

def kadane(a,size):

	max_sum =a[0]
	cur_max = a[0]

	for i in range(1,size):
		cur_max = max(a[i], cur_max + a[i])
		max_sum = max(max_sum,cur_max)
		return max_sum

a = [1 , 2, -1, 3, 4, -2]
print('Maximum contiguous sum is' , kadane(a,len(a)))
