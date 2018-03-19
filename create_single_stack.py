class MyStack():

    class MyStackError(IndexError):
        '''Raise an Index Error when try to pop from empty stack'''

    class StackNode():

        def __init__(self, data):
            self.data = data
            self.next = None

    def __init__(self):
        self.top = None

    def isEmpty(self):
        return self.top == None

    def pop(self):
        if self.isEmpty():
            raise IndexError("You just tried to pop from an empty stack. Empty Stack Error")
        item = self.top.data
        self.top = self.top.next
        #set top to the next node down from top bc will pop off
        return item

    def push(self, item):
        t = self.StackNode(item)
        t.next = self.top
        #new node T needs next pointer set to old top
        self.top = t
        #set new top pointer to new node t

    def peek(self):
        if self.isEmpty():
            raise IndexError("Nothing to peek at the stack is empty")
        return self.top.data


stack = MyStack()

print stack

stack.push("I will be the node at the bottom of the stack")
stack.push("I will be the 2nd to the the bottom of the stack")
stack.push("I will be the top of the stack")

print stack.pop()
print stack.peek()
print stack.pop()
print stack.peek()
print stack.pop()

print stack.isEmpty()
print stack.peek()
print stack.isEmpty()


# first = "First entry to go on the stack"
# second = "Second entry to go on the stack"

# stack.push("sneaky extra push to make the peek exception test fail")
# stack.push("sneaky extra push to make the pop exception test fail")
# stack.push(first)
# stack.push(second)

# result = stack.pop()

# if result == second:
#     print "Cool, we got back '%s' when expected" % second

# result2 = stack.pop()

# if result2 == first:
#     print "Cool, and '%s' too" % first

# expecting this to fail:
# try:
#     result3 = stack.pop()
#     print "** What?!?  There's still data to pop from the stack?"
#     print "   Got back: '%s'" % result3
# except MyStack.MyStackEmptyError:
#     print "Oh good, we got a stack empty error when popping too much"

# try:
#     result4 = stack.peek()
#     print "** What?!?  There's still data to peek on the stack?"
#     print "   Got back: '%s'" % result4
# except ValueError:
#     print "*** shouldn't have gotten ValueError"
# except MyStack.MyStackEmptyError:
#     print "Oh good, we got a stack empty error when peeking too late"
# except IndexError:
#     print "Got an IndexError that's not a MyStackLookupError"
