from collections import Counter 
#Create a list containing just counts of each distinct element
    freq = [s.count(letter) for letter in set(s) ]
    #If all values the same, then return 'YES'
    if max(freq)-min(freq) == 0:
        return 'YES'
    #If difference between highest count and lowest count is 1
    #and there is only one letter with highest count, 
    #then return 'YES' (because we can subtract one of these 
    #letters and max=min , i.e. all counts are the same)
    elif freq.count(max(freq)) == 1 and max(freq) - min(freq) == 1:
        return 'YES'
    #If the minimum count is 1
    #then remove this letter, and check whether all the other
    #counts are the same
    elif freq.count(min(freq)) == 1:
        freq.remove(min(freq))
        if max(freq)-min(freq) == 0:
            return 'YES'
        else:
            return 'NO'
    else:
        return 'NO'