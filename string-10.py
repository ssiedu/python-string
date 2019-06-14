#program to pring all occurences of a word in given sentence

line="this is python and python is easy and python is wonderful";
sub="python";

end=length=len(line);
lensub=len(sub);

start=count=0

while True :
    pos=line.find(sub,start,end);
    if pos!=-1:
        print(pos);
        count+=1;
        start=pos+lensub;
    else :
        break;

print("Total Occurences of ",sub," : ", count);
        
        
    
