stack = []

# Push operation
def push(item):
    stack.append(item)
    print(item, "pushed into stack")

# Pop operation
def pop():
    if len(stack) == 0:
        print("Stack Underflow")
    else:
        item = stack.pop()
        print(item, "popped from stack")

# Peek operation
def peek():
    if len(stack) == 0:
        print("Stack is empty")
    else:
        print("Top element is:", stack[-1])

# Display operation
def display():
    if len(stack) == 0:
        print("Stack is empty")
    else:
        print("Stack elements:", stack)


# Main program
push(10)
push(20)
push(30)

display()
peek()

pop()
display()

peek()