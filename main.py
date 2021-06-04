# inp = int(input())
# lst = [int(input()) for _ in range(inp)]
# X = int(input())
# if X > sum(lst):
#     print('-1')
# l1 = []
# l2 = []
# #print(lst)
# try:
#     for i in range(len(lst)):
#         l1.append(lst[i])
#         if sum(l1)==X:
#             print(len(l1))
#         else:
#             continue
#
# except:
#     for j in range(len(lst) - 1, -1, -1):
#         l2.append(lst[i])
#         if sum(l2)==X:
#             print(len(l2))
#         else:
#             continue

# a = [1,2,2,3,1]
# x = dict((i,a.count(i)) for i in a)
# print(x)
# y = max(x, key=x.get)
# print(a.index(y))
# lst = []
# for i in range(len(a)-1,-1,-1):
#     if a[i]==y:
#         lst.append(i)
# print(lst)

# nums = [2,1,-1]
# for i in range(len(nums)):
#     x, y  =  nums[:i], nums[i+1:]
#
#     if sum(x)==sum(y):
#         print(i)


# T = [[11, 12, 5, 2], [15, 6,10], [10, 8, 12, 5], [12,15,8,6]]
# for r in T:
#     for c in r:
#         print(c,end = " ")
#     print()

# import collections
# dict1 = {'day1': 'Mon', 'day2': 'Tue'}
# dict2 = {'day3': 'Wed', 'day4': 'Thu'}
#
# res = collections.ChainMap(dict2, dict1)
# print(res.maps, '\n')


# inp = int(input())
# base = int(input())
#
# remainder = []
# while(inp>0):
#     remainder.append(str(inp%base))
#
#     inp = inp//base
#
# print(remainder)
# remainder.reverse()
# print(''.join(remainder))

# mat = []
# for i in range(3):
#     x = []
#     for j in range(3):
#         x.append(j)
#     mat.append(x)
# print(mat)

# nums1 = [4,1,2]
# nums2 = [1,3,4,2]
# out = []
# for i in range(len(nums1)):
#     x = nums2.index(nums1[i])
#     if x == len(nums2) - 1: out.append(-1)
#     matched = False
#     for j in range(x + 1, len(nums2)):
#         if nums2[j] > nums1[i]:
#             out.append(nums2[j])
#             matched = True
#             break
#         if not matched:
#             out.append(-1)
# print(out)

# a = list(s)
# for i in range(1, len(a), 2):
#     a[i] = chr(ord(a[i - 1]) + int(a[i]))
# return ''.join(a)

# arr = [2,2,1,2,1]
# arr[0] = arr[0]+1
# print(arr)

# class SeatManager:
#     def __init__(self,int: n):
#         self.lst = list(range(1,n+1))
#         heapify(self.lst)
#
#     def reserve(self) -> int:
#         return heappop(self.lst)
#
#     def unreserve(self, seatNumber: int) -> None:
#         heappush(self.lst, seatNumber)

# arr = [ 1,2,3,7,8,2,4]
# target = int(input())
# try:
#     sum1 = 0
#     for i in range(len(arr)):
#         sum1 += arr[i]
#         if sum1==target:
#             x = i+1
#             break
#
#     sum2 = 0
#     for i in range(len(arr)-1,-1,-1):
#         sum2 +=arr[i]
#         if sum2==target:
#             y = len(arr)-i
#             break
#
#     print(min(x,y))
# except:
#     print(-1)



# s = '111=12'
# p = s.find('=')
# x = s[:p]
# y = s[p+1:]
# print(x , y)
#
# hashtable = {}
# for i in range(len(s)):
#     hashtable[i] = s[i]
#
# print(hashtable)

# arr = [1,0,2,3,0,4,5,0]
# for i in range(1, len(arr)):
#     if arr[i - 1] == 0:
#         arr[i], arr[i + 1] = 0, arr[i]
#         arr.pop()
#
#     else:continue
#
# print(arr)

# n = [1,2,0,6,8,4,6,3,7,7,0]
# for i in range(1,len(n)):
#     if n[i-1]>n[i]:
#         n[i-1]=n[i]
# print(n)

# import math
#
# x= 8
# print(int(math.sqrt(x)))
#
# lo, hi = 1, n
#         while lo < hi:
#             mid = (lo + hi) / 2
#             if guess(mid) == 1:
#                 lo = mid + 1
#             else:
#                 hi = mid
#         return lo

# arr =  [7,1,14,11]
# hashtable = {}
# for i in range(len(arr)):
#     hashtable[i]=arr[i]
#
# for i in hashtable.values():
#     if i*2 in hashtable
#
# print(hashtable)

# s = 'AABCAAADA'
# k = 3
# split_size = int(len(s)/k)
# for i in range(split_size):
#     t = s[:k]
#
#     u = ''
#     for j in t:
#         if j not in u:
#             u+=j
#
#     print(u)
#     s = s[k:]
#---------------------------------------------------------------------------------------
'''s = "i like this program very much"
words = s.split()
#print(words)
string = []
for word in words:
    string.insert(0, word)
    #print(string)
print(' '.join([i for i in string]))'''
#--------------------------------------------------------------------------------------------

# arr = [0,0,1,1,2,3,3,4,4]
#
# writepointer = 1
# for i in range(len(arr)):
#     if arr[i] != arr[i-1]:
#         arr[writepointer] = arr[i]
#         writepointer += 1
#
# print(writepointer)



# nums = [1,4,3,2]
#
# for i in range(len(nums) - 1):
#     lst = []
#     count = 0
#     for j in range(i + 1, len(nums)):
#
#
#         x = min(nums[i], nums[j])
#         count += x
#
#     lst.append(count)
#     print(lst)

# a = "0110"
# b = "1011"
# x, y = int(a, 2), int(b, 2)
# print(x, y)
# print(x^y)
# print((x&y) << 1)

# def addBinary(self, a: str, b: str) -> str:
#     x, y = int(a, 2), int(b, 2)
#     while y:
#         answer = x ^ y
#         carry = (x & y) << 1
#         x, y = answer, carry
#     return bin(x)[2:]
# i, j, summ, carry = len(a)-1, len(b)-1, '', 0
#
# while i >= 0 and j>= 0:
#     d1 = int(a[i])
#     d2 = int(b[i])
#     summ += str((d1+d2+carry)%2)
#     carry = (d1 + d2 + carry)//2
#     i -= 1
#     j -= 1
# i = 0
# j = 0
# while i>=j:
#     summ[i],summ[j] = summ[j],summ[i]
#     i += 1
#     j -= 1
# print(summ)

'''import turtle
a = turtle.Turtle()
a.getscreen().bgcolor('yellow')

a.penup()
a.goto(-200,100)
a.pendown()

a.speed(25)

def star(turtle,size):
    if size<=10:
        return
    else:
        turtle.begin_fill()
        for i in range(5):
            turtle.forward(size)
            star(turtle, size/3)
            turtle.left(216)
            turtle.end_fill()
star(a,360)
turtle.done()'''

# nums = [-1,2,3]
# nums.sort(reverse=True)
# print(nums)

# n = [1,0,2,3,0,4,5,0]
# arr = sorted(n)

# s = "cbaebabacd"
# p = "bac"
# v = s[:len(p)]
# print(sorted(v) == sorted(p))


import math

# x = 12
# y = 3
#
# d = math.sqrt(1 + (x+y)*8)
# if(d - int(d)>0):
#     print(-1)
# else:
#     n = int((-1+d)/2)
#     summ = 0
#     count = 0
#     for i in range(n,0,-1):
#         if(summ+i<=x):
#             count += 1
#             summ += 1
#     print(count)


# from itertools import permutations
# perm = permutations([1, 2, 3])
# Print the obtained permutations
# for i in list(perm):
#     print(i)
# import functools
# n = int(input())
# for i in range(n):
#      lst.append(int(input()))
# s = sum(lst)
# r = functools.reduce(lambda x, y: x | y, lst)
# from collections import Counter
# cnt = Counter("nlaebolko")
# cntBalloon = Counter('balloon')
# print(cntBalloon)
# x = cntBalloon.values()
# y = [i for i in x if i>1]
#print(cntBalloon)
#print([cnt[c] // cntBalloon[c] for c in cntBalloon])
# l1 = ["eat","sleep","repeat"]
# s1 = "geek"
# a = enumerate(l1)
# b = enumerate(s1,2)
# print(list(a))
# print(list(b))

# pattern = "abda"
# string = ['dog', 'cat', 'cat', 'dog']
# #string = s.split()
# #print(set(zip(p, pattern)))
# #string = str.split()
# print(list(zip(pattern, string)))
# mpp, mps = {}, {}
# for i, (p, s) in enumerate(zip(pattern, string)):
#     print(i , p , s)
#     if mpp.get(p) != mps.get(s): print(False)
#     mpp[p] = mps[s] = i
#     print(mps, mpp)


# s = 'asda'
# t = 'fdvs'
# for i,j in zip(s,t):
#     print(i , j)


# import string
# s = "thequickbrownfoxjumpsoverthelaydog"
# for i in string.ascii_lowercase:
#     if i not in s:
#         print(False)
#         break
# print(True)
# t = sorted(s)
# d = ''.join(t)
# f = set(s)
# print(f)
# g = sorted(''.join(f))
# print(g)
# h = ''.join(g)
# print(h)
# x = string.ascii_lowercase
# print(x == h)
#s = "cdbbaabbaa"
#print(s[::-1])
# from collections import Counter
# s = 'fefwef'
# c = Counter(s)
# res = 0
# for k, count in c.items():
#     res += count // 2
# print(len(s) > res * 2)

# hash = set()
# for i in s:
#     if i not in hash:
#         hash.add(i)
#     else:hash.remove(i)
#
# print(len(s)-len(hash)+1 if len(hash)>0 else len(s))

# s1 = "this apple is sweet"
# s = list(s1.split())
# for i in s:
#     print(i)
#     print(s.count(i))

# import string
# s = "A man, a plan, a canal: Panama"
# st = ''.join(i for i in s if i in string.ascii_letters)
# x = st.lower()
# print(x)
#----------------------------------------------------------------------------------------------
'''
import turtle as t
t.speed('fastest')
t.bgcolor('black')
t.pensize(4)

def tree(branchLen, t):
    if branchLen > 4:
        t.forward(branchLen)
        t.right(20)
        tree(branchLen-15, t)
        t.left(40)
        tree(branchLen-15,t)
        t.right(20)
        t.backward(branchLen)

def main():
    myWin = t.Screen()
    t.left(90)
    t.up()
    t.backward(200)
    t.down()
    t.color('green')
    tree(110,t)
    myWin.exitonclick()

main()'''
#------------------------------------------------------------------------------------------
'''
def create_stack():
    stack = []
    return stack
def is_empty():
    return len(stack)==0
def push(stack, item):
    stack.append(item)
    print('pushed item: ' + item)

def pop(stack):
    if is_empty():
        print('empty stack')
    return stack.pop()
stack = create_stack()
push(stack, str(1))
push(stack, str(2))
push(stack, str(3))
push(stack, str(4))
print("popped item: " + pop(stack))
print("stack after popping an element: " + str(stack))
'''
#-----------------------------------------------------------------------------------------------
'''
class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if len(self.queue)==0:
            return None
        self.queue.pop(0)
    def display(self):
        print(self.queue)

    def size(self):
        return len(self.queue)

q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)

q.display()

q.dequeue()

print("After removing an element")
q.display()'''
#----------------------------------------------------------------------------------------
'''
class CircularQueue:
    def __init__(self, k):
        self.k = k
        self.queue = [None] * k
        self.head = self.tail = -1

    def enqueue(self,data):
        if ((self.tail + 1)%self.k == self.head):
            print('The circular queue is full\n')
        elif self.head == -1:
            self.head = 0
            self.tail = 0
            self.queue[self.tail] = data
        else:
            self.tail = (self.tail+1)%self.k
            self.queue[self.tail] = data

    def dequeue(self):
        if self.head==-1:
            print('The circular queue is empty\n')
        elif(self.head==self.tail):
            temp =  self.queue[self.head]
            self.head -= 1
            self.tail -= 1
            return temp
        else:
            temp = self.queue[self.head]
            self.head = (self.head+1)%self.k
            return temp

    def printCQueue(self):
        if (self.head == -1):
            print("No element in the circular queue")

        elif (self.tail >= self.head):
            for i in range(self.head, self.tail + 1):
                print(self.queue[i], end=" ")
            print()
        else:
            for i in range(self.head, self.k):
                print(self.queue[i], end=" ")
                for i in range(0, self.tail + 1):
                    print(self.queue[i], end=" ")
                print()

    # Your MyCircularQueue object will be instantiated and called as such:
obj = CircularQueue(5)
obj.enqueue(1)
obj.enqueue(2)
obj.enqueue(3)
obj.enqueue(4)
obj.enqueue(5)
print("Initial queue")
obj.printCQueue()


obj.dequeue()
obj.dequeue()
print("After removing an element from the queue")
obj.printCQueue()
# print('\n')
# obj.enqueue(6)
# obj.enqueue(7)
# obj.printCQueue()
'''
#--------------------------------------------------------------------------------------------
# import string
# s = "aDxF"
# lst = []
# for c in s:
#     if c in string.ascii_lowercase:
#         lst.append(c.upper())
#     else:
#         lst.append(c.lower())
# print(lst)
# from collections import Counter
# tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"]
# S = Counter(tasks)
# print(S)
# nums = [1,3]
# lst = []
# for i in range(len(nums)-1):
#     xor1 = 0
#     for x in range(i+1,len(nums)):
#         xor1 = xor1^nums[x]
#         lst.append(xor1)
#     j = i+1
#     while(j<len(nums)):
#         xor2 = 0
#         for n in nums[i:j+1]:
#             xor2 = xor2^n
#             lst.append(xor2)
#         j += 1
#print(sum(lst))

# s = '110'
# x = {int(i) for i in s[0:2]}
# print(x)
# #x = int(set(s[0:2]))
# print(x == 1)


#x = {int(i) for i in s[0:2]}
'''
# class Node:
# 
#     # Function to initialise the node object
#     def __init__(self, data):
#         self.data = data  # Assign data
#         self.next = None  # Initialize next as null
# 
# 
# # Linked List class contains a Node object
# class LinkedList:
# 
#     # Function to initialize head
#     def __init__(self):
#         self.head = None
# 
#     # This function prints contents of linked list
#     # starting from head
#     def printList(self):
#         temp = self.head
#         while (temp):
#             print(temp.data)
#             temp = temp.next
# 
# 
# # Code execution starts here
# if __name__ == '__main__':
#     # Start with the empty list
#     llist = LinkedList()
# 
#     llist.head = Node(1)
#     second = Node(2)
#     third = Node(3)
# 
#     llist.head.next = second;  # Link first node with second
#     second.next = third;  # Link second node with the third node
# 
#     llist.printList()
'''
# lst = [1,1,2,3,3,4,6,6,7,8,9,9]
# s = sorted(set(lst))
# print(s)
'''
Following code for testing and understanding:

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):

    def __init__(self):
        a = ListNode(1)
        b = ListNode(2)
        c = ListNode(3)
        d = ListNode(4)

        self.head = a
        a.next = b
        b.next = c
        c.next = d
        d.next = None

        

    def reverseKGroup(self, k):
        dummy_head = ListNode(None)
        temp_res = dummy_head
        temp_res.next = self.head
        left = self.head
        right = self.head

        while True:
            count = 0
            
            for _ in range(k): 
                if right:
                    #print(right.val)
                    right = right.next
                    
                    count += 1
                
            if count == k:
                l1 = left
                l2 = right
                #print(l1.val)
                #print(l2.val)
                
                while count > 0:
                    print(l1.val)
                    print(l2.val)
                    print('start')
                    temp = l1.next
                    l1.next = l2
                    l2 = l1
                    l1 = temp
                    count -= 1
                    print(l1.val)
                    print(l2.val)
                    print('end')
                
                #print(l2.val)
                temp_res.next = l2
                temp_res = left 
                #print(temp_res.next.val)
                #print(temp_res.val)
                left = right 
            else:
                return dummy_head.next

def main():
    s = Solution()
    s.reverseKGroup(3)

if __name__ == "__main__":
    main()
'''
# import string
# s = '123'
# p = '11'
# #print([ord(i)-ord('0') for i in s])
# no1 = 0
# for i in s:
#     no1 = no1*10 +(ord(i)-48)
# print(no1)
# board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
# m = len(board)
# n = len(board[0])
# print([[0]*n]*m)

# s = 'chris alan'
# lst = list(s)
# lst[0] = lst[0].upper()
# for i in range(len(lst)):
#     if lst[i] == ' ':
#         lst[i+1] = lst[i+1].upper()
# print(''.join(lst))

# mat = [[1,2,3],[4,5,6],[7,8,9]]
# k = 1
# m = len(mat)
# n = len(mat[0])
# ans = [[0] * n] * m
# print(ans)
#
#
# for i in range(m):
#     for j in range(n):
#         pref_sum = 0
#         for x in range(max(0, i - k), min(n, i + k + 1)):
#             for y in range(max(0, j - k), min(m, j + k + 1)):
#                 pref_sum += mat[x][y]
#         print(pref_sum)
#'''
# class Node:
#     def __init__(self,item):
#         self.left = None
#         self.right = None
#         self.val = item
#
# def in_order(root):
#     if root:
# from collections import Counter
# jewels = "aA"
# stones = "aAAbbbb"
#
# d = Counter(jewels)
# print(d)
'''
class Node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.val = data

    def inOrder(self):
        if self.left:
            self.left.inOrder()
        print(self.val, end = ' ')
        if self.right:
            self.right.inOrder()

    def preOrder(self):
        print(self.val, end=' ')
        if self.left:
            self.left.preOrder()
        if self.right:
            self.right.preOrder()

    def postOrder(self):
        if self.left:
            self.left.postOrder()
        if self.right:
            self.right.postOrder()
        print(self.val, end=' ')

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print(root.inOrder())
'''
'''
import random
from time import sleep

import pygame


class CarRacing:
    def __init__(self):

        pygame.init()
        self.display_width = 800
        self.display_height = 600
        self.black = (0, 0, 0)
        self.white = (255, 255, 255)
        self.clock = pygame.time.Clock()
        self.gameDisplay = None

        self.initialize()

    def initialize(self):

        self.crashed = False

        self.carImg = pygame.image.load('images/car.png')
        self.car_x_coordinate = (self.display_width * 0.45)
        self.car_y_coordinate = (self.display_height * 0.8)
        self.car_width = 49

        # enemy_car
        self.enemy_car = pygame.image.load('images/enemy_car_1.png')
        self.enemy_car_startx = random.randrange(310, 450)
        self.enemy_car_starty = -600
        self.enemy_car_speed = 5
        self.enemy_car_width = 49
        self.enemy_car_height = 100

        # Background
        self.bgImg = pygame.image.load("images/back_ground.jpg")
        self.bg_x1 = (self.display_width / 2) - (360 / 2)
        self.bg_x2 = (self.display_width / 2) - (360 / 2)
        self.bg_y1 = 0
        self.bg_y2 = -600
        self.bg_speed = 3
        self.count = 0

    def car(self, car_x_coordinate, car_y_coordinate):
        self.gameDisplay.blit(self.carImg, (car_x_coordinate, car_y_coordinate))

    def racing_window(self):
        self.gameDisplay = pygame.display.set_mode((self.display_width, self.display_height))
        pygame.display.set_caption('Car Race -- Robin Bhutani')
        self.run_car()

    def run_car(self):

        while not self.crashed:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.crashed = True
                # print(event)

                if (event.type == pygame.KEYDOWN):
                    if (event.key == pygame.K_LEFT):
                        self.car_x_coordinate -= 50
                    if (event.key == pygame.K_RIGHT):
                        self.car_x_coordinate += 50

            self.gameDisplay.fill(self.black)
            self.back_ground_raod()

            self.run_enemy_car(self.enemy_car_startx, self.enemy_car_starty)
            self.enemy_car_starty += self.enemy_car_speed

            if self.enemy_car_starty > self.display_height:
                self.enemy_car_starty = 0 - self.enemy_car_height
                self.enemy_car_startx = random.randrange(310, 450)

            self.car(self.car_x_coordinate, self.car_y_coordinate)
            self.highscore(self.count)
            self.count += 1
            if (self.count % 100 == 0):
                self.enemy_car_speed += 1
                self.bg_speed += 1

            if self.car_y_coordinate < self.enemy_car_starty + self.enemy_car_height:
                if self.car_x_coordinate > self.enemy_car_startx and self.car_x_coordinate < self.enemy_car_startx + self.enemy_car_width or self.car_x_coordinate + self.car_width > self.enemy_car_startx and self.car_x_coordinate + self.car_width < self.enemy_car_startx + self.enemy_car_width:
                    self.crashed = True
                    self.display_message("Game Over !!!")
                    #break

            if self.car_x_coordinate < 310 or self.car_x_coordinate > 460:
                self.crashed = True
                self.display_message("Game Over !!!")
                #break

            pygame.display.update()
            self.clock.tick(60)


    def display_message(self, msg):
        font = pygame.font.SysFont("comicsansms", 72, True)
        text = font.render(msg, True, (255, 255, 255))
        self.gameDisplay.blit(text, (400 - text.get_width() // 2, 240 - text.get_height() // 2))
        self.display_credit()
        pygame.display.update()
        self.clock.tick(60)
        sleep(3)
        car_racing.initialize()
        car_racing.racing_window()

    def back_ground_raod(self):
        self.gameDisplay.blit(self.bgImg, (self.bg_x1, self.bg_y1))
        self.gameDisplay.blit(self.bgImg, (self.bg_x2, self.bg_y2))

        self.bg_y1 += self.bg_speed
        self.bg_y2 += self.bg_speed

        if self.bg_y1 >= self.display_height:
            self.bg_y1 = -600

        if self.bg_y2 >= self.display_height:
            self.bg_y2 = -600

    def run_enemy_car(self, thingx, thingy):
        self.gameDisplay.blit(self.enemy_car, (thingx, thingy))

    def highscore(self, count):
        font = pygame.font.SysFont("lucidaconsole", 20)
        text = font.render("Score : " + str(count), True, self.white)
        self.gameDisplay.blit(text, (0, 0))

    def display_credit(self):
        font = pygame.font.SysFont("lucidaconsole", 14)
        text = font.render("Thanks & Regards,", True, self.white)
        self.gameDisplay.blit(text, (600, 520))
        text = font.render("Robin Bhutani", True, self.white)
        self.gameDisplay.blit(text, (600, 540))
        text = font.render("Insta:robin_bhutani", True, self.white)
        self.gameDisplay.blit(text, (600, 560))


if __name__ == '__main__':

    car_racing = CarRacing()
   # while True:
    car_racing.racing_window()
        #x = int(input('enter: '))
        #if x != 1:
            #break
'''
# s = 'abcbaba'
# n = 7
# ans = n
# i, j = 0, 1
# while j < n:
#     if s[i] == s[j]:
#         ans += 1
#         i += 1
#         j += 1
#     else:
#         i += 1
#         j += 1
# print(ans)
# x, y = 0, 2
# while y < n:
#     if s[x] == s[y]:
#         ans += 1
#         x += 1
#         y += 1
#     else:
#         x += 1
#         y += 1
#
#
# print(ans)
# x = filter(lambda i:i%2==0, list(range(1,11)))
# print(list(x))
n = 701
while n > 1:
    x = n%26
    print(x)
    n = n//26
    print(n)







