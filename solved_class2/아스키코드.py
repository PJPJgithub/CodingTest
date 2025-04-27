#https://www.acmicpc.net/problem/11654
'''
x -> 아스키코드 : ord()
아스키코드 -> x : chr()
'''
import sys
sys.stdin=open("input.txt",'r')

x=input()

print(ord(x))