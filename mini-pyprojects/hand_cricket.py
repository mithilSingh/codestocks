import random
toss=['heads','tails']

r=random.choice(toss)
while True:
	a=input('go for toss..... choose heads or tails -->')
	
	
	if a==r:
		print('you won the toss')
		while True:
			b=input('choose batting or balling > ')
			if b=='batting' or b=='balling':
				break
			else :
				print('please choose batting or balling')
		
		break
	elif a!= 'heads' and a!='tails':
		print('please choose head or tails')
	elif a!=r:
		print ('you lost the toss')
		ra=random.choice(['batting','balling'])
		print ('computer chooses ',ra)
		break
if a==r:
	ra=''
if a!=r:
	b=''
rum=0
rum2=0

if b=='batting' or ra=='balling':

	mr=[1,2,3,4,5,6]
	print ('go for batting ...enter runs from 1 to 6')
	while True:
		try:
			ranrun=random.choice(mr)
			run=int(input('enter your runs which u want to score:'))
			if run not in mr:
				print('choose runs from 1 to 6')
			elif run==ranrun:
				print ('umpire:out !!!')
				break
			elif run!=ranrun:
				mr.append(run)
				print ('umpire:',run,'runs')
				rum+=run
				mr.append(run)
				print ('total score',rum)
			print('-------------------------------------')
		except:
			print('please enter your choice from 1to 6')
	print ('your final score',rum)
	print('=========================================================')
	print ('now go for balling ...enter runs from 1 to 6')
	
	while True:
		try:
			mr2=[1,2,3,4,5,6]
			ranrun2=random.choice(mr2)
			run2=int(input('enter your runs which u think will be scored:'))
			
			if ranrun2 not in mr:
				print('choose runs from 1 to 6')
			elif run2==ranrun2:
				print ('umpire:out !!!')
				break
				
			elif run2!=ranrun2:
				rum2+=ranrun2
				print ('umpire:',ranrun2,'runs')
				print ('total run scored by bot',rum2)
			if rum2>rum:
				break
			print('-------------------------------------')
		except:
			print('please enter your choice from 1to 6')
			
	print('final runs scored by Bot',rum2)
	print('=========================================================')
		
elif b=='balling' or ra=='batting':
	print ('go for balling ...enter runs from 1 to 6')
	while True:
		try:
			mr=[1,2,3,4,5,6]
			ranrun=random.choice(mr)
			run=int(input('enter your runs which u think will be scored:'))
			
			if ranrun not in mr:
				print('choose runs from 1 to 6')
			elif run==ranrun:
				print ('umpire:out !!!')
				break
			elif run!=ranrun:
				rum2+=ranrun
				print ('umpire:',ranrun,'runs')
				print ('total score',rum2)
			print('-------------------------------------')
		except:
			print('please enter your choice from 1to 6')
			
	print('final runs scored by Bot',rum2)	
	print('=========================================================')	
	print ('go for batting ...enter runs from 1 to 6')
	mr2=[1,2,3,4,5,6]
	while True:		
		try:
			ranrun2=random.choice(mr2)
			run2=int(input('enter your runs which u want to score:'))
			if run2 not in mr2:
				print('choose runs from 1 to 6')
			elif run2==ranrun2:
				print ('umpire:out !!!')
				break
			elif run2!=ranrun2:
				mr2.append(run2)
				print ('umpire:',run2,'runs')
				rum+=run2
				print ('total score',rum)
			if rum>rum2:
				break
		except:
			print('please enter your choice from 1to 6')
		
	print ('your final score',rum)
	print('=========================================================')
	

if rum==rum2:
	print(' match draw')
elif  rum<rum2:
	print('bot won')
elif rum>rum2:
	print('you won')
