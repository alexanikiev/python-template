# mylinkedlist.py


class Node:
    """
    Node is a class that represents a single node in a linked list.
    """

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    """
    "LinkedList is a class that represents a singly linked list.
    """

    def __init__(self):
        self.head = None

    def append(self, data):
        """
        append adds a new node with the given data to the end of the
        linked list.
        """
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def prepend(self, data):
        """
        prepend adds a new node with the given data to the beginning of the
        linked list.
        """
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete(self, data):
        """
        delete removes the first node with the given data from the
        linked list.
        """
        temp = self.head

        if temp and temp.data == data:
            self.head = temp.next
            temp = None
            return

        prev = None
        while temp and temp.data != data:
            prev = temp
            temp = temp.next

        if temp is None:
            return

        prev.next = temp.next
        temp = None

    def display(self):
        """
        display prints the linked list in a readable format.
        """
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")


# Example usage:
# llist = LinkedList()
# llist.append(1)
# llist.append(2)
# llist.append(3)
# llist.prepend(0)
# llist.display()  # Output: 0 -> 1 -> 2 -> 3 -> None

# llist.delete(2)
# llist.display()  # Output: 0 -> 1 -> 3 -> None
