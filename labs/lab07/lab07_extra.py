""" Optional Questions for Lab 07 """

from lab07 import *

# Q6
def remove_all(link , value):
    """Remove all the nodes containing value. Assume there exists some
    nodes to be removed and the first element is never removed.

    >>> l1 = Link(0, Link(2, Link(2, Link(3, Link(1, Link(2, Link(3)))))))
    >>> print(l1)
    <0 2 2 3 1 2 3>
    >>> remove_all(l1, 2)
    >>> print(l1)
    <0 3 1 3>
    >>> remove_all(l1, 3)
    >>> print(l1)
    <0 1>
    """
    if link is not Link.empty and link.rest is not Link.empty:
        if link.second == value:
            if link.rest.rest:
                link.rest = link.rest.rest
            else:
                link.rest = link.empty
            return remove_all(link, value)
        else:
            return remove_all(link.rest, value)

# Q7
def deep_map_mut(fn, link):
    """Mutates a deep link by replacing each item found with the
    result of calling fn on the item.  Does NOT create new Links (so
    no use of Link's constructor)

    Does not return the modified Link object.

    >>> link1 = Link(3, Link(Link(4), Link(5, Link(6))))
    >>> deep_map_mut(lambda x: x * x, link1)
    >>> print(link1)
    <9 <16> 25 36>
    """
    if isinstance(link.first, Link):
        link.first.first = fn(link.first.first)
    else:
        link.first = fn(link.first)
    if link.rest is not Link.empty:
        deep_map_mut(fn,link.rest)

# Q8
def has_cycle(link):
    """Return whether link contains a cycle.

    >>> s = Link(1, Link(2, Link(3)))
    >>> s.rest.rest.rest = s
    >>> has_cycle(s)
    True
    >>> t = Link(1, Link(2, Link(3)))
    >>> has_cycle(t)
    False
    >>> u = Link(2, Link(2, Link(2)))
    >>> has_cycle(u)
    False
    """
    # Had to take the help of internet gods
    # Not sure i understand how python is doing it in the backend
    links = []
    l = link
    while l.rest is not Link.empty:
        if l in links:
            return True
        links.append(l)
        l = l.rest
        
    return False

def has_cycle_constant(link):
    """Return whether link contains a cycle.

    >>> s = Link(1, Link(2, Link(3)))
    >>> s.rest.rest.rest = s
    >>> has_cycle_constant(s)
    True
    >>> t = Link(1, Link(2, Link(3)))
    >>> has_cycle_constant(t)
    False
    """
    # Didnt try this one
    "*** YOUR CODE HERE ***"

# Q9
def reverse_other(t):
    """Mutates the tree such that nodes on every other (even_indexed) level
    have the labels of their branches all reversed.

    >>> t = Tree(1, [Tree(2), Tree(3), Tree(4)])
    >>> reverse_other(t)
    >>> t
    Tree(1, [Tree(4), Tree(3), Tree(2)])
    >>> t = Tree(1, [Tree(2, [Tree(3, [Tree(4), Tree(5)]), Tree(6, [Tree(7)])]), Tree(8)])
    >>> reverse_other(t)
    >>> t
    Tree(1, [Tree(8, [Tree(3, [Tree(5), Tree(4)]), Tree(6, [Tree(7)])]), Tree(2)])
    """
    height = 0
    def rev(tr, h):
        if tr.is_leaf():
            return
        else:
            #print(height,tr.branches)
            if len(tr.branches) > 1 and h%2 == 0:
                reverse = [x.label for x in tr.branches][::-1]
                for branches, r in zip(tr.branches,reverse):
                    branches.label = r
            h += 1
            for branches in tr.branches:
                rev(branches, h)
    return rev(t, height)
