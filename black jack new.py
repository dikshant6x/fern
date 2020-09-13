#!/usr/bin/env python
# coding: utf-8
# In[1]:
#black jack game

def play_again():
    x=input('do you want to play another hand(yes or no)')
    if x.lower()=='yes':
        print('NEW GAME')
        start()
    else :
        print('thank you for playing ')
        return
    
        
def end():
    while True:
#        print('d')
        continue


# In[2]:


def deck():
    from random import randint
    group=randint(1,4)
    #print(group)
    if group==1:
        e=hearts()
    if group==2:
        e=clubs()
    if group==3:
        e=spades()
    if group==4:
        e=diamonds()
    return e


# In[3]:


list1=[1,2,3,4,5,6,7,8,9,10,11,12,13]
list2=[1,2,3,4,5,6,7,8,9,10,11,12,13]
list3=[1,2,3,4,5,6,7,8,9,10,11,12,13]
list4=[1,2,3,4,5,6,7,8,9,10,11,12,13]
def lis1(rand):
    ind=list1.index(rand)
    list1.pop(ind)
def lis2(rand):
    ind=list2.index(rand)
    list2.pop(ind)
def lis3(rand):
    ind=list3.index(rand)
    list3.pop(ind)
def lis4(rand):
    ind=list4.index(rand)
    list4.pop(ind)
    
from random import randint    
    
def hearts():
    h=randint(1,13)
    #print(h)
    gr='hearts'
    if h in list1:
        lis1(h)
        #print(list1)
        if h==1:
            print(gr+' ace')    
        elif h==2:
            print(f'{gr} {h}')
        
        elif h==3:
            print(f'{gr} {h}') 
            
        elif h==4:
            print(f'{gr} {h}') 
           
        elif h==5:
            print(f'{gr} {h}')
         
        elif h==6:
            print(f'{gr} {h}')
        
        elif h==7:
            print(f'{gr} {h}')
    
        elif h==8:
            print(f'{gr} {h}')
               
        elif h==9:
            print(f'{gr} {h}') 
                
        elif h==10:
            print(f'{gr} {h}') 
                 
        elif h==11:
            print(gr+' jack')  
            h=10
        elif h==12:
            print(gr+' queen') 
            h=10
        elif h==13:
            print(gr+' king')
            h=10
    else:
        deck()    
    return h    
def clubs():
    h=randint(1,13)
    #print(h)
    gr='clubs'
    if h in list2:
        lis2(h)
        #print(list2)
        if h==1:
            print(gr+' ace')
            
        elif h==2:
            print(f'{gr} {h}')
            
        elif h==3:
            print(f'{gr} {h}')
                
        elif h==4:
            print(f'{gr} {h}')
               
        elif h==5:
            print(f'{gr} {h}')
            
        elif h==6:
            print(f'{gr} {h}')
            
        elif h==7:
            print(f'{gr} {h}')
            
        elif h==8:
            print(f'{gr} {h}')
            
        elif h==9:
            print(f'{gr} {h}')
                
        elif h==10:
            print(f'{gr} {h}')
            
        elif h==11:
            print(gr+' jack') 
            h=10
        elif h==12:
            print(gr+' queen')
            h=10  
        elif h==13:
            print(gr+' king')  
            h=10
    else:
        deck() 
    return h    
def spades():
    h=randint(1,13)
    #print(h)
    gr='spades'
    if h in list3:
        lis3(h)
        #print(list3)
        if h==1:
            print(gr+' ace')
        elif h==2:
            print(f'{gr} {h}')
        elif h==3:
            print(f'{gr} {h}')  
        elif h==4:
            print(f'{gr} {h}') 
        elif h==5:
            print(f'{gr} {h}')
        elif h==6:
            print(f'{gr} {h}')
        elif h==7:
            print(f'{gr} {h}')
        elif h==8:
            print(f'{gr} {h}')
        elif h==9:
            print(f'{gr} {h}') 
        elif h==10:
            print(f'{gr} {h}')
        elif h==11:
            print(gr+' jack')
            h=h-1
        elif h==12:
            print(gr+' queen')
            h= h-2
        elif h==13:
            print(gr+' king')
            h= h-3
    else:
        deck()
    return h    
def diamonds():
    h=randint(1,13)
    #print(h)
    gr='diamonds'
    
    if h in list4:
        lis4(h)
        #print(list4)
        if h==1:
            print(gr+' ace')
            return h
        elif h==2:
            print(f'{gr} {h}')
            return h
        elif h==3:
            print(f'{gr} {h}')  
            return h
        elif h==4:
            print(f'{gr} {h}') 
            return h
        elif h==5:
            print(f'{gr} {h}')
            return h
        elif h==6:
            print(f'{gr} {h}')
            return h
        elif h==7:
            print(f'{gr} {h}')
            return h
        elif h==8:
            print(f'{gr} {h}')
        elif h==9:
            print(f'{gr} {h}') 
            return h
        elif h==10:
            print(f'{gr} {h}')   
            return h
        elif h==11:
            print(gr+' jack')    
            return h-1
        elif h==12:
            print(gr+' queen')  
            h= h-2
        elif h==13:
            print(gr+' king') 
            h= h-3
    else:
        deck()       
    return h    


# In[4]:


class dealer():
    def __init__(self):
        pass
    def hit(self):
        ds=deck()
        return ds
    
class player():
    def __init__(self,chipbalance):
        self.chipb=chipbalance
        pass
    def chiploss(self,chips=2):
        ub=self.chipb-chips
        self.chipb=ub
        return ub
            
            
    def hit(self):
        ps=deck()
        return ps
    def chipwin(self,chips=2):
        ub=self.chipb+chips
        self.chipb=ub
        return ub
    

    
def ace():
    print('ace is here')
    f=int(input('what do you want to choose(1 or 11)'))
    if f==1 or f==11:
        pass
    else:
        ace()
    return f   
        
def check(number):
    if number==1:
        ace()
    else:
        pass


# In[5]:


de=dealer()
pl=player(10)


# In[6]:


def start():
    print('Welcome to BlackJack! Get as close to 21 as you can without going over!\n    Dealer hits until she reaches 17. Aces count as 1 or 11.')
    print('PLAYER CARDS')
    p1=pl.hit()
    if p1==1:
        p1=ace()
#    print(p1)
    p2=pl.hit()
    if p2==1:
        p2=ace()
#    print(p2)
    print('--'*20)
    print('DEALER CARDS')
    d1=de.hit()
    if d1==1:
        d1=ace()
#    print(d1)
    print('face down')
    print('--'*20)
    #print(type(p1))
    #print(type(p2))
    total=p1+p2
    print(f'player card_total_is {total}')
    while True:    
        if total<21:
            a=input('Player:want to hit(yes or no) ')
            if a.lower()=='yes':
                print('PLAYER')
                p3=pl.hit()
                if p3==1:
                    p3=ace()
                total=total+p3
                print(total)
            elif a.lower()=='no':
                break
            else:
                print('try again')
        elif total==21:
            break
        else:
9            print('PLAYER BUSTED')
            print('-'*20)
            pl.chiploss()
            if pl.chipb>1:
                play_again()
            else:
                end()
                
            
            #break
    print('-'*20)        
    print('DEALER')
    d2=de.hit()
    if d2==1:
        d2=ace()
#    print(d2)
    tot=d1+d2
    print(tot)
    while True:
        if tot<17:  #dealer total less than 17 case
            d3=de.hit()
            if d3==1:
                d3=ace()
#            print(d3)
            tot=tot+d3
            print(tot)
        elif tot>=17 and tot<=total:
            d4=de.hit()
            if d4==1:
                d4=ace()
#            print(d4)
            tot=tot+d4
            print(tot)
#            b=input('dealer:want to hit')
#            if b.lower()=='yes':
#                if tot>total and tot<=21:
#                    print('Dealer wins')
#                    break
#                elif tot>21:
#                    print('Dealer busted')
#                    break
        elif tot>total and tot<=21:
            print('DEALER WINS')
            print(' '*20)
            pl.chiploss()
            if pl.chipb>1:
                play_again()
            #break
        elif tot>21:
            print('DEALER BUSTED')
            print('-'*20)
            pl.chipwin()
            if pl.chipb>1:
                play_again()
            
            break

            
            
            


# In[ ]:


start()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




