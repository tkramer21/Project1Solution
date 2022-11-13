from typing import TypeVar  # For use in type hinting

# Type Declarations
T = TypeVar('T')  # generic type
SLL = TypeVar('SLL')  # forward declared
Node = TypeVar('Node')  # forward declare `Node` type


class SLLNode:
    """
    Node implementation
    Do not modify.
    """

    __slots__ = ['val', 'next']

    def __init__(self, value: T, next: Node = None) -> None:
        """
        Initialize an SLL Node
        :param value: value held by node
        :param next: reference to the next node in the SLL
        :return: None
        """
        self.val = value
        self.next = next

    def __str__(self) -> str:
        """
        Overloads `str()` method to cast nodes to strings
        return: string
        """
        return '(Node: ' + str(self.val) + ' )'

    def __repr__(self) -> str:
        """
        Overloads `repr()` method for use in debugging
        return: string
        """
        return '(Node: ' + str(self.val) + ' )'

    def __eq__(self, other: Node) -> bool:
        """
        Overloads `==` operator to compare nodes
        :param other: right operand of `==`
        :return: bool
        """
        return self is other if other is not None else False
        # return self.val == other.val if other is not None else False


class SinglyLinkedList:
    """
    Implementation of an SLL
    """

    __slots__ = ['head', 'tail']

    def __init__(self) -> None:
        """
        Initializes an SLL
        :return: None
        DO NOT MODIFY THIS FUNCTION
        """
        self.head = None
        self.tail = None

    def __repr__(self) -> str:
        """
        Represents an SLL as a string
        DO NOT MODIFY THIS FUNCTION
        """
        return self.to_string()

    def __eq__(self, other: SLL) -> bool:
        """
        Overloads `==` operator to compare SLLs
        :param other: right hand operand of `==`
        :return: `True` if equal, else `False`
        DO NOT MODIFY THIS FUNCTION
        """
        comp = lambda n1, n2: n1 == n2 and (comp(n1.next, n2.next) if (n1 and n2) else True)
        return comp(self.head, other.head)

    # ============ Modify below ============ #
    def push(self, value: T) -> None:
        """
        Pushes an SLLNode to the end of the list
        :param value: value to push to the list
        :return: None
        """

        new_node = SLLNode(value)

        if self.head == None:  # list is empty
            self.head = new_node
            self.tail = new_node

        else:
            self.tail.next = new_node
            self.tail = new_node

    def to_string(self) -> str:
        """
        Converts an SLL to a string
        :return: string representation of the linked list
        """
        str = ""
        if self.head != None:
            curnode = self.head
            while curnode != None:
                str += curnode.val
                if curnode.next != None:
                    str += " --> "
                curnode = curnode.next
            return str
        else:
            return "None"

    def length(self) -> int:
        """
        Determines number of nodes in the list
        :return: number of nodes in list
        """
        curnode = self.head
        cnt = 0
        while curnode != None:
            cnt += 1
            curnode = curnode.next
        return cnt

    def sum_list(self) -> T:
        """
        Sums the values in the list
        :return: sum of values in list
        """
        curnode = self.head
        if self.head != None:
            val = self.head.val
            while curnode != None:
                if curnode == self.head:
                    curnode = curnode.next
                else:
                    val += curnode.val
                    curnode = curnode.next

            return val
        else:
            return None

    # change exmple git
    def remove(self, value: T) -> bool:
        """
        Removes the first node containing `value` from the SLL
        :param value: value to remove
        :return: True if a node was removed, False otherwise
        """
        curnode = self.head
        while curnode != None:
            if curnode.next != None and curnode.next.val == value:
                if curnode.next == self.tail:
                    self.tail = curnode

                curnode.next = curnode.next.next
                return True
            elif curnode.val == value and self.length() == 1:
                self.head = None
                self.tail = None
                return True

            curnode = curnode.next
        return False

    def remove_all(self, value: T) -> bool:
        """
        Removes all instances of a node containing `value` from the SLL
        :param value: value to remove
        :return: True if a node was removed, False otherwise
        """
        curnode = self.head
        bool = False
        while curnode != None:
            if curnode.next != None and curnode.next.val == value:
                if curnode.next == self.tail:
                    self.tail = curnode

                curnode.next = curnode.next.next
                bool = True
            elif curnode.val == value and self.length() == 1:
                self.head = None
                self.tail = None
                bool = True

            elif self.head.val == value:
                self.head = self.head.next
                bool = True

            curnode = curnode.next
        return bool

    def search(self, value: T) -> bool:
        """
        Searches the SLL for a node containing `value`
        :param value: value to search for
        :return: `True` if found, else `False`
        """

        curnode = self.head
        while curnode != None:
            if curnode.val == value:
                return True
            curnode = curnode.next
        return False

    def count(self, value: T) -> int:
        """
        Returns the number of occurrences of `value` in this list
        :param value: value to count
        :return: number of times the value occurred
        """

        curnode = self.head
        cnt = 0
        while curnode != None:
            if curnode.val == value:
                cnt += 1
            curnode = curnode.next
        return cnt


def reverse(data: SLL) -> None:
    """
    Reverses the data
    :param data: an SLL
    :return: None
    """
    curnode = data.head
    prev = None
    data.tail = curnode

    while curnode != None:
        next = curnode.next
        curnode.next = prev
        prev = curnode
        curnode = next
    data.head = prev
