if __name__ == '__main__':
    N = int(input())
    lst=[]
    for i in range(N):
        bank=input().split()
        if(bank[0]=="insert"):
            lst.insert(int(bank[1]),int(bank[2]))
        if(bank[0]=="print"):
            print(lst)
        if(bank[0]=="remove"):
            lst.remove(int(bank[1]))
        if(bank[0]=="append"):
            lst.append(int(bank[1]))
        if(bank[0]=="sort"):
            lst.sort()
        if(bank[0]=="pop"):
            lst.pop()
        if(bank[0]=="reverse"):
            lst.reverse()    
                            
                            
    