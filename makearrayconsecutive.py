#Make Array Consecutive 
#input [2,5,7,9,11]
def makearrayconsecutive(arr):
    s =0
    arr.sort()
    for i in range(len(arr)-1):
        if arr[i+1] -  arr[i] > 1:
            s += arr[i+1] -  arr[i] - 1
    return s

print(makearrayconsecutive([6,2,3,8]))