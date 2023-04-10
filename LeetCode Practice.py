# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 13:01:32 2023

@author: Qu.B
"""
import math
import random
import sys
import re
from typing import List
import collections as ListNode


"""2047. Number of Valid Words in a Sentence"""
class Solution:
    def countValidWords(self, sentence: str) -> int:
        words = sentence.split()
        rege = re.compile(r'^([a-z]+\-?[a-z]+[!\,.]?)$|^([a-z]*[!\,.]?)$') 
        count = 0
        for word in words:     
            match = re.match(rege, word)
            if match:
                count += 1
        return count
     

"""557. Reverse Words in a String III"""        
def reverseWords(self, s: str) -> str:
    r = ""
    k = s.split(" ")
    for i in k:            
        r += i[::-1]
        r += " "
    r, result = r[:-1], r[-1]
    return r     
    

def saveThePrisoner(n, m, s):
    # Write your code here
    warn = (m + (s-1)) % n
    
    if warn == 0:
        return n
    
    return warn   


   
    """14. Longest Common Prefix"""
    def longestCommonPrefix(self, strs: List[str]) -> str:
        re = ""
        strs = sorted(strs)
        first = strs[0]
        last = strs[-1]
        for i in range(min(len(first), len(last))):
            if first[i] != last[i]:
                return re
            else:
                re += first[i]
        return re

    """500. Keyboard Row"""
    def findWords(self, words: List[str]) -> List[str]:
        first = "qwertyuiop"
        second = "asdfghjkl"
        third = "zxcvbnm"
        re = []
        for word in words:
          w = word.lower()
          if len(set(first + w)) == len(first) or len(set(second + w)) == len(second) or len(set(third + w)) == len(third):
            re.append(word)

        return re
    
    """20. Valid Parentheses"""
    def isValid(self, s: str) -> bool:
    
        while '()' in s or '{}' in s or '[]' in s:
            s = s.replace('()', '').replace('{}', '').replace( '[]', '')
    
        if len(s) != 0:
            return False
        else:
            return True

    def mergeTwoLists(self, list1:[ListNode], list2:[ListNode]) -> [ListNode]:
        head = tail = ListNode()

        while list1 and list2:
            if list1.val <= list2.val:
                tail.next = list1
                list1 = list1.next
            else: 
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        tail.next = list1 or list2

        return head.next
    
    
    
    """27. Remove Element"""
    def removeElement(self, nums: List[int], val: int) -> int:
        for i in range(nums.count(val)):
            if val in nums:
                nums.remove(val)
        return len(nums)
    
    
    """28. Find the Index of the First Occurrence in a String"""
    def strStr(self, haystack: str, needle: str) -> int:
        i = -1
        if needle in haystack:
            i = haystack.index(needle)
        
        return i
    
    """35. Search Insert Position"""
    def searchInsert(self, nums: List[int], target: int) -> int:

        if target in nums:
            return nums.index(target)

        for i in nums:
            if i > target:
                return nums.index(i)
        return len(nums)
            
            
    """58. Length of Last Word"""
    def lengthOfLastWord(self, s: str) -> int:
        a = s.split(" ")
        while "" in a:
            a.remove("")
        return len(a[-1])
            
    """HackerRank: Counter game"""
    def counterGame(n):
        k = 1
        p = 1
        while n > 1:
            while k < n:
                k = k * 2
            if k > n:
                k = k /2
            if k == n:
                n = n / 2
                p = p * (-1)
            if k < n:
                n = n - k
                p = p * (-1)
            print (n)
        if p < 0:
            return "Louise"
        else:
            return "Richard"


    """HackerRank: Find Digits"""
    def findDigits(n):
        st = str(n)
        cont = 0
        for i in st:
            k = int(i)
            if k > 0:
                if n % k == 0:
                    cont += 1
        return cont


    """HackerRank:Extra Long Factorials"""
    def extraLongFactorials(n):
        k = 0
        for i in range(1, n+1):
            k = k * i
        print (k)
        """or"""
    def extraLongFactorials(n):
        print(math.factorial(n))

    """HackerRank:Lonely Integer"""
    def lonelyinteger(a):
        for i in a:
            if a.count(i) < 2:
                return i


    """HackerRank:Subarray Division"""
    def birthday(s, d, m):
        sum_ = sum(s[:m])
        count = 1 if sum_ == d else 0
        for i in range (m, len(s)):
            sum_ += s[i] - s[i - m]
            if sum_ == d:
                count += 1
        return count
    """HackerRank:luckBalance"""
    def luckBalance(k, contests):
        ret = 0;
        contests.sort(reverse = True, key = lambda x: (x[1], x[0]))
        for i in contests[k:]:
            if i[1] == 1:
                i[0] = i[0] * -1
        ret = sum(i[0] for i in contests)
        return ret
    """HackerRank:Mark and Toys"""
    def maximumToys(prices, k):
        prices.sort()
        count = 0
        for i in prices:
            if k > i:
                count +=1 
                k = k - i
        return count
    """66. Plus One"""
    def plusOne(self, digits: List[int]) -> List[int]:
        g = ""
        a = []
        for i in digits:
            g += str(i)
        k = int(g) + 1
        g = str(k)
        for i in g:
            a.append(int(i))
        return a



    """HackerRank:Tower Breakers"""
    def towerBreakers(n, m):
        ls = []
        for i in range (n):
            ls.append(m)
        player = 1;
        while sum(ls) > len(ls):
            for i in range(len(ls)):
                if( ls[i] > 1):
                    ls[i] = ls[i] - (ls[i] -1)
                    player += 1
        if player % 2 == 0:
            return 1
        if player % 2 != 0:
            return 2
    
    
    def towerBreakers(n, m):
        if m == 1:
            return 2
        if n == 1:
            return 1
    
        return 2 if n % 2 == 0 else 1

if __name__ == '__main__':
    print("Hello World!")
    word = "abs dsa aw! qwe-qwe-"
    #a = Solution()
    #b = a.countValidWords
    #c = saveThePrisoner(3, 7, 3)
    #res = ["c","o","o"]
    #words = ["bella","label","roller"]
    k = 3
    c = [[5, 0], [10, 0], [1, 1], [2, 1], [5, 1], [8, 1]]
    m = 7
    n = 3
    towerBreakers(n, m)
    

    
    

    