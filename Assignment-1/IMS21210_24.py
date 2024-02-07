def permute(lst, f=0):
    if f >= len(lst):
        print(lst)
        return None
    else:
        for i in range(len(lst)):
            # swapping the i value of list with other elements
            lst[f], lst[i] = lst[i], lst[f]
            permute(lst, f + 1)
            # swapping them back to their places
            lst[f], lst[i] = lst[i], lst[f]


permute([1, 2, 3])
