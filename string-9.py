#program to count uppercase,lowercase,alphabates and digits in given string

str=input("Enter a String---> ");
lc=0;
uc=0;
alpha=0;
digits=0;
spaces=0;
for ch in str :
    if ch.islower():
            lc+=1;
    elif ch.isupper():
            uc+=1;
    elif ch.isspace():
            spaces+=1;
    elif ch.isdigit():
            digits+=1;

    if ch.isalpha():
        alpha+=1;

print("Total Length     : ",len(str));    
print("Total LowerCase  : ",lc);
print("Total UpperCase  : ",uc);
print("Total Alphabates : ",alpha);
print("Total Digits     : ",digits);
print("Total Spaces     : ",spaces);
