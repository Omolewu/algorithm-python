#Given am array of integer, find the pairs of adjacent elements that has the largest product and return that product

# input: [2, -3, -4, 5, 4, 6, 0, 7, 8, 9]

def adjacentarray(arrnum):
    lproduct = 0
    for n in range(len(arrnum)-1):
        if arrnum[n] * arrnum[n+1] > lproduct:
            lproduct = arrnum[n] * arrnum[n+1]
    
    return lproduct 

print(adjacentarray([2, -3, -4, 5, 4, 6, 0, 7, 8, 9]))   