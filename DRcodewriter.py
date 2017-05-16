#The things in quotes are the names of your characters.
#They're what you're going to be typing over and over in Catalysis macros.
#Make them short, but recognizable.
FIRST = "jc" #justin chevalier by Aeliren
SECOND = "ak" #alicia knightly by FenrirDarkWolf
THIRD = "kb" #kreat baff by Dypo
FOURTH = "sb" #shaun baldwin by Lind
FIFTH = "at" #adam turner by DragonTrainer
SIXTH = "vi" #viktor brunovich ivanov by Greeny
SEVENTH = "ft" #fane tuffs by LunchPolice
EIGHTH = "kk" #ken knott by gotMLK7
NINTH = "zt" #zachary tei by Lind
TENTH = "hb" #hugo beardsley by Lind
ELEVENTH = "dk" #drake kones by FenrirDarkWolf
TWELFTH = "gm" #garret manson by Godot Mango
THIRTEENTH = "p" #porho by Dataman
FOURTEENTH = "ed" #elliot darbin by Eldariub
FIFTEENTH = "ts" #ta'mha shii by Lind
SIXTEENTH = "dd" #desron delite by DragonTrainer

#See the following links? Don't change them unless they stop working.
#They are generic enough to work for any user.
#Plus, they take up less than 1KB on my GitHub.
wide3 = "http://SemperSolus.github.io/3wide.png"
wide6 = "http://SemperSolus.github.io/6wide.png"
wide7 = "http://SemperSolus.github.io/7wide.png"
wide9 = "http://SemperSolus.github.io/9wide.png"
wide11 = "http://SemperSolus.github.io/11wide.png"
wide15 = "http://SemperSolus.github.io/15wide.png"
places = ["3wide","6wide","7wide","9wide","11wide","15wide"]
#The key to this dict is the NAME of the background object.
#The value to this dict is the URL of the background object.
#You will need some sort of backdrop (bg), but other than that, it's up to you.
#if you want different backgrounds you can make a BG1, BG2, etc..
bgs = {"bg":"https://i.imgur.com/5V78Cyc.png",
       "pillar":"https://i.imgur.com/1UoUcxh.png",
       "throne":"https://i.imgur.com/rtsXEWU.png"}
#If you want to change the number of students, don't forget to change
#this list.
students = [FIRST,SECOND,THIRD,FOURTH,FIFTH,
            SIXTH,SEVENTH,EIGHTH,NINTH,TENTH,
            ELEVENTH,TWELFTH,THIRTEENTH,FOURTEENTH,
            FIFTEENTH,SIXTEENTH]
#Put the emotional suffixes of each character here.
#The ones here are just examples.
#Don't forget to put in the external image URLs.
#To be clear, the URLs you're putting in are for the sprites that
        # DON'T TALK.
#This code absolutely does not work with the pre-installed AAO sprites.
#(I'm not saying it's impossible; I'm just saying it's a lot of work.)
emo = {FIRST:{"n":"http://i.imgur.com/bkNBdue.gif",
              "thinking":"http://i.imgur.com/aBJR10Q.gif"},
              SECOND:{"n":"http://i.imgur.com/We5xp4g.gif",
                      "m":"http://i.imgur.com/wdQfjDl.gif",
                      "h":"http://i.imgur.com/KP6MAm5.png"},
              THIRD:{"n":"http://i.imgur.com/SatVpMV.gif"},
              FOURTH:{"n":"http://i.imgur.com/WQDSksR.gif",
                      "w":"http://i.imgur.com/kYFPuGe.gif",
                      "thinking":"http://i.imgur.com/2UW4ECb.gif"},
              FIFTH:{"n":"http://i.imgur.com/wnQF8Ct.gif",
                     "deadpan":"http://i.imgur.com/wHJ689Y.gif",
                     "m":"http://i.imgur.com/NMn1eZY.gif"},
              SIXTH:{"n":"http://i.imgur.com/LBzWDp4.gif",
                     "tray":"http://i.imgur.com/0l86qzb.gif"},
              SEVENTH:{"n":"http://i.imgur.com/SghP8he.png"},
              EIGHTH:{"n":"http://i.imgur.com/w0KSf2D.gif",
                      "pleading":"http://i.imgur.com/ze297tq.gif",
                      "h":"http://i.imgur.com/k94vUhn.gif",
                      "crying":"http://i.imgur.com/j093gjm.gif"},
              NINTH:{"n":"http://i.imgur.com/rtf1Iso.gif",
                     "m":"http://i.imgur.com/XzJWHs8.gif",
                     "thinking":"http://i.imgur.com/PtZ7TOr.png"},
              TENTH:{"n":"http://i.imgur.com/n9zAmzW.gif",
                     "h":"http://i.imgur.com/YhLfPbC.gif",
                     "m":"http://i.imgur.com/9Xp5tVB.gif",
                     "proud":"http://i.imgur.com/fMCt7sG.gif"},
              ELEVENTH:{"n":"http://i.imgur.com/avsQIWT.gif",
                        "point":"http://i.imgur.com/qfBI1MH.gif",
                        "w":"http://i.imgur.com/pMcA34G.gif",
                        "thinking":"http://i.imgur.com/Vr7L2bf.gif"},
              TWELFTH:{"n":"http://i.imgur.com/s8ve83a.png",
                       "m":"http://i.imgur.com/jnBnKkp.png"},
              THIRTEENTH:{"n":"http://i.imgur.com/qQLrBqX.gif",
                          "money":"http://i.imgur.com/v8fGpi4.gif"},
              FOURTEENTH:{"n":"http://i.imgur.com/9ccpBtG.gif",                          
                          "w":"http://i.imgur.com/XRhzULq.gif"},
              FIFTEENTH:{"n":"http://i.imgur.com/RKUEMmy.gif",
                         "beads":"http://i.imgur.com/e6IsJJ7.gif",
                         "meditate":"http://i.imgur.com/oSaX1mt.gif",
                         "pray":"http://i.imgur.com/rEqTs5j.gif"},
              SIXTEENTH:{"n":"http://i.imgur.com/FQELMXj.gif",
                         "m":"http://i.imgur.com/88cMSRr.gif",
                         "h":"http://i.imgur.com/m82Ioxi.gif"}}
#These are the background objects that go behind each character.
loc = {FIRST:["bg"],
              SECOND:["bg"],
              THIRD:["bg","pillar"],
              FOURTH:["bg"],
              FIFTH:["bg"],
              SIXTH:["bg"],
              SEVENTH:["bg","pillar"],
              EIGHTH:["bg"],
              NINTH:["bg","throne"],
              TENTH:["bg"],
              ELEVENTH:["bg","pillar"],
              TWELFTH:["bg"],
              THIRTEENTH:["bg"],
              FOURTEENTH:["bg"],
              FIFTEENTH:["bg","pillar"],
              SIXTEENTH:["bg"]}

#This dictionary is pretty much just because Python doesn't support
#switch statements.
placedict = {1:"3wide",2:"3wide",3:"7wide",4:"9wide",5:"6wide",6:"7wide",
             7:"15wide",8:"9wide",14:"15wide"}
transdict = {1:"center",2:"side",3:"center",4:"center",5:"side",6:"side",
             7:"center",8:"side",14:"side"}

setofobjs = {}


def main():
    '''
    makeplace("3wide",wide3)
    makeplace("6wide",wide6)
    makeplace("7wide",wide7)
    makeplace("9wide",wide9)
    makeplace("15wide",wide15)
    addEmoBgs()
    addCourtBgs()
    setemo()
    '''
    hideall()

def makeplace(strname,string):
    print("Place "+strname+" {")
    print("path: "+string)
    print("}\n")

def addEmoBgs():
#Here we go. Forbidden Nested Loop #2.
#The first loop iterates through the list of places.
    for place in places:
#The next layer iterates through the list of students.
        for student in students:
#Each student corresponds to a dictionary whose keys are emotions and values
       #are external image URLs.
            emolist = emo[student]
#The next layer iterates through the dictionary of that student's emotions.
            for emotion in emolist.keys():
#This layer runs once for each time the place is wider than the screen.
               for x in range(int(place.replace("wide",''))):
                       if (student != "first"):
                           break
                       print(place + " background {")
                       print("path: " + emolist[emotion])
                       print("x: " + str(x*256))
                       print("y: 0")
                       print("name:: " + student + "_" +emotion+"_"+ str(x))
                       print("hidden: true")
                       print()
               

def addCourtBgs():
#Hoo, boy. This is the Nested Loop every Python developer tells you not to do.
#The first loop iterates through the list of places.
    for place in places:
#The next layer iterates through the list of students.
        for student in students:
#The next layer iterates through the dictionary of images behind each student.
            for bg in loc[student]:
#This layer iterates through the list of images.
    
#This layer runs once for each time the place is wider than the screen.

                for x in range(int(place.replace("wide",''))):
                    if (student != "first"):
                        break
                    print(place + " background {")
                    print("path: " + str(bgs.get(bg)))
                    print("x: " + str(x*256))
                    print("y: 0")
                    print("name:: " + bg +"_"+ str(x))
                    print("hidden: true")
                    print()
               

def transition():
    for s1 in students:
        for s2 in students:
            if (s1 == s2):
                continue
            dif = (students.index(s2) - students.index(s1))
            startPos = "right" if dif <0 else "left"
            endPos = "left" if startPos == "right" else "right"
            endPos = "center" if 
            dif%=len(students)
            #student1_to_student2 {
            print(s1 + "_to_"+s2+ " {")
            print("hideall")
            #place, $place$, right/left
            print("place, "+placedict.get(dif)+", "+startPos)
            #set_sprite, student1, n
            print("set_sprite, "+ s1 + ", "+ emo.get(s1).get("n","n"))
            print("CPos, "+startPos)
            #set_sprite, student2, n
            print("set_sprite, "+ s2 + ", "+ emo.get(s2).get("n","n"))
            print("CPos, "+endPos)
            #this loop goes through each "slot" in Place from right to left.
            for y in range(0,int(placedict.get(dif).replace("wide","")),-1):
                newstudent = students[(students.index(s1) -
                    (int(placedict.get(dif).replace("wide",""))-y))%len(students)]
                print
            else:
                print("place, "+placedict.get(dif)+", left")
            print("scroll, bezier")
            print("erase")
            print
            
def setemo():
    for student in students:
        for emotion in emo.get(student,"ERROR").keys():
            print(student+"_"+emotion+" {")
            print("varDef")
            print(student+"_emo\n" + emotion + "\n}")
            print()

            
#the place called is determined by dif.
#you are aligned on the left or the right depending on whether goleft is
            #false or true, respectively.
#REMINDER: make a macro called hideall, that sets the "hidden" attribute
            #of all the objects I've created to "true". LOT of nested loops!

def hideall():
    print("hideall {")
    for place in places:
        for student in students:
            emolist = emo[student]
            for emotion in emolist.keys():
                for x in range(int(place.replace("wide",""))):                
                    candidate = place+"_"+student + "_" +emotion+"_"+ str(x)                    
                    if(candidate in setofobjs):
                        print("hideObj")
                        print(place)
                        print(student + "_" +emotion+"_"+ str(x)+"\n")
            for bg in loc[student]:
                #TODO: Fix this part so it isn't so repetitive.
                for x in range(int(place.replace("wide",""))):                
                    print("hideObj")
                    print(place)
                    print(bg+"_"+ str(x))
    print("\n}")
