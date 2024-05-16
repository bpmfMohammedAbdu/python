x= int(input ("inter the value of x axise"))
y= int(input ("inter the value of y axise"))
print (f"the cordinats of(x,y)are =({x},{y})")
if x > -1000 and x < 1000 and y > -1000 and y < 1000:
    if x > 0 and y > 0:
        print (1)
    elif x<0 and y < 0:
         print (3)
         print  ("          |      ")
         print  ("          |      ")
         print  ("    ______|______")
         print  ("       |__|      ")
         print(f"({x},{y}) |      ")
         print  ("          |      ")
    elif x > 0 and y < 0:
         print (4)
    elif x < 0 and y >0:
        print (2)
    else:
        print (f"at origin {x,y}")    
else :
    print (" but the value of x or y not allow to inter  above 1000 or below -1000 ")
    print ("plese cheke x or y cordinate(x,y) and tray agin !")
