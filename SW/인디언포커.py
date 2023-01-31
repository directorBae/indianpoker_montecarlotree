'''
indian poker game program
'''

import math
import random

def computerbetting():

    from random import randrange
    from random import randint
    from random import uniform
    
    global a
    global bp2c
    global bp1c

    m=randrange(2,5)
    n=randrange(1,3)
    
    k =randrange(1,11)
    
    if 10>a>=5:
     if k>=7:
      bp2c=bp1c
     elif 7>=k>=3:
         if bp1c<(p2c/m):
             bp2c=int(round(uniform(bp1c, p2c/m+1)))
             if bp2c<bp1c:
                 bp2c=bp1c
         elif bp1c>(p2c/m):
             bp2c=int(round(uniform((p2c/m), bp1c+1)))
             if bp2c<bp1c:
                 bp2c=bp1c
         else:
             bp2c=bp1c
     else:
        bp2c=0

    elif a<5:
     if k>=3:
      bp2c=bp1c
     elif k>=7:
         if bp1c<(p2c/n):
          bp2c=int(round(uniform(bp1c, (p2c/n)+1)))
          if bp2c<bp1c:
                 bp2c=bp1c
         elif bp1c>(p2c/n):
          bp2c=int(round(uniform((p2c/n), bp1c+1)))
          if bp2c<bp1c:
                 bp2c=bp1c
         else:
             bp2c=bp1c
  
     else:
      bp2c=bp1c
    elif a >= 10:
     if k>=1:
         if bp1c<(p2c):
             bp2c=int(round(uniform(bp1c, p2c+1)))
             if bp2c<bp1c:
                 bp2c=bp1c
         elif bp1c>(p2c):
             bp2c=int(round(uniform(p2c, bp1c+1)))
             if bp2c<bp1c:
                 bp2c=bp1c
         else:
             bp2c=bp1c
     elif k<1:
      bp2c=0
     else:
      bp2c=bp1c   

    if bp1c==0:
        bp2c=0

    elif bp1c==p2c:
        bp2c=bp1c

sump1c=0
sump2c=0

def sigmabp1c():
    global sump1c
    global sump2c
    global bp1c
    global bp2c
    sump1c=bp1c+sump1c

def sigmabp2c():
    global sump1c
    global sump2c
    global bp1c
    global bp2c
    sump2c=bp2c+sump2c

def checkdeck():
    global deck
    if not deck:
        deck=[1,2,3,4,5,6,7,8,9,10,1,2,3,4,5,6,7,8,9,10]

def checkchip():
    global sump1c
    global sump2c
    global bp1c
    global bp2c
    global p1c
    global p2c

    if (p1c-sump1c)<0:
        bp1c=p1c

    elif (p2c-sump2c)<0:
        bp2c=p2c

chip=int(input("초기 칩 수를 입력하세요: "))
print("\n")

p1c=chip
p2c=chip
                            
s=0
i=2
p=0
r=2
o=0
q=2
bp1c=0
bp2c=0
v=0
bcode=1

deck=[1,2,3,4,5,6,7,8,9,10,1,2,3,4,5,6,7,8,9,10]

while i>=s:
 print("\n")
 print(i-1, "번째 라운드")
 print("카드를 뽑습니다, 당신이 P1, 컴퓨터가 P2입니다. ")

 a= random.choice(deck)
 deck.remove (a)
 b= random.choice(deck)
 deck.remove (b)

 p1c=p1c-1
 p2c=p2c-1

 if p1c<=0:
  print("플레이어 2의 최종 승리")
  break
 elif p2c<=0:
  print("플레이어 1의 최종 승리")
  break

 print("상대방이 뽑은 카드는", b, "입니다.")
 print("기본 베팅합니다. P1 현재 칩 수=", p1c, "P2 현재 칩 수=", p2c)
 
 print("베팅하려면 자신이 가진 칩 수 내에서 베팅하고, 포기하려면 0을 누르십시오.")

 while r>=p:
    
  bp1c=int(input())
  sigmabp1c()
  checkchip()
  p1c=p1c-bp1c
  
  if ((bp1c==0) and (a!=10)):
    print("P2 승리")
    if bcode==0:
        p2c=p2c+sump2c+sump1c+v*2
    else:
        p2c=p2c+sump2c+sump1c+1+1
    bcode=1
    v=0
    bp1c=0
    bp2c=0
    sump1c=0
    sump2c=0
    print("나의 카드는", a, "였습니다.")
    break

  elif ((bp1c==0) and (a==10)):
    p1c=p1c-10
    if bcode==0:
        p2c=p2c+sump2c+sump1c+v*2+10
    else:
        p2c=p2c+sump2c+sump1c+1+1+10
    bcode=1
    v=0
    print("페널티: 10 카드를 들고 포기했으므로 10개의 칩이 상대에게로 주어집니다.")
    bp1c=0
    bp2c=0
    sump1c=0
    sump2c=0
    break

  elif ((bp1c!=0) and (sump1c==sump2c)):
   if a>b:
    print("P1 승리")
    if bcode==0:
        p1c=p1c+sump2c+sump1c+v*2
    else:
        p1c=p1c+sump2c+sump1c+1+1
    bcode=1
    v=0
    bp1c=0
    bp2c=0
    print("나의 카드는", a, "였습니다.")
    sump1c=0
    sump2c=0
    break
                            
   elif b>a:
    print("P2 승리")
    if bcode==0:
        p2c=p2c+sump2c+sump1c+v*2
    else:
        p2c=p2c+sump2c+sump1c+1+1
    bcode=1
    v=0
    bp1c=0
    bp2c=0
    print("나의 카드는", a, "였습니다.")
    sump1c=0
    sump2c=0
    break
    
   else:
    print("무승부")
    print("나의 카드는", a, "였습니다.")
    bp1c=0
    bp2c=0
    bcode=0
    v=v+1
    break
  
  else:
   computerbetting()
   sigmabp2c()
   checkchip()
   p2c=p2c-bp2c
   
  print("P2는",bp2c, "만큼 베팅했습니다.")
                            
  if ((sump1c>sump2c) or (sump2c>sump1c)):                     
    if ((bp1c == 0) or (bp2c == 0)):
     code=1
     
     if ((bp2c==0) and (b==10)):
      code=4
         
    elif ((bp1c!=0) and (bp2c!=0)):
     code=3

  elif (sump1c==sump2c):
      code=2
    
  if code==1:
   if bp1c==0:
    print("P2  승리")
    if bcode==0:
        p2c=p2c+sump2c+sump1c+v*2
    else:
        p2c=p2c+sump2c+sump1c+1+1
    bcode=1
    v=0
    bp1c=0
    bp2c=0
    print("나의 카드는", a, "였습니다.")
    sump1c=0
    sump2c=0
    break
    
   elif bp2c==0:
    print("P1 승리")
    if bcode==0:
        p1c=p1c+sump2c+sump1c+v*2
    else:
        p1c=p1c+sump2c+sump1c+1+1
    bcode=1
    v=0
    bp1c=0
    bp2c=0
    print("나의 카드는", a, "였습니다.")
    sump1c=0
    sump2c=0
    break
    
  elif code==2:
   if a>b:
    print("P1 승리")
    if bcode==0:
        p1c=p1c+sump2c+sump1c+v*2
    else:
        p1c=p1c+sump2c+sump1c+1+1
    bcode=1
    v=0
    bp1c=0
    bp2c=0
    print("나의 카드는", a, "였습니다.")
    sump1c=0
    sump2c=0
    break
                            
   elif b>a:
    print("P2 승리")
    if bcode==0:
        p2c=p2c+sump2c+sump1c+v*2
    else:
        p2c=p2c+sump2c+sump1c+1+1
    bcode=1
    v=0
    bp1c=0
    bp2c=0
    print("나의 카드는", a, "였습니다.")
    sump1c=0
    sump2c=0
    break
    
   else:
    print("무승부")
    print("나의 카드는", a, "였습니다.")
    bp1c=0
    bp2c=0
    bcode=0
    v=v+1
    break

  elif code==3:
    r=r+1
    print("베팅을 계속 진행합니다: 더 많이 베팅하거나, 상대가 베팅한 만큼 베팅하십시오.")
 
  elif code==4:
    p2c=p2c-10
    if bcode==0:
        p1c=p1c+sump2c+sump1c+v*2+10
    else:
        p1c=p1c+sump2c+sump1c+1+1+10
    bcode=1
    v=0
    bp1c=0
    bp2c=0
    print("페널티: 10 카드를 들고 포기했으므로 10개의 칩이 상대에게로 주어집니다.")
    sump1c=0
    sump2c=0
    break

 checkdeck()
 
 if p1c<=0:
  print("P2의 최종 승리")
  break
 elif p2c<=0:
  print("P1의 최종 승리")
  break
 else:                           
  i=i+1
