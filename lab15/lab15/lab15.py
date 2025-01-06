# Note: The Tree implemenation is at the bottom of the file
# Please read the docstrings to learn how to interact with a Tree object.

def berry_finder(t):
    """Returns True if t contains a node with the value 'berry' and
    False otherwise.

    >>> scrat = Tree('berry')
    >>> berry_finder(scrat)
    True
    >>> sproul = Tree('roots', [Tree('branch1', [Tree('leaf'), Tree('berry')]), Tree('branch2')])
    >>> berry_finder(sproul)
    True
    >>> numbers = Tree(1, [Tree(2), Tree(3, [Tree(4), Tree(5)]), Tree(6, [Tree(7)])])
    >>> berry_finder(numbers)
    False
    >>> t = Tree(1, [Tree('berry',[Tree('not berry')])])
    >>> berry_finder(t)
    True
    """
    if t.is_leaf():
        return (type(t.label) == str) and ('berry' == t.label)
    else:
        for branch in t.branches:
            if berry_finder(branch):
                return True
    return False




def height(t):
    """Return the height of a Tree.

    >>> t = Tree(3, [Tree(5, [Tree(1)]), Tree(2)])
    >>> height(t)
    2
    >>> t = Tree(3, [Tree(1), Tree(2, [Tree(5, [Tree(6)]), Tree(1)])])
    >>> height(t)
    3
    """
    def find_max(t, level=0):
        if t.is_leaf():
            return 0
        else:
            val = level
            for branch in t.branches:
                max = 1 + height(branch)
        return max

def max_path_sum(t):
    """Return the maximum path sum of the Tree.

    >>> t = Tree(1, [Tree(5, [Tree(1), Tree(3)]), Tree(10)])
    >>> max_path_sum(t)
    11
    """
    paths = []
    def find_sum(t, paths):
        if t.is_leaf():
            return t.label
        else:
            sum = 0
            for branch in t.branches:
                paths.append(max_path_sum(branch))



def find_path(t, x):
    """
    >>> t = Tree(2, [Tree(7, [Tree(3), Tree(6, [Tree(5), Tree(11)])] ), Tree(15)])
    >>> find_path(t, 5)
    [2, 7, 6, 5]
    >>> find_path(t, 10)  # returns None
    """
    # Highlight the code and press Ctrl-'/' to unccomment the code all at once
    # if _____________________________:
    #     return _____________________________
    # _____________________________:
    #     path = ______________________
    #     if _____________________________:
    #         return _____________________________
    def search(t, path):
        if t.is_leaf():
            return path
        else:
            path.append()
            for branch in t.branches:


# Optional Question
def has_path(t, word):
    """Return whether there is a path in a Tree where the entries along the path
    spell out a particular word.

    >>> greetings = Tree('h', [Tree('i'),
    ...                        Tree('e', [Tree('l', [Tree('l', [Tree('o')])]),
    ...                                   Tree('y')])])
    >>> print(greetings)
    h
      i
      e
        l
          l
            o
        y
    >>> has_path(greetings, 'h')
    True
    >>> has_path(greetings, 'i')
    False
    >>> has_path(greetings, 'hi')
    True
    >>> has_path(greetings, 'hello')
    True
    >>> has_path(greetings, 'hey')
    True
    >>> has_path(greetings, 'bye')
    False
    >>> has_path(greetings, 'hint')
    False
    """
    assert len(word) > 0, 'no path for empty word.'
    # Write your code here


class Tree:

    def __init__(self, label, branches=[]):
        """
        A Tree is constructed by passing a label and an optional *list* of branches.
        The list passed must only contain objects of the Tree class.
        """
        self.label = label
        for branch in branches:
            assert isinstance(branch, Tree)
        self.branches = list(branches)

    def is_leaf(self):
        """
        Returns a boolean, true if this Tree object is a leaf (has no branches), false otherwise.
        """
        return not self.branches

    def __repr__(self):
        if self.branches:
            branch_str = ', ' + repr(self.branches)
        else:
            branch_str = ''
        return f'Tree({self.label}{branch_str})'

    def __str__(self):
    
        def indented(self):
            lines = []
            for b in self.branches:
                for line in indented(b):
                    lines.append('  ' + line)
            return [str(self.label)] + lines

        return '\n'.join(indented(self))


t = Tree(3, [Tree(5, [Tree(1)]), Tree(2)])
height(t)
