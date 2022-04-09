# Linked List Node
class Node:
	def __init__(self, data=None, next=None):
		self.data = data
		self.next = next


# Function
def detectCycle(head):

	# take two pointers slow n fast
	slow = fast = head

	while fast and fast.next:

		# move slow 1 step
		slow = slow.next

		# move fast 2 steps
		fast = fast.next.next

		# if pointers meet
		if slow == fast:
			return True

	# if pointers dont meet
	return False


if __name__ == '__main__':

	head = None
	for i in reversed(range(5)):
		head = Node(i + 1, head)

	# insert cycle
	# put '#' for below line if u dont want cycle
	head.next.next.next.next.next = head.next.next

	if detectCycle(head):
		print('Cycle Found')
	else:
		print('No Cycle Found')
