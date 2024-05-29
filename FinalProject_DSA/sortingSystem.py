import pandas as pd


# _____________________________________bubbleSort________________________________________________
def bubblesort(arr, start, end, column, Type):
    for i in range(start, end):
        flag = True
        for j in range(start, end - i - 1):
            if Type == 'ascending':

                if arr[j][column] > arr[j + 1][column]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
            elif Type == "descending":
                if arr[j][column] < arr[j + 1][column]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]

                    flag = False
        if flag:
            break
    return arr


# _____________________________________HeapSort________________________________________________
def heapify(arr, N, i, column, Type):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    if Type == 'ascending':
        while left < N:
            if right < N and arr[right][column] > arr[left][column]:
                largest = right
            if arr[largest][column] < arr[left][column]:
                largest = left
            if largest == i:
                return
            arr[i], arr[largest] = arr[largest], arr[i]
            i = largest
            left = 2 * i + 1
            right = 2 * i + 2
    elif Type == 'descending':
        largest = i
        if left < N and arr[left][column] < arr[largest][column]:
            largest = left
        if right < N and arr[right][column] < arr[largest][column]:
            largest = right
        if largest != i:
            (arr[i],
             arr[largest]) = (arr[largest],
                              arr[i])
            heapify(arr, N, largest, column, Type)


def heapSort(arr, column, Type):
    N = len(arr)

    for i in range(N // 2 - 1, -1, -1):
        heapify(arr, N, i, column, Type)

    for i in range(N - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0, column, Type)


# _____________________________________insertionSort________________________________________________
def insertionSort(arr, start, end, column, Type):
    flag = True
    for i in range(start + 1, end):
        key = arr[i]
        j = i - 1
        if Type == 'ascending':
            while arr[j][column] > key[column] and j >= start:
                arr[j + 1] = arr[j]
                j = j - 1
                arr[j + 1] = key
        elif Type == 'descending':
            while arr[j][column] < key[column] and j >= start:
                arr[j + 1] = arr[j]
                j = j - 1
                arr[j + 1] = key

            flag = False
    if flag:
        return arr

    return arr


# _____________________________________MergeSort________________________________________________
def merge(array, start, end, mid, column, Type):
    left = array[start:mid + 1]
    right = array[mid + 1:end + 1]

    i = j = 0
    k = start
    if Type == 'ascending':
        while i < len(left) and j < len(right):
            if left[i][column] <= right[j][column]:
                array[k] = left[i]
                i += 1
            else:
                array[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            array[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            array[k] = right[j]
            j += 1
            k += 1
    elif Type == 'descending':
        while i < len(left) and j < len(right):
            if left[i][column] >= right[j][column]:
                array[k] = left[i]
                i += 1
            else:
                array[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            array[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            array[k] = right[j]
            j += 1
            k += 1


def MergeSort(array, start, end, column, Type):
    
    if start < end:
    
        mid = start + (end - start) // 2
        MergeSort(array, start, mid, column, Type)
        MergeSort(array, mid + 1, end, column, Type)
        merge(array, start, end, mid, column, Type)
        

# _____________________________________SelectionSort________________________________________________
def selectionSort(arr, start, end, column, Type):
    for i in range(start, end - 1):
        min_index = i
        for j in range(i + 1, end):
            if Type == 'ascending':
                if arr[j][column] < arr[min_index][column]:
                    min_index = j
            elif Type == 'descending':
                if arr[j][column] > arr[min_index][column]:
                    min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr


# _____________________________________QuickSort________________________________________________
def partition(A, p, r, column, Type):
    x = A[r]
    i = p - 1

    for j in range(p, r):
        if Type == 'ascending':

            if A[j][column] <= x[column]:
                i = i + 1
                A[i], A[j] = A[j], A[i]
        elif Type == 'descending':
            if A[j][column] >= x[column]:
                i = i + 1
                A[i], A[j] = A[j], A[i]

    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1


def QuickSort(A, p, r, column, Type):
    if p < r:
        q = partition(A, p, r, column, Type)
        QuickSort(A, p, q - 1, column, Type)
        QuickSort(A, q + 1, r, column, Type)


# _____________________________________ShellSort________________________________________________

def shellSort(arr, column, Type):
    n = len(arr)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            if Type == 'ascending':
                while j >= gap and arr[j - gap][column] > temp[column]:
                    arr[j] = arr[j - gap]
                    j -= gap
                arr[j] = temp
            elif Type == "descending":
                while j >= gap and arr[j - gap][column] < temp[column]:
                    arr[j] = arr[j - gap]
                    j -= gap
                arr[j] = temp
        gap //= 2
    return arr


# _____________________________________RadixSort________________________________________________
def InsertionSorting(array, exp, column, Type):
    for i in range(1, len(array)):
        j = i - 1
        key = array[i]
        if Type == 'ascending':
            while j >= 0 and key[column] // exp < array[j][column] // exp:
                array[j + 1] = array[j]
                j -= 1
            array[j + 1] = key
        elif Type == 'descending':
            while j >= 0 and key[column] // exp < array[j][column] // exp:
                array[j + 1] = array[j]
                j -= 1
            array[j + 1] = key


def RadixSort(array, column, Type):
    max_element = max(array, key=lambda x: x[column])[column]
    exp = 1
    while max_element // exp > 0:
        InsertionSorting(array, exp, column, Type)
        exp = exp * 10
    return array


# _____________________________________PigeonHoleSort________________________________________________

def pigeonhole(arr, column, Type):
    key = [item[column] for item in arr]
    mini = min(key)
    maxi = max(key)
    rangeValues = maxi - mini + 1
    pigeonholes = [0] * rangeValues
    sortedArray = []

    for item in arr:
        keys = item[column] - mini
        pigeonholes[keys] += 1

    if Type == 'ascending':
        for i in range(rangeValues):
            while pigeonholes[i] > 0:
                value = i + mini
                for item in arr:
                    if item[column] == value:
                        sortedArray.append(item)
                        pigeonholes[i] -= 1
    elif Type == 'descending':
        for i in range(rangeValues - 1, -1, -1):
            while pigeonholes[i] > 0:
                value = i + mini
                for item in arr:
                    if item[column] == value:
                        sortedArray.append(item)
                        pigeonholes[i] -= 1

    return sortedArray


# _____________________________________CountingSort________________________________________________

def countingSort(array, column, Type):
    # Extract the column values to sort
    values = [item[column] for item in array]
    m = max(values)
    n = min(values)

    Count = [0] * (m - n + 1)
    output = [0] * len(array)

    for val in values:
        k = val - n
        Count[k] += 1

    for i in range(1, len(Count)):
        Count[i] += Count[i - 1]
    if Type == 'ascending':
        for i in range(len(array) - 1, -1, -1):
            j = values[i] - n
            Count[j] -= 1
            if 0 <= Count[j] < len(output):
                output[Count[j]] = array[i]
    elif Type == 'descending':
        for i in range(len(array)):
            j = values[i] - n
            output[Count[j]] = array[i]
            Count[j] += 1

    return output


# _____________________________________TimSort________________________________________________
def TimSort(array, start, end, column, Type):
    min_run = 70
    n = len(array)

    for i in range(0, n, min_run):
        end = min((i + n - 1), (n - 1))
        insertionSortTim(array, i, end, column, Type)

    s = min_run
    while s < n:
        for j in range(0, n, s * 2):
            mid = min((n - 1), (j + s - 1))
            if s < mid:
                merge(array, start, mid, end, column, Type)
        s = s * 2
    return array


def insertionSortTim(arr, start, end, column, Type):
    for i in range(start + 1, end + 1):
        j = i
        if Type == 'ascending':
            while j > start and arr[j][column] < arr[j - 1][column]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
                j -= 1
        elif Type == 'descending':
            while j > start and arr[j][column] > arr[j - 1][column]:  # Adjusted for descending order
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
                j -= 1


# _____________________________________CockTail Shaker Sort________________________________________________

def CockTailShaker(arr, n, column, Type):
    if Type == 'ascending':
        flag = True
        for i in range(0, n):
            for j in range(0, n - i - 1):
                if arr[j][column] > arr[j + 1][column]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    flag = True
            if not flag:
                break

            for j in range(n - 2 - i, -1 + i, -1):
                if arr[j][column] > arr[j + 1][column]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    flag = True

            if not flag:
                break
        return arr
    elif Type == 'descending':
        flag = True
        for i in range(0, n):
            for j in range(0, n - i - 1):
                if arr[j][column] < arr[j + 1][column]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    flag = True
            if not flag:
                break

            for j in range(n - 2 - i, -1 + i, -1):
                if arr[j][column] < arr[j + 1][column]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    flag = True

            if not flag:
                break
        return arr


# _____________________________________Multi level Sort________________________________________________

def islower(left, right, list):
    for i in list:
        left_value = left[i]
        right_value = right[i]

        if left_value < right_value:
            return True
        elif left_value > right_value:
            return False

    return False


def Merge(array, start, end, mid, column):
    left = array[start:mid + 1]
    right = array[mid + 1:end + 1]

    i = j = 0
    k = start
    while i < len(left) and j < len(right):
        if islower(left[i], right[j], column):
            array[k] = left[i]
            i += 1
        else:
            array[k] = right[j]
            j += 1
        k += 1
    while i < len(left):
        array[k] = left[i]
        i += 1
        k += 1
    while j < len(right):
        array[k] = right[j]
        j += 1
        k += 1


def MultiLevelSort(array, start, end, column):
    if start < end:
        mid = start + (end - start) // 2
        MultiLevelSort(array, start, mid, column)
        MultiLevelSort(array, mid + 1, end, column)
        Merge(array, start, end, mid, column)


# _____________________________________MAIN MENU CALLING FUNCTIONS________________________________________________
def dataSorter(algo,column,Type):
    

   file1 = 'Resturant1.csv'
   df = pd.read_csv(file1)

   records = df.to_dict('records')
   if algo == 'Bubble Sort':
       records=bubblesort(records, 0, len(records), column, Type)
   elif algo == 'Selection Sort':
       records=selectionSort(records, 0, len(records), column, Type)
   elif algo == 'Merge Sort':
       MergeSort(records, 0, len(records) - 1, column, Type)
   elif algo == 'Quick Sort':
       QuickSort(records,0,len(records)-1,column,Type)
   elif algo == 'Tim Sort':
       records=TimSort(records, 0, len(records), column, Type)
   elif algo == 'Heap Sort':
        heapSort(records, column, Type)
   elif algo == 'Insertion Sort':
       records=insertionSort(records,0, len(records), column, Type)
   elif algo == 'Counting Sort':
       records= countingSort(records, column, Type)
   elif algo == 'Pigeonhole Sort':
       records=pigeonhole(records, column, Type)
   elif algo == 'Radix Sort':
       records = RadixSort(records, column, Type)
   elif algo ==   'CockTail Shaker Sort':
       records=CockTailShaker(records, len(records), column, Type)
   elif algo == 'Shell Sort':
       records = shellSort(records, column, Type)
       
   sorted_df=pd.DataFrame(records)
   sorted_df.to_csv('resturantsort.csv',index=False)    
       
def MultiSort(column):
    file1 = 'Resturant1.csv'
    df = pd.read_csv(file1)
    records = df.to_dict('records')
    MultiLevelSort(records, 0, len(records), column)
    sorteddf=pd.DataFrame(records)
    sorteddf.to_csv('etsy_5.csv',index=False) 
    
    
    
       
       
       
# MergeSort(records, 0, len(records) - 1, columnName, 'descending')

# # QuickSort(records,0,len(records)-1,columnName,'ascending')
# # sortedData = CockTailShaker(records, len(records), columnName, 'descending')
# MultiLevelSort(records,0,len(records)-1,list1)
# sorted_df = pd.DataFrame(records)
# # # Sort the DataFrame using insertion sort
# # insertionSort(df, columnName,0,len(df))

# sorted_df.to_csv("insertionSortFILE1.csv", index=False)
# print("Loaded in CSV")
