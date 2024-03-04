class Node:
    def __init__(self, node_value):
        self.value = node_value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def add_new_node(self, node_value):
        new_node = Node(node_value)
        if not self.head:
            self.head = new_node
            return
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = new_node

    def delete_duplicates_from_list(self):
        no_duplicates_list = []
        current_node = self.head
        prev_node = None

        while current_node:
            if current_node.value in no_duplicates_list:
                prev_node.next = current_node.next
            else:
                no_duplicates_list.append(current_node.value)
                prev_node = current_node
            current_node = current_node.next

    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.value, end=" ")
            current_node = current_node.next


def print_linked_list(list):
    curr_node = list.head
    while curr_node:
        print(curr_node.value, end=' ')
        curr_node = curr_node.next


if __name__ == '__main__':
    linked_list = LinkedList()
    linked_list.add_new_node(34)
    linked_list.add_new_node(21)
    linked_list.add_new_node(23)
    linked_list.add_new_node(18)
    linked_list.add_new_node(54)
    linked_list.add_new_node(23)
    linked_list.add_new_node(21)
    linked_list.add_new_node(34)
    linked_list.add_new_node(18)

    print("list with duplicates:")
    print_linked_list(linked_list)
    linked_list.delete_duplicates_from_list()
    print("\nlist without duplicates:")
    print_linked_list(linked_list)
