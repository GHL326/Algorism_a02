import pyvisalgo as va


DATA_FILE = "data/elementary_sort.json"

vis = va.visualizer("bubble_sort")

def Bubble_Sort(array):
    n = len(array)

    for b in range(n):
        for i in range(0,n-b-1):
            if array [i] > array[i+1]:
                array[i], array[i+1] = array [i+1], array[i]
                vis.update(array, [i, i+1], [i, i+1])
