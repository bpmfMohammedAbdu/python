print ("well come to GPA maker!")
print ("inter the creadt houre of each subjuct ")
math=int (input ("the creadt houre of applied math1 ="))
phy=int (input ("the creadt houre of physics ="))
english=int (input ("the creadt houre of english ="))
chemistry=int (input ("the creadt houre of chemistry ="))
civic=int (input ("the creadt houre of civic  ="))
python=int (input ("the creadt houre of python =")) 
#subject result resiver from the user
sub=print (input ("inter the total subject you take "))
mathresult=int(input ("inter your total result in applied math"))
phyresult=int(input ("inter your total result in physics"))
englishresult=int(input ("inter your total result in english"))
chemistryresult=int(input ("inter your total result in chemistry"))
civicresult=int(input ("inter your total result in civic"))
pythonresult=int(input ("inter your total result in python"))
#multiplication or subjuct result and creadt houre
'''mathr=mathresult*math
phyr=phyresult*phy
englishr=englishresult*english
chemistryr=chemistryresult*chemistry
civicr=civicresult*civic
pythonr=pythonresult*python
''' 
#gerading system
if mathresult > 0 and mathresult <= 100:
    if mathresult >= 90 and mathresult <=100 :
        m =(" A+")
        m1=4
    elif  mathresult >= 85 and mathresult <=89:
        m= ("  is A")
        m1=4
    elif mathresult >= 80 and mathresult <=84:
        m= (" A-")
        m1=3.75
    elif mathresult >=75 and mathresult <=80:
        m= (" B+")
        m1=3.5     
    elif mathresult >=70 and mathresult <=74:
        m= (" B") 
        m1=3    
    elif mathresult >=65 and mathresult <=69:
        m= (" B-") 
        m1=2.75
    elif mathresult >=60 and mathresult <=64:
        m= ("C+") 
        m1=2.5
    elif mathresult >=50 and mathresult <=69:
        m= (" C") 
        m1=2
    elif mathresult >45 and mathresult <=49:
        m= (" C-") 
        m1=1.75
    elif mathresult >=40 and mathresult <=45:
        m= (" D") 
        m1=1
    elif mathresult >=0 and mathresult <=39:
        m= ("F") 
        m1=0 
else :
    m="incorect tray agin" 
#grading system
if  phyresult > 0 and phyresult <= 100:
    if phyresult >= 90 and phyresult <=100 :
        p =(" A+")
        p1=4
    elif  phyresult >= 85 and phyresult <=89:
        p= (" A")
        m1=4
    elif phyresult >= 80 and phyresult <=84:
        p= (" A-")
        p1=3.75
    elif phyresult >=75 and phyresult <=80:
        p= (" B+")
        p1=3.5     
    elif phyresult >=70 and phyresult <=74:
        p= ("B") 
        p1=3    
    elif phyresult >=65 and phyresult <=69:
        p= (" B-") 
        p1=2.75
    elif phyresult >=60 and phyresult <=64:
        p= ("C+") 
        p1=2.5
    elif phyresult >=50 and phyresult <=69:
        p=(" C") 
        p1=2
    elif phyresult >45 and phyresult <=49:
        p= (" C-") 
        p1=1.75
    elif phyresult >=40 and phyresult <=45:
        p= (" D") 
        p1=1
    elif phyresult >=0 and phyresult <=39:
        p= ("F") 
        p1=0 
else :
    p="incorect tray agin" 
#grading system
if  englishresult > 0 and englishresult <= 100:
    if englishresult >= 90 and englishresult <=100 :
        e =(" A+")
        e1=4
    elif  englishresult >= 85 and englishresult <=89:
        e= ("A")
        e1=4
    elif englishresult >= 80 and englishresult <=84:
        e= ("A-")
        e1=3.75
    elif englishresult >=75 and englishresult <=80:
        e= ("B+")
        e1=3.5     
    elif englishresult >=70 and englishresult <=74:
        e= (" B") 
        e1=3    
    elif englishresult >=65 and englishresult <=69:
        e= ("B-") 
        e1=2.75
    elif englishresult >=60 and englishresult <=64:
        e= (" C+") 
        e1=2.5
    elif englishresult >=50 and englishresult <=69:
        e=(" C") 
        e1=2
    elif englishresult >45 and englishresult <=49:
        e= (" C-") 
        e1=1.75
    elif englishresult >=40 and englishresult <=45:
        e= (" D") 
        e1=1
    elif englishresult >=0 and englishresult <=39:
        e= ("F") 
        e1=0 
else :
    e="incorect tray agin" 
#grading system
if chemistryresult > 0 and chemistryresult <=100 :
    if chemistryresult >= 90 and chemistryresult <=100 :
        c =(" A+")
        c1=4
    elif  chemistryresult >= 85 and chemistryresult <=89:
        c= ("A")
        c1=4
    elif chemistryresult >= 80 and chemistryresult <=84:
        c= (" A-")
        c1=3.75
    elif chemistryresult >=75 and chemistryresult <=80:
        c= ("B+")
        c1=3.5     
    elif chemistryresult >=70 and chemistryresult <=74:
        c= (" B") 
        c1=3    
    elif chemistryresult >=65 and chemistryresult <=69:
        c= (" B-") 
        c1=2.75
    elif chemistryresult >=60 and chemistryresult <=64:
        c= (" C+") 
        c1=2.5
    elif chemistryresult >=50 and chemistryresult <=69:
        c=(" C") 
        c1=2
    elif chemistryresult >45 and chemistryresult <=49:
        c= ("C-") 
        c1=1.75
    elif chemistryresult >=40 and chemistryresult <=45:
        c= (" D") 
        c1=1
    elif chemistryresult >=0 and chemistryresult <=39:
        c= (" F") 
        c1=0 
else :
    c="incorect tray agin" 
#grading system
if  civicresult > 0 and civicresult <= 100:
    if civicresult >= 90 and civicresult <=100 :
        s =("A+")
        s1=4
    elif  civicresult >= 85 and civicresult <=89:
        s= ("A")
        s1=4
    elif civicresult >= 80 and civicresult <=84:
        s= ("A-")
        s1=3.75
    elif civicresult >=75 and civicresult <=80:
        s= (" B+")
        s1=3.5     
    elif civicresult >=70 and civicresult <=74:
        s= (" B") 
        s1=3    
    elif civicresult >=65 and civicresult <=69:
        s= (" B-") 
        s1=2.75
    elif civicresult >=60 and civicresult <=64:
        s= ("C+") 
        s1=2.5
    elif civicresult >=50 and civicresult <=69:
        s=("C") 
        s1=2
    elif civicresult >45  and civicresult <=49:
        s= ("C-") 
        s1=1.75
    elif civicresult >=40 and civicresult <=45:
        s= ("D") 
        s1=1
    elif civicresult >=0 and civicresult <=39:
        s= (" F") 
        s1=0 
else :
    s="incorect tray agin" 
#grading system
if    pythonresult > 0 and pythonresult  <= 100:
    if pythonresult >= 90 and pythonresult  <=100 :
        py=(" A+")
        py1=4
    elif  pythonresult >= 85 and pythonresult <=89:
        py= (" A")
        py1=4
    elif pythonresult >= 80 and pythonresult <=84:
        py= (" A-")
        py1=3.75
    elif pythonresult >=75 and pythonresult <=80:
        py= ("B+")
        py1=3.5     
    elif pythonresult >=70 and pythonresult <=74:
        py= (" B") 
        py1=3    
    elif pythonresult >=65 and pythonresult <=69:
        py= ("B-") 
        py1=2.75
    elif pythonresult >=60 and pythonresult <=64:
        py= (" C+") 
        py1=2.5
    elif civicresult >=50 and pythonresult <=69:
        py=(" C") 
        py1=2
    elif pythonresult >45  and pythonresult <=49:
        py= ("C-") 
        py1=1.75
    elif pythonresult >=40 and pythonresult <=45:
        py= ("D") 
        py1=1
    elif pythonresult >=0 and pythonresult <=39:
        py= (" F") 
        py1=0 
else :
    p="incorect tray agin" 
#creadut hour muliply by each gread    
mathr=m1*math
phyr=p1*phy
englishr=english*e1
chemistryr=chemistry*c1
civicr=civic*s1
pythonr=python*py1
#sum of cradit hour multiple by each gread
sumCG=  mathr+phyr+englishr+chemistryr+civicr+python    
#creadit hour summ1
creadit_hour_sum=phy+englishr+chemistry+civic+python 
#last gpa result 
gpa=sumCG/creadit_hour_sum
print ("\n\n\n\n")
print (f"you take total {sub}  subject \n")
print ("*subject_______________________result________________________grade_______________gpa")
print (f" applide math1 -----------------{mathresult}----------------{m}                 |")
print (f" Gneral physics-----------------{phyresult}-----------------{p}                 |")
print (f" English      ------------------{englishresult}-------------{e}                 |")           
print (f" civic        ------------------{civicresult}---------------{s}                 |")
print (f" Chemistry    ------------------{chemistryresult}-----------{c}                 |")
print (f" Python       ------------------{pythonresult}--------------{py}                |")
print (f"                                                              your Gpa is       ={gpa}")
