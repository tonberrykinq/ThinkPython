# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="karlo"
__date__ ="$Sep 29, 2011 8:58:52 PM$"

def encapsulate(val, seq):
    if type(seq) == type(""):
        return str(val)
    if type(seq) == type([]):
        return [val]
    return (val,)


def insert_in_middle(val, seq):
    """
      >>> insert_in_middle(2,['a','b','c','d'])
      ['a', 'b', 2, 'c', 'd']
      >>> insert_in_middle('a','karlo')
      'kaarlo'
      >>> insert_in_middle('ca',('ca','kaj','sto'))
      ('ca', 'ca', 'kaj', 'sto')
    """
    middle = len(seq)/2
    return seq[:middle] + encapsulate(val, seq) + seq[middle:]


def insert_at(index, val, seq):
    """
      >>> insert_at(2,'k',['a','b','c','d'])
      ['a', 'b', 'k', 'c', 'd']
      >>> insert_at(1,'a','karlo')
      'kaarlo'
      >>> insert_at(2,'ca',('ca','kaj','sto'))
      ('ca', 'kaj', 'ca', 'sto')
    """
    return seq[:index] + encapsulate(val, seq) + seq[index:]


def reverse(seq):
    """
      >>> reverse([1, 2, 3, 4, 5])
      [5, 4, 3, 2, 1]
      >>> reverse(('shoe', 'my', 'buckle', 2, 1))
      (1, 2, 'buckle', 'my', 'shoe')
      >>> reverse('Python')
      'nohtyP'
    """
    if type(seq) == type(""):
        reverseString = ""
        for i in range(1,len(seq)+1):
            reverseString = reverseString + seq[-1*i]
        return reverseString
    if type(seq) == type([]):
        seq.reverse()
        return seq
    reverseTouple = ()
    for i in range(1,len(seq)+1):
        reverseTouple = reverseTouple + encapsulate(seq[-1*i],seq)
    return reverseTouple


def sort_sequence(seq):
    """
      >>> sort_sequence([3, 4, 6, 7, 8, 2])
      [2, 3, 4, 6, 7, 8]
      >>> sort_sequence((3, 4, 6, 7, 8, 2))
      (2, 3, 4, 6, 7, 8)
      >>> sort_sequence("nothappy")
      'ahnoppty'
    """
    typeOfSeq = ''
    if type(seq) == type(""):
        seqAsList = list(seq)
        typeOfSeq = 's'
    elif type(seq) == type(()):
        seqAsList = list(seq)
        typeOfSeq = 't'
    else:
        seqAsList = seq
        typeOfSeq = 'l'    
    for i in range(len(seqAsList)-1):
        j = i        
        min = seqAsList[i]
        replace = False
        for item in seqAsList[i:]:
            if item < min:                                
                minIndex = j
                min = item
                replace = True
            j = j + 1
        if (replace):
            seqAsList[i], seqAsList[minIndex] = seqAsList[minIndex],seqAsList[i]        
    if typeOfSeq == 's':
        return str(seqAsList)
    elif typeOfSeq == 't':
        return tuple(seqAsList)
    else:
        return seqAsList

def make_empty(seq):
    """
      >>> make_empty([1, 2, 3, 4])
      []
      >>> make_empty(('a', 'b', 'c'))
      ()
      >>> make_empty("No, not me!")
      ''
    """
    if type(seq) == type(""):
        return  ''
    if type(seq) == type([]):
        return []
    return ()
def insert_at_end(val, seq):
    """
    >>> insert_at_end(5, [1, 3, 4, 6])
    [1, 3, 4, 6, 5]
    >>> insert_at_end('x', 'abc')
    'abcx'
    >>> insert_at_end(5, (1, 3, 4, 6))
    (1, 3, 4, 6, 5)
    """
    return seq + encapsulate(val, seq)
def insert_in_front(val, seq):
    """
    >>> insert_in_front(5, [1, 3, 4, 6])
    [5, 1, 3, 4, 6]
    >>> insert_in_front(5, (1, 3, 4, 6))
    (5, 1, 3, 4, 6)
    >>> insert_in_front('x', 'abc')
    'xabc'
    """
    return encapsulate(val,seq) + seq
def index_of(val, seq, start=0):
    """
    >>> index_of(9, [1, 7, 11, 9, 10])
    3
    >>> index_of(5, (1, 2, 4, 5, 6, 10, 5, 5))
    3
    >>> index_of(5, (1, 2, 4, 5, 6, 10, 5, 5), 4)
    6
    >>> index_of('y', 'happy birthday')
    4
    >>> index_of('banana', ['apple', 'banana', 'cherry', 'date'])
    1
    >>> index_of(5, [2, 3, 4])
    -1
    >>> index_of('b', ['apple', 'banana', 'cherry', 'date'])
    -1
    """
    if type(seq) == type(""):
        return  seq.find(val,start)
    else:
        try:
            return seq.index(val,start)
        except ValueError:
            return -1
def remove_at(index, seq):
    """
    >>> remove_at(3, [1, 7, 11, 9, 10])
    [1, 7, 11, 10]
    >>> remove_at(5, (1, 4, 6, 7, 0, 9, 3, 5))
    (1, 4, 6, 7, 0, 3, 5)
    >>> remove_at(2, "Yomrktown")
    'Yorktown'
    """
    return seq[:index] + seq[index+1:]

def remove_val(val, seq):
    """
    >>> remove_val(11, [1, 7, 11, 9, 10])
    [1, 7, 9, 10]
    >>> remove_val(15, (1, 15, 11, 4, 9))
    (1, 11, 4, 9)
    >>> remove_val('what', ('who', 'what', 'when', 'where', 'why', 'how'))
    ('who', 'when', 'where', 'why', 'how')
    >>> remove_val(13, (1, 15, 11, 4, 9))
    (1, 15, 11, 4, 9)
    """
    removeIndex = index_of(val,seq)
    if removeIndex == -1:
        return seq
    else:
        return remove_at(removeIndex,seq)
def remove_all(val, seq):
    """
    >>> remove_all(11, [1, 7, 11, 9, 11, 10, 2, 11])
    [1, 7, 9, 10, 2]
    >>> remove_all('i', 'Mississippi')
    'Msssspp'
    """
    seqRemoved = remove_val(val, seq)
    if seqRemoved == seq:
        return seqRemoved
    else:
        return remove_all(val,seqRemoved)
def count(val, seq):
    """
    >>> count(5, (1, 5, 3, 7, 5, 8, 5))
    3
    >>> count('s', 'Mississippi')
    4
    >>> count((1, 2), [1, 5, (1, 2), 7, (1, 2), 8, 5])
    2
    """
    count = 0
    for item in seq:
        if val == item:
            count = count + 1
    return count
if __name__ == "__main__":
#    import doctest
#    doctest.testmod()
    sort_sequence("nothappy")