class DataAnalyzer:
    def __init__(self):
        self.data_set = set()
        self.data_dict = {}

    def add_to_set(self, elements):
        self.data_set.update(elements)

    def remove_from_set(self, element):
        self.data_set.discard(element)

    def get_set(self):
        return self.data_set

    def create_dictionary(self, keys, values):
        if len(keys) == len(values):
            self.data_dict = dict(zip(keys, values))

    def update_dictionary(self, key, value):
        self.data_dict[key] = value

    def get_dictionary(self):
        return self.data_dict

    def search_dictionary(self, key):
        return key in self.data_dict

    def remove_from_dictionary(self, key):
        if key in self.data_dict:
            del self.data_dict[key]

# Example usage:
analyzer = DataAnalyzer()
analyzer.add_to_set([1, 2, 3])
print(analyzer.get_set())  # Output: {1, 2, 3}
analyzer.remove_from_set(2)
print(analyzer.get_set())  # Output: {1, 3}
analyzer.create_dictionary(['a', 'b', 'c'], [1, 2, 3])
print(analyzer.get_dictionary())  # Output: {'a': 1, 'b': 2, 'c': 3}
analyzer.update_dictionary('d', 4)
print(analyzer.get_dictionary())  # Output: {'a': 1, 'b': 2, 'c': 3, 'd': 4}
print(analyzer.search_dictionary('b'))  # Output: True
analyzer.remove_from_dictionary('c')
print(analyzer.get_dictionary())  # Output: {'a': 1, 'b': 2, 'd': 4}
