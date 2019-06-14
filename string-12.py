#program to print a string that capitalizes every other letter in thr string
str1="python";
length=len(str1);
print("Original String : ",str1);
str2="";

for i in range(0,length,2):
    str2+=str1[i];
    if  i<(length-1):
        str2+=str1[i+1].upper();

print("Capitalized     : ",str2);

