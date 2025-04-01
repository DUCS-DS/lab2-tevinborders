
def monotonic(lst):
    """Return True if lst is monotonic; return False, otherwise."""
    inc = True
    dec = True
    currval=lst[0]
    for i in range(1,len(lst)):
        if lst[i] >= currval:
            dec = False
        if lst[i] < currval:
            inc = False
        currval=lst[i]     
    if inc or dec:
        return True #return True
    else:
        return False

print(monotonic([1,1,3,100]))
print(monotonic([11,1,-9,-10]))
print(monotonic([2,3,2,3]))

#
# Feel free to replace these comments with
# code that tests your function monotonic.
#
