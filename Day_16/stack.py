stack = []

## Push elements onto the stack
stack.append(1)
stack.append(2)
stack.append(3)
stack.append(4)
print("Stack after pushing elements:", stack)

#peak at the top element of the stack
top_element = stack[-1]
print("Top element of the stack:", top_element)

#pop elements from the stack
popped_element = stack.pop()
print("Popped element:", popped_element)

#stack after popping an element
print("Stack after popping an element:", stack)

#isEmpty check
is_empty = not bool(stack)
print("Is the stack empty?", is_empty)  

#size of the stack
stack_size = len(stack)
print("Size of the stack:", stack_size)