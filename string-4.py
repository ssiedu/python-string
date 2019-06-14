#display a string
#first-char    last-char
#second-char   second-last

text=input('enter a string')
start=0;
for end in range(-1,(-len(text)-1),-1):
    print(text[end],'\t',text[start]);
    start+=1;
