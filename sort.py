def insertionSort(arr): 
  
    for i in range(1, len(arr)): 
  
        key = arr[i] 
  
        j = i-1
        while j >=0 and key < arr[j] : 
                arr[j+1] = arr[j] 
                j -= 1
        arr[j+1] = key 
  
  
arr = [12, 11, 13, 5, 6] 
insertionSort(arr) 
print ("排序后的数组:") 
for i in range(len(arr)): 
    print ("%d" %arr[i])
def swap(arr,i,j):
  tmp = arr[i];
  arr[i] = arr[j]
  arr[j]=tmp

def selection_sort(arr):
    for i in range(0,len(arr)):
      min = i
      for j in range(i+1,len(arr)):
        if arr[j] < arr[min]:
          min = j
      swap(arr,i,min)
