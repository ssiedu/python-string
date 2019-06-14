#iterating string in backward direction

text=input('enter a string=>');
length=len(text);
print(length);
print('_______________________________________________________________');
#for i in range(-length,0):
for i in range(-1,-length-1,-1):    #range(start,end,increment/decrement) #start from -1 i.e. last -length-1 i.e. first
    print(text[i]);

print('_______________________________________________________________');
