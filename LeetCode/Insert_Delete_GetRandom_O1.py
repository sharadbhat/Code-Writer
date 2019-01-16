# LeetCode
# https://leetcode.com/problems/insert-delete-getrandom-o1/

from random import choice

class RandomizedSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.s = set()

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.s:
            self.s.add(val)
            return True
        return False

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.s:
            self.s.remove(val)
            return True
        return False

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        return choice([i for i in self.s])


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
