a=int(raw_input())
dd={'mon':'0', 'tues':'1', 'wed':'2', 'thurs':'3', 'fri':'4', 'sat':'5', 'sun':'6'}
for i in range(0,a):
	b=raw_input().strip().split(" ")
	dat=int(b[0])
	dy=b[1]
	c=[]
	if (dat>=28 and dat<=31):
		if (dy in dd):
			
			dy=int(dd[dy])
			if (dat==28):
				for i in range(0,7):
					c.append("4")
				print " ".join(c)	
					
			elif (dat==29):
				for i in range(0,7):
					if (i==dy):
						c.append("5")
					else:
						c.append("4")
				print " ".join(c)
			

			elif (dat==30):
				for i in range(0,7):
					if (dy>=6):
						if (i==0):
							c.append("5")

						elif (i==dy):
							c.append("5")
						else:
							c.append("4")
					elif (i==dy):
						c.append("5")
					elif (i==dy+1):
						c.append("5")
					else:
						c.append("4")
				print " ".join(c)

			elif (dat==31):
				for i in range(0,7):
					if (dy==5):
						if (i==0):
							c.append("5")
						elif (i==dy):
							c.append("5")
						elif (i==dy+1):
							c.append("5")
						else:
							c.append("4")
					elif (dy==6):
						if (i==0):
							c.append("5")
						elif (i==1):
							c.append("5")
						elif (i==6):
							c.append("5")
						else:
							c.append("4")
					elif (i==dy):
						c.append("5")
					elif (i==dy+1):
						c.append("5")
					elif (i==dy+2):
						c.append("5")
					else:
						c.append("4")
				print " ".join(c)
	else:
		break			