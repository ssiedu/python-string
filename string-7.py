#string functions

str="this is python code and python is the easiest language i love python";
str1=str.capitalize();      #makes the first character capitalized
print(str1);
pos1=str.find("python");    #searchs for the first occurance from 0
print(pos1);
pos2=str.find("python",9);   #searchs for the first occurance from 9 to end
print(pos2);
pos3=str.find("python",25,50); #searchs for the first occurance between 25 and 50 returns -1 if search fails
print(pos3);

res1="abc12".isalnum();     #True if alleast one alphabate or digit exists
print(res1);    #True
res2="abc".isalnum();
print(res2);    #True
res3="123".isalnum();
print(res3);    #True
res4="@#@$".isalnum();
print(res4);    #False
res5=" ".isalnum();
print(res5);    #False

res6="abc".isalpha();       #True if all characters are alphabates
print(res6);    #True
res7="123".isalpha();
print(res7);    #False

res8="1234".isdigit();      #True if all characters are digit
print(res8);

res9="abcf55".islower();      #True if all the characters are in lowercase
print(res9);    #True

res10="  ".isspace();        #True if all the characters are spaces
print(res10);   #True

res11="ABC10".isupper();    #True if all the characters are uppercase
print(res11);   #True

res12="abcd".upper();
print(res12);

res13="XYZ".lower();
print(res13);
