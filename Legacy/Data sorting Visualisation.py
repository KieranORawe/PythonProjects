import numpy as np
import random
import pygame
import time

pygame.init()
game_display = pygame.display.set_mode((1920,1080),pygame.FULLSCREEN)
pygame.display.set_caption("Data Visulisation")

white = (255,255,255)

#Selection Sort
def selection_sort(x):
    for i in range(len(x)):
        swap = i + np.argmin(x[i:])
        (x[i], x[swap]) = (x[swap], x[i])
        draw(list(x))
        time.sleep(0.01)
    return x

#Bubble Sort
def bubblesort(list):
    for iter_num in range(len(list)-1,0,-1):
        for idx in range(iter_num):
            if list[idx]>list[idx+1]:
                temp = list[idx]
                list[idx] = list[idx+1]
                list[idx+1] = temp
        draw(list)
        time.sleep(0.01)
    return list

#Insertion Sort
def insertion_sort(InputList):
    for i in range(1, len(InputList)):
        j = i-1
        nxt_element = InputList[i]

        while (InputList[j] > nxt_element) and (j >= 0):
            InputList[j+1] = InputList[j]
            j=j-1
        InputList[j+1] = nxt_element
        
        draw(InputList)
        time.sleep(0.01)
        
#Shell Sort
def shellSort(input_list):
    gap = len(input_list) // 2
    while gap > 0:
        for i in range(gap, len(input_list)):
            temp = input_list[i]
            j = i
            while j >= gap and input_list[j - gap] > temp:
                input_list[j] = input_list[j - gap]
                j = j-gap
            input_list[j] = temp
            draw(input_list)
            time.sleep(0.01)
        gap = gap//2
        
#Heap Sort
def heapify(nums, heap_size, root_index):
    largest = root_index
    left_child = (2 * root_index) + 1
    right_child = (2 * root_index) + 2
    if left_child < heap_size and nums[left_child] > nums[largest]:
        largest = left_child
    if right_child < heap_size and nums[right_child] > nums[largest]:
        largest = right_child
    if largest != root_index:
        nums[root_index], nums[largest] = nums[largest], nums[root_index]
        heapify(nums, heap_size, largest)
def heap_sort(nums):
    n = len(nums)
    for i in range(n, -1, -1):
        heapify(nums, n, i)
    for i in range(n - 1, 0, -1):
        nums[i], nums[0] = nums[0], nums[i]
        heapify(nums, i, 0)
        draw(nums)
        time.sleep(0.01)

#Radix Sort
def countingSort(arr, exp1): 
    n = len(arr) 
    output = [0] * (n) 
    count = [0] * (10) 
    for i in range(0, n): 
        index = (arr[i]/exp1) 
        count[ int((index)%10) ] += 1
    for i in range(1,10): 
        count[i] += count[i-1] 
    i = n-1
    while i>=0: 
        index = (arr[i]/exp1) 
        output[ count[ int((index)%10) ] - 1] = arr[i] 
        count[ int((index)%10) ] -= 1
        i -= 1
    i = 0
    for i in range(0,len(arr)): 
        arr[i] = output[i]
        draw(arr)
def radixSort(arr): 
    max1 = max(arr) 
    exp = 1
    while max1/exp > 0: 
        countingSort(arr,exp) 
        exp *= 10

#Draw Graph
def draw (data):
    global game_display
    game_display.fill((0,0,0))
    for i in range(len(data)):
        pygame.draw.rect(game_display,white,[i,1080,1,-data[i]/(size/1080)])
    pygame.display.update()

size = 400

data_list = []
for i in range(1,size+1):
    data_list.append(i)
blank_list = data_list[:]
for i in range(len(data_list)):
    chosen = random.randint(0,size-1)
    data_list[chosen], data_list[i] = data_list[i],data_list[chosen]

draw(data_list)
time.sleep(1)

#selection_sort(np.array(data_list))
#bubblesort(data_list)
#insertion_sort(data_list)
#shellSort(data_list)
#heap_sort(data_list)
radixSort(data_list)
time.sleep(1)
pygame.quit()

