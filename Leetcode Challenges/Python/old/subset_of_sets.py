"""
This is a solution of a problem from the book - Cracking the Coding Interview

Write a method to return all subsets of a set. 

"""
import copy

def get_subsets(given_set, index = None):

    # base case - get the subset for the cases 1 less than given length 
    if index is None:
        index = len(given_set) - 1
    if index == -1:
        return [[]]

    old_subs = get_subsets(given_set, index - 1)
    new_subs = [] # stores the subsets for the given case
    item = given_set[index]
    
    for val in old_subs:
        new_subs.append(val)
        entry = copy.deepcopy(val)
        entry.append(item)
        new_subs.append(entry)
    return new_subs


def subsets(given_set):
    result = [[]]
    for item in given_set:
        for subset in result:
            result = result + [list(subset) + [item]]
    return result


if __name__ == '__main__':
    print(get_subsets([1, 2, 3]))
    print(subsets([1, 2, 3, 4]))