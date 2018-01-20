class MyList(object):
	def __init__(self, *a): self.a=list(a)
	def __len__(self): return len(self.a)
	def __getitem__(self, i): return self.a[i]
	def __setitem__(self, i ,j): self.a[i] = j*2
	def __str__(self):  return str(self.a)
b = MyList(3,4,5)
print b[2]
b[2]=7
print b[2]
print str(b)

# print b.a
# print len(b)
# print b