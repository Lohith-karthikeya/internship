class ListManipulator:
    def __init__(self):
        self.internal_list = []

    def add_elements(self, elements):
        self.internal_list.extend(elements)

    def remove_duplicates(self):
        self.internal_list = list(set(self.internal_list))

    def reverse_list(self):
        self.internal_list.reverse()

    def sort_list(self):
        self.internal_list.sort()

    def get_unique_elements(self):
        return list(set(self.internal_list))

    def remove_element(self, element):
        if element in self.internal_list:
            self.internal_list.remove(element)

    def get_list(self):
        return self.internal_list

# Example usage:
manipulator = ListManipulator()
manipulator.add_elements([1, 2, 3, 4, 3, 2, 1])
manipulator.remove_duplicates()
print(manipulator.get_list())  # Output: [1, 2, 3, 4]
manipulator.reverse_list()
print(manipulator.get_list())  # Output: [4, 3, 2, 1]
manipulator.sort_list()
print(manipulator.get_list())  # Output: [1, 2, 3, 4]
print(manipulator.get_unique_elements())  # Output: [1, 2, 3, 4]
manipulator.remove_element(3)
print(manipulator.get_list())  # Output: [1, 2, 4]
