class MySet:

    def __init__(self, items):
        """Takes a list of items and builds a set with them, removing
           duplicates if necessary.
        """
        self.collection = items

    def add_item(self, item):
        """ Adds an item to the set if it is not already present. If the
            item is present, do nothing.
        """
        if item not in self.collection:
            self.collection.append(item)

    def remove_item(self, item):
        """ Removes item from the set.  Does nothing if item is not
            in the set.
        """
        if item in self.collection:
            self.collection.remove(item)

    def is_empty(self):
        """Returns True is the set has no members."""
        if len(self.collection) == 0:
            return True

    def has_item(self, item):
        """returns True if item is in the set, False otherwise."""
        if item in self.collection:
            return True
        else:
            return False

    def intersection(self, otherset):
        """Returns a new set that is the intersection of self
           and otherset.
           """
        end_set = []
        for i in otherset:
            if i in self.collection:
                end_set.append(i)
        return end_set

    def union(self, otherset):
        """"Returns a new set that is the union of self and otherset"""
        end_set = []
        end_set = self.collection

        for i in otherset:
            if i not in end_set:
                end_set.append(i)

        return end_set



    def is_subset_of(self, otherset):
        """Returns True if self is a subset of otherset."""
        if otherset in self.collection:
            return True
        else:
            return False

    def is_equal_to(self, otherset):
        """Returns True if self and otherset are equal, i.e.,
           they have the exact same members.
        """
        if self.collection == otherset:
            return True
        else:
            return False

    def is_proper_subset_of(self, otherset):
        """Returns True is self is a *proper* subset of otherset."""
        pass
