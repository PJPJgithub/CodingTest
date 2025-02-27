#https://www.acmicpc.net/problem/2609
#유클리드호제법
import sys
sys.stdin=open("input.txt","r")

def gcd(x,y):
    while(y):
        x,y=y,x%y
    return x

def lcm(x,y):
    return (x*y)//gcd(x,y)

a,b=map(int,input().split())

print(gcd(a,b))
print(lcm(a,b))