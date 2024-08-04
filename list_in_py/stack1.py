#initializing the empty stack
stack = []

#pushing elements onto the stack
stack.append(1)
stack.append(2)
stack.append(3)

#output after pushing elements
print("stack after pushing elements:", stack)

#popping element from the stack
top_element = stack.pop()
print("popped element:", top_element)
print("stack after popping an element:", stack)

top_element = stack.pop()
print("popped element:", top_element)
print("stack after popping an element:", stack)

top_element = stack.pop()
print("popped element:", top_element)
print("stack after popping an element:", stack)

#checking the last ele without removing it
if stack:
    top_element = stack[-1]
    print("top element:", top_element)
else:
    print("stack is empty")