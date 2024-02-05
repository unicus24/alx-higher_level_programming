'''

Write a class MyList that inherits from list:

Public instance method: def print_sorted(self): that prints the list, but sorted (ascending sort)
You can assume that all the elements of the list will be of type int
You are not allowed to import any module

'''

#!/usr/bin/python3

class MyList(list):
    """Custom list type intended to only contain integers."""

    def print_sorted(self):
        """Prints MyList lists in ascending order by value.

        """
        sorted_list = self[:]
        sorted_list.sort()
        print(sorted_list)
