user =["nathan" ,"2313 ", "geez ","pass231","abebe","092313133","miki","pl3s34dontHaceM3"]
user_name = user [:-1:2] #to separet password from user name
user_password =  user[1::2]#to separt password from user name
#to change list to dictionary
#dictionary ={ user_name[i]:user_password[i] for i in range (len(user_name)) }
dictionary ={"nathan":"2313","geez":"pass231","abebe":"092313133","miki":"pl3s34dontHaceM3"}
chance = 0
while chance < 5 :

    u_name =input ("enter your name ")#to accept users name from the yousr 
    u_password =input ("enter your password ")#to accept users password from the yousr
    if u_name in user and dictionary [u_name]==u_password:#condition to cheke u_name and u_password
        print ("wellcome to Gtst company !")
    else:
        print("Inccorict login!")
        chance += 1# chance =chance + 1
print ("you are limeted ")
