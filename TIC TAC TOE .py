#!/usr/bin/env python
# coding: utf-8

# In[1]:
#tic tac toe game

x_o=input('what will u prefer = X or O')
if x_o.lower()=='x':
    p1='X'
    p2='O'
elif x_o.lower()=='o':
    p1='O'
    p2='X'

    
    
def board(tup):
    print(tup)
    a=tup[0]
    b=tup[1]
    c=tup[2]
    d=tup[3]
    e=tup[4]
    f=tup[5]
    g=tup[6]
    h=tup[7]
    i=tup[8]
    print('    |   |   ')
    print(f'  {a} |  {b}| {c}  ')
    print('    |   |   ')
    print('-------------')
    print('    |   |')
    print(f'  {d} |  {e}| {f}')
    print('    |   |')
    print('-------------')
    print('    |   |   ')
    print(f'  {g} |  {h}| {i}   ')
    print('    |   |   ')
    
    if a==b==c=='X' or a==d==g=='X' or a==e==i=='X' or b==e==h=='X' or c==e==g=='X' or c==f==i=='X' or d==e==f=='X' or g==h==i=='X':
        result()
        
    elif a==b==c=='O' or a==d==g=='O'or a==e==i=='O' or b==e==h=='O' or c==e==g=='O' or c==f==i=='O' or d==e==f=='O'or g==h==i=='O':
        result1()


# In[2]:


def lis1(list,position_1):
    index1=list.index(position_1)
    print(index1)
    list.pop(index1)
    print(list)
def lis2(list,position_2):
    index2=list.index(position_2)
    list.pop(index2)
    print(list)


# In[6]:


def p1cal(position_1,a,b,c,d,e,f,g,h,i):    
    
    if position_1 in [1,2,3,4,5,6,7,8,9]:
        if position_1==1:
            a=p1
        elif position_1==2:
            b=p1
                
        elif position_1==3:
            c=p1
            
        elif position_1==4:
             d=p1 
               
        elif position_1==5:
             e=p1
               
        elif position_1==6:
             f=p1
               
        elif position_1==7:
             g=p1    
              
        elif position_1==8:
             h=p1    
              
        elif position_1==9:
             i=p1   
    return a,b,c,d,e,f,g,h,i
  
               
            
def p2cal(position_2,tup1):

    a=tup1[0]
    b=tup1[1]
    c=tup1[2]
    d=tup1[3]
    e=tup1[4]
    f=tup1[5]
    g=tup1[6]
    h=tup1[7]
    i=tup1[8]
    if position_2 in [1,2,3,4,5,6,7,8,9]:
        if position_2==1:
            a=p2
        elif position_2==2:
             b=p2
        elif position_2==3:
             c=p2
        elif position_2==4:
             d=p2    
        elif position_2==5:
             e=p2
        elif position_2==6:
             f=p2
        elif position_2==7:
             g=p2    
        elif position_2==8:
             h=p2    
        elif position_2==9:
            i=p2        
    

    return a,b,c,d,e,f,g,h,i


# In[7]:


def main():
    
    position_1 = int(input('Player-1 : enter the position '))
    print(position_1)
    lis1(list,position_1)
    if ctr==1:
        
        a=' '
        b=' '
        c=' '
        d=' '
        e=' '
        f=' '
        g=' '
        h=' '
        i=' '


        board(p1cal(position_1,a,b,c,d,e,f,g,h,i))
    if ctr!=1:
        yz=xy[2]
        a=yz[0]
        b=yz[1]
        c=yz[2]
        d=yz[3]
        e=yz[4]
        f=yz[5]
        g=yz[6]
        h=yz[7]
        i=yz[8]
        board(p1cal(position_1,a,b,c,d,e,f,g,h,i))
    
    position_2 = int(input('Player-2 : enter the position '))
    lis2(list,position_2)
    board(p2cal(position_2,p1cal(position_1,a,b,c,d,e,f,g,h,i)))
    xyz=p2cal(position_2,p1cal(position_1,a,b,c,d,e,f,g,h,i))
    return position_1,position_2,xyz


# In[ ]:


list=[1,2,3,4,5,6,7,8,9]
ctr=1
while ctr<10:
    xy=main()
    
    ctr=ctr+1
    
    def result():
        if (x_o.lower()=='x'):
            print('Player 1 wins')
       
        else:
            print('Player 2 wins')
        return 
  
        
    def result1():
        if (x_o.lower()=='o'):
            print('Player 1 wins')
        
        else:
            print('Player 2 wins')
        
    if ctr==9:
        print('DRAW')
        break


# In[ ]:




