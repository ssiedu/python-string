#string methods lstrip and rstrip

str1="  hello user  "
print(str1);
print(len(str1));
str2=str1.lstrip();#will remove all leading white spacese
print("________________________________________________________");
print(str2);
print(len(str2));
print("________________________________________________________");
str3=str1.rstrip();
print(str3);
print(len(str3));
print("________________________________________________________");

str4="Thehehre There";
str5=str4.lstrip("The");    #all the possible combination of The,he,h,e,Te etc will be removed from begining
print(str4);#re There (Theheh) will be truncated
print(str5);
print("________________________________________________________");
str6="this is pythonpython";
str7=str6.rstrip("hon");    #all the possible combination of python will be truncated from right side
str8=str6.rstrip("python");
print(str6);
print(str7);    #this is pythonpyt
print(str8);    #this is 
print("________________________________________________________");
