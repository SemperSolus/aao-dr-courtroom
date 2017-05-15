#The things in quotes are the names of your characters.
#They're what you're going to be typing over and over in Catalysis macros.
#Make them short, but recognizable.
FIRST = "first"
SECOND = "second"
THIRD = "third"
FOURTH = "fourth"
FIFTH = "fifth"
SIXTH = "sixth"
SEVENTH = "seventh"
EIGHTH = "eighth"
NINTH = "ninth"
TENTH = "tenth"
ELEVENTH = "eleventh"
TWELFTH = "twelfth"
THIRTEENTH = "thirteenth"
FOURTEENTH = "fourteenth"
FIFTEENTH = "fifteenth"
SIXTEENTH = "sixteenth"

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
bgs = {"bg":"background_url_goes_here",
       "pillar":"pillar_url_goes_here",
       "throne":"throne_url_goes_here"}
#If you want to change the number of students, don't forget to change
#this list.
students = [FIRST,SECOND,THIRD,FOURTH,FIFTH,
            SIXTH,SEVENTH,EIGHTH,NINTH,TENTH,
            ELEVENTH,TWELFTH,THIRTEENTH,FOURTEENTH,
            FIFTEENTH,SIXTEENTH]
#Put the emotional suffixes of each character here.
#The ones here are just examples.
#Don't forget to put in the external image URLs.
#This code absolutely does not work with the pre-installed AAO sprites.
#(I'm not saying it's impossible; I'm just saying it's a lot of work.)
emo = {FIRST:{"normal":"URL","mad":"URL","damage":"URL",
              "worried":"URL","thinking":"URL"},
              SECOND:{"normal":"URL","mad":"URL","damage":"URL",
                      "worried":"URL","thinking":"URL"},
              THIRD:{"normal":"URL","mad":"URL","damage":"URL",
                     "worried":"URL","thinking":"URL"},
              FOURTH:{"normal":"URL","mad":"URL","damage":"URL",
                      "worried":"URL","thinking":"URL"},
              FIFTH:{"normal":"URL","mad":"URL","damage":"URL",
                     "worried":"URL","thinking":"URL"},
              SIXTH:{"normal":"URL","mad":"URL","damage":"URL",
                     "worried":"URL","thinking":"URL"},
              SEVENTH:{"normal":"URL","mad":"URL","damage":"URL",
                       "worried":"URL","thinking":"URL"},
              EIGHTH:{"normal":"URL","mad":"URL","damage":"URL",
                      "worried":"URL","thinking":"URL"},
              NINTH:{"normal":"URL","mad":"URL","damage":"URL",
                     "worried":"URL","thinking":"URL"},
              TENTH:{"normal":"URL","mad":"URL","damage":"URL",
                     "worried":"URL","thinking":"URL"},
              ELEVENTH:{"normal":"URL","mad":"URL","damage":"URL",
                        "worried":"URL","thinking":"URL"},
              TWELFTH:{"normal":"URL","mad":"URL","damage":"URL",
                       "worried":"URL","thinking":"URL"},
              THIRTEENTH:{"normal":"URL","mad":"URL","damage":"URL",
                          "worried":"URL","thinking":"URL"},
              FOURTEENTH:{"normal":"URL","mad":"URL","damage":"URL",
                          "worried":"URL","thinking":"URL"},
              FIFTEENTH:{"normal":"URL","mad":"URL","damage":"URL",
                         "worried":"URL","thinking":"URL"},
              SIXTEENTH:{"normal":"URL","mad":"URL","damage":"URL",
                         "worried":"URL","thinking":"URL"}}
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
            if (dif <0):
                goleft = True
            dif%=len(students)
            print(s1 + "_to_"+s2+ " {")
            print("hideall")
            if (goleft):
                print("place, "+placedict.get(dif)+", right")
                #this loop goes through each "slot" in Place from right to left.
                for y in range(0,int(placedict.get(dif).replace("wide","")),-1):
                    newstudent = students[(students.index(s1) - (int(placedict.get(dif).replace("wide",""))-y))%len(students)]
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
    print("hideObj")
    for place in places:
        for student in students:
            emolist = emo[student]
            for emotion in emolist.keys():
                for x in range(int(place.replace("wide",""))):                
                    print(place+" -> "+student + "_" +emotion+"_"+ str(x))
            for bg in loc[student]:
                for x in range(int(place.replace("wide",""))):                
                    print(place+" -> "+bg+"_"+ str(x))
    print(":\n}")
