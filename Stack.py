
class Stack:

    def __init__(self, some_list=[]):
        self.stack_list = some_list

    def isEmpty(self):
        if len(self.stack_list) == 0:
            return True
        else:
            return False

    def push(self, item):
        self.stack_list.append(item)

    def pop(self):
        if len(self.stack_list) > 0:
            return self.stack_list.pop()
        else:
            return

    def peek(self):
        index = len(self.stack_list)
        if index == 0:
            return
        else:
            return self.stack_list[index - 1]

    def size(self):
        return len(self.stack_list)


if __name__ == '__main__':
    pass
