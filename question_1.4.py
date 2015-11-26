# -*- coding:utf-8 -*-

#整数の入力


'''
    引数で渡された３つの数字にもとづき、最終的な場所をきめる
    >>> compress_string('3,5,10')
    'west 8'
'''


#cond is list of threshold,
def move(cond,dist):
  if dist < cond[1]:
    return cond[1]

  elif dist > cond[2]:
    return cond[2]

  else dist

cond = map(int,raw_input().split())
point = 0

#リストの一行目がNで、N回にわたってdを代入していく。
#raw_inputが、westがEastの代入

for i in range(cond[0]):
  mv = raw_input().split()
  if mv[0] =='East':
    point = point + move(cond,int(mv[1]))

  else:
    point = point - move(cond,int(mv[1]))

if point < 0:
  print "West "+str(-1*point)
elif point > 0:
  print "East " + str(point)
else:
  print 0 