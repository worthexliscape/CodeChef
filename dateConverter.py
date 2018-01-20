a = "01/10/2017"


def dateConverter(val):
	dd,mm,yy=a.split("/")
	ddd=int(dd)
	mmm=int(mm)
	yyy=int(yy)
	d={'1':'January', '2':'February', '3':'March', '4':'April', '5':'May', '6':'June', '7':'July', '8':'August', '9':'September', '10':'October', '11':'November', '12':"December"}
	if(str(mmm) in d):
		mmm=d[str(mmm)]
		
	print str(ddd)+" "+mmm+", "+str(yyy)
	return ddd,mmm,yyy 
	# return val

dateConverter(a)

