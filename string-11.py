#string to check a palindrome
#comparing 1st and last, 2nd and 2nd last till mid
str = input("Enter A String To Check For A Palindrome => ");
mid=len(str)//2;
#print(mid);
j=-1;
isPalindrome=True;

for i in range(0,mid):
    #print(i,",",j);
    #print(str[i],"==",str[j])
    if(str[i]!=str[j]):
        #print(str[i],"==",str[j])
        isPalindrome=False;
    j-=1;
if isPalindrome:
    print("Yes ! Its A Palindrome");
else:
    print("No ! Its Not A Palindrome");



