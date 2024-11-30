import random
word_list=['apple','bannana','mango']
lives=6
word=random.choice(word_list)
print(word)
count=0
for i in word:
    #print(i)
    count=count+1
print(count)    
print("you have six chances !!good luck")
p=[]
for i in range(1,count+1):
    p.append('_')
print(p) 
go=False
while not go:
  d=input('guess a letter:').lower()
  for i in range(0,count):
    l=word[i]
    if l==d:
      p[i]=d
  print(p)    
  if d not in word:
    lives-=1
    if lives==0:
      go=True
      print("you lose")
  if '_' not in p:
    go=True
    print(True)           