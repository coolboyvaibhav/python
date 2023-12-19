
#########merge request
email=input("enter email id :")#g@g.in ,ddd@gmail.com
k,j,d=0,0,0
if len(email)>=6:#1
    if email[0].isalpha():#2  #weather it is alphabet or not 
        if ('@' in email) and (email.count('@')==1):#3
            if (email[-4]=='.') ^ (email[-3]=='.'):#4  # .in or .com
                for i in email:
                    if i==i.isspace():
                        k=1
                    elif i.isalpha():
                        if i==i.upper():#comparing  given with  converted to uppercase case
                            j=1
                    elif i.isdigit():
                        continue#to proceed the loop 
                    elif i=="_" or i=="." or i=="@":
                        continue
                    else:#any other symbol which is not valid to use 
                        d=1
                if k==1 or j==1 or d==1:
                    print("wrong email 5")
                else:
                    print("correct email")
            else:
                print("wrong email 4")
        else:
            print("wrong email 3")
    else:
        print('email wrong 2')
else:
    print('wrong email 1')