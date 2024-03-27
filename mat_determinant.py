'''
Created on Sep 17, 2021

@author: bborade
'''
def main():
    limit = int(input())
    mat = []
    for _ in range(limit):
        temp = []
        for _ in range(limit):
            temp.append(input())
    mat.append(temp)
    print(mat)
    

main()