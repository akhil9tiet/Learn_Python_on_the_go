# Display median of a list
def median(lst):
    lst.sort()
    lst_len = len(lst)
    mid = int(lst_len/2)
    avg = 0
    if lst_len % 2 != 0:
        return lst[mid]
    else:
        avg = float((float(lst[mid]) + (float(lst[mid - 1])))/2)
        return avg

print median([4,5,5,4])