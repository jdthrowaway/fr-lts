from random import randrange
xlist=[]
ylist=[]
zlist=[]

options = {0 : 'face ',2 : 'r leg',3 : 'l leg',4 : 'tummy',5 : 'pubis',6 : 'chest',7 : 'chest',8 : 'r arm',9 : 'l arm',1 : 'arse '}
options1 = {0 : 'take pic',2 : 'kneel 2x',3 : 'selfie',4 : 'read 5x',5 : 'draw 2 \u2661',6 : 'wear clamps x3',7 : 'mouth open x5',9 : 'draw 3x dicks',8 : 'dildo in mouth x2',1 : 'spank ass x10'}

key=[
['dumb slut', 'cum here (\u2191 to mouth)', 'slut', 'slap me hard', 'choke me (on neck)', 'TOY (mouth as O)', 'facefuck me', 'public use', 'stupid cunt', 'I \u2661 rape'],
['fuck me!', 'public use', 'anal only', 'dick \u2191', 'free anal', 'BBC only', 'Cum inside (\u2191)', 'breed me', 'hurt me', 'open 24/7'],
['fuckhole', 'slut', 'please use me', '\u2162 +1', 'tie me down', 'whip me', 'use me', 'dumb slut', 'I \u2661 daddy', 'rape cunt'],
['fuckhole', 'slut', 'please use me', '\u2162 +1', 'tie me down', 'whip me', 'use me', 'dumb slut', 'I \u2661 daddy', 'rape cunt'],
['use my holes', 'public cum dump', 'punish me please', 'rapemeat', 'breed me', 'fill me with cum', 'cum dump', 'rape doll', 'fuck doll', 'make me cry'],
['no dignity', 'desperate hole', 'please?', 'cum rag', 'slave', 'pig', 'grope me', 'Im your slut', 'worthless', 'bimbo'],
['yes daddy', '\u2661 on nipples', 'hurt my tits', 'cock obsessed', 'property of daddy', 'asking for it', 'dumb whore', 'cum all over me', 'cock drunk', 'cum rag'],
['yes daddy', '\u2661 on nipples', 'hurt my tits', 'cock obsessed', 'property of daddy', 'asking for it', 'dumb whore', 'cum all over me', 'cock drunk', 'cum rag'],
['cock whore', 'I \u2661 cum', 'for handjob', 'tie me down', 'make me beg', 'FUCK SLUT', 'handcuff me', 'made to serve', 'slave cunt', 'abuse me'],
['cock whore', 'I \u2661 cum', 'for handjob', 'tie me down', 'make me beg', 'FUCK SLUT', 'handcuff me', 'made to serve', 'slave cunt', 'abuse me'],
]

while list(set([1,2,3,4,5,6,7,8,9,0])^set(ylist)):
    xlist.append(randrange(10))
    ylist.append(randrange(10))
    zlist.append(randrange(10))

sorted=sorted(zip(ylist,xlist,zlist), key=lambda x: x[1])
listnew=[list(t) for t in zip(*sorted)]
xlist=listnew[0]
ylist=listnew[1]
zlist=listnew[2]

print("{: ^10} {: ^20} {: ^40}".format('Where', 'What', 'Specials'))
for i in range(len(ylist)):
   speciallist=''
   if ((xlist[i] == 2) or ((xlist[i-1] == 2) and (i > 0))):
      speciallist=speciallist+'kneel '
   if ((xlist[i] == 6) or ((xlist[i-1] == 6) and (i > 0)) or ((xlist[i-2] == 6) and (i > 1))):
      speciallist=speciallist+'wear clamps '
   if ((xlist[i] == 7) or ((xlist[i-1] == 7) and (i > 0)) or ((xlist[i-2] == 7) and (i > 1)) or ((xlist[i-3] == 7) and (i > 2)) or ((xlist[i-4] == 7) and (i > 3))):
      speciallist=speciallist+'mouth open wide '
   if ((xlist[i] == 8) or (xlist[i-1] == 8 and (i > 0))):
      speciallist=speciallist+'dildo in mouth '

   if len(speciallist) > 0:
      if xlist[i]  in [2,6,7,8]:
           print("{: ^10} {: ^20} {: ^40}".format(options[ylist[i]],'"'+key[ylist[i]][zlist[i]]+'"',' '+speciallist))
      else:
          speciallist=speciallist+' '+options1[xlist[i]]
          print("{: ^10} {: ^20} {: ^40}".format(options[ylist[i]],'"'+key[ylist[i]][zlist[i]]+'"',' '+speciallist))
   else:
      speciallist=options1[xlist[i]]
      print("{: ^10} {: ^20} {: ^40}".format(options[ylist[i]],'"'+key[ylist[i]][zlist[i]]+'"',' '+speciallist))
