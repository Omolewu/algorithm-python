# Code to calculate century

def calcentury (year):
    cenNum =0
    if 1 <= year and year <= 100:
         cenNum = 1
    
    elif year % 100 != 0:
        centNum = (year // 100) + 1
       
    else:
        centNum = year // 100
    return centNum

print(calcentury (2024))