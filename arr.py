import cPickle
inFridge=["ketchup", "mustard", "relish"]
print inFridge

File=open("fridge.txt","w")
cPickle.dump(inFridge, File)
File.close()

inFridge.append("pickles")
print inFridge
File=open("fridge.txt","w")
cPickle.dump(inFridge, File)
File.close()

File=open("fridge.txt",'r')
inFridgeFile=cPickle.load(File)
File.close()
print inFridgeFile