# arr =[ 8 ,8 ,14 ,10 ,3 ,5 ,14 ,12]
# answer is [8, 7, 6, 4, 3, 2]
arr = [5, 4, 4, 2, 2, 8]
result = []

def cutthesticks(arr):
  while(len(arr)>=1):
    arr= [x-min(arr) for x in arr]
    result.append(len(arr))
    arr = [x for x in arr if x!=0] # using list comprehension to remove the all cutted sticks 
    print(arr)


cutthesticks(arr)
print(result)