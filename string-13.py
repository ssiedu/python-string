#to check whether a email is from gmail.com or not

email=input("Enter Mail Id : ");
domain="gmail.com";
lenmail=len(email);
lendom=len(domain);
print(lenmail);
print(lendom);
sub=email[(lenmail-lendom):];

if domain==sub:
    if lenmail==lendom:
        print("you entered only domain");
    else:
        print("its from gmail.");
else:
    print("its other domain");
