'''
Hi, all. Semper Solus here.
If you're reading this, it's because either you accidentally found my GitHub,
or you clicked on the link from Ace Attorney Online, and are curious about
putting a DanganRonpa-style courtroom in your trials. I'll assume the latter.

Now, Ace Attorney Online is a case maker that prides itself on being browser-
based and requiring little to no programming knowledge. Don't get me wrong;
that's pretty great, but since the process for making a DanganRonpa courtroom
does require manipulating and executing a program, I've decided to make my
documentation a little... TOO thorough.

<<<<<<< HEAD
See, I play way more cases than I've made. I figure, if I make this, I might as
=======
I play way more cases than I've made. I figure, if I make this, I might as
>>>>>>> origin/master
well let other people use this so I can play their stuff.
Of course, that means making this as accessible, generic, and customizable
as possible.

That's why this file has more comments than code.

In conclusion, to everyone with actual programming prowess (which excludes me),
please bear with me.
'''

#On to the code...

<<<<<<< HEAD
'''
The PREFIXES of your characters go here.

The characters that are already here are just for debugging purposes.
They're from AAO's Random Characters thread.
=======



'''
The things in quotes are the Catalysis prefixes of your characters.
The ones that are currently here are ones I put in for testing purposes.
>>>>>>> origin/master
'''
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

'''
See the following links? Don't change them unless they stop working.
They are generic enough to work for any user who wants a DanganRonpa-esque
trial with 16 or fewer students.
Plus, they take up less than 1KB on my GitHub.

It's not like they're anything special, anyway. Take the standard black 129x256-
pixel background, and multiply the width by the number after "wide". If you save
it as a png and don't include an alpha channel it takes up almost no space.

Computer graphics fun fact! The reason this png takes up such little space is
because pngs are saved in the format of "a pixel's color, how many pixels are
that color until the next one, and so on." Since all pixels are the same color,
You save space big-time.
'''
wide3 = "http://SemperSolus.github.io/3wide.png"
wide6 = "http://SemperSolus.github.io/6wide.png"
wide7 = "http://SemperSolus.github.io/7wide.png"
wide9 = "http://SemperSolus.github.io/9wide.png"
wide11 = "http://SemperSolus.github.io/11wide.png"
wide15 = "http://SemperSolus.github.io/15wide.png"
<<<<<<< HEAD
places = ["3wide","6wide","7wide","9wide","15wide"]
=======


places = {"3wide":"http://SemperSolus.github.io/3wide.png",
          "6wide":"http://SemperSolus.github.io/6wide.png",
          "7wide":"http://SemperSolus.github.io/7wide.png",
          "9wide":"http://SemperSolus.github.io/9wide.png",
          "15wide":"http://SemperSolus.github.io/15wide.png"}
>>>>>>> origin/master

'''
The key to this dict is the NAME of the background object.
The value to this dict is the URL of the background object.
You will need some sort of backdrop (bg), but other than that, it's up to you.
if you want different backgrounds you can make a BG1, BG2, etc..
'''

bgs = {"bg":"https://i.imgur.com/4IXP175.png",
       "pillar":"https://i.imgur.com/1UoUcxh.png",
       "throne":"https://i.imgur.com/rtsXEWU.png"}

<<<<<<< HEAD
# Similarly, foreground objects go here.
=======
# Similarly, foreground objects go here. You can have more than one.
>>>>>>> origin/master

fgs = {"podium":"https://i.imgur.com/tvPMuyc.png"}

'''
If you want to change the number of students, don't forget to change
this list.
For whatever reason (so many people could use it, I guess), I tried to make
the code incredibly dynamic. Instead of referring to a static number of
<<<<<<< HEAD
students, like 16, I referred to the length of this list.
Also, this list is handy for changing who is next to whom. Just move 'em around.

Ooh! Right. If you want to leave a seat empty, like the first DR game, that's
not done here. That's done over in emo{}. Make a blank 192x256 rectangle or
something.
=======
students, like 16, I always refer to the length of this list.
Also, this list is handy for changing who is next to whom. Just move 'em around.

Ooh! Right. If you want to leave a seat empty, like the first DR game, that's
not done here. That's done over in emo{}. Make a transparent 192x256 rectangle
or something. Or leave the dict empty? Does that work?
>>>>>>> origin/master
'''
students = [FIRST,SECOND,THIRD,FOURTH,FIFTH,
            SIXTH,SEVENTH,EIGHTH,NINTH,TENTH,
            ELEVENTH,TWELFTH,THIRTEENTH,FOURTEENTH,
            FIFTEENTH,SIXTEENTH]

'''
Put the emotional suffixes of each character here.
The ones here are just examples.
Don't forget to put in the external image URLs.
To be clear, the URLs you're putting in are for the sprites that DON'T TALK.
This code absolutely does not work with the pre-installed AAO sprites.
(I'm not saying it's impossible; I'm just saying it's a lot of work for me.)

Also note that a sprite's "default" expression should be first in the
<<<<<<< HEAD
dictionary.
=======
dictionary, and it HAS to be called 'n'.

>>>>>>> origin/master
... And just in case you don't know, a "dictionary" (called in other languages
a "map") is simply a collection of key-value pairs.
The idea is that each key "maps" to a value. A dictionary can have only 1
of each key, but more than one value if you want.
In the case below, the keys are the emotion suffixes, and the values are
the URLs. Isn't this an educational hobby?
Like, I'm not joking. I did not know Python when I started. It probably shows.
'''

emo = {FIRST:{"n":"http://i.imgur.com/bkNBdue.gif",
<<<<<<< HEAD
              "thinking":"http://i.imgur.com/aBJR10Q.gif"},
=======
              "th":"http://i.imgur.com/aBJR10Q.gif"},
>>>>>>> origin/master
              SECOND:{"n":"http://i.imgur.com/We5xp4g.gif",
                      "m":"http://i.imgur.com/wdQfjDl.gif",
                      "h":"http://i.imgur.com/KP6MAm5.png"},
              THIRD:{"n":"http://i.imgur.com/SatVpMV.gif"},
              FOURTH:{"n":"http://i.imgur.com/WQDSksR.gif",
                      "w":"http://i.imgur.com/kYFPuGe.gif",
<<<<<<< HEAD
                      "thinking":"http://i.imgur.com/2UW4ECb.gif"},
=======
                      "th":"http://i.imgur.com/2UW4ECb.gif"},
>>>>>>> origin/master
              FIFTH:{"n":"http://i.imgur.com/wnQF8Ct.gif",
                     "deadpan":"http://i.imgur.com/wHJ689Y.gif",
                     "m":"http://i.imgur.com/NMn1eZY.gif"},
              SIXTH:{"n":"http://i.imgur.com/LBzWDp4.gif",
                     "tray":"http://i.imgur.com/0l86qzb.gif"},
              SEVENTH:{"n":"http://i.imgur.com/SghP8he.png"},
              EIGHTH:{"n":"http://i.imgur.com/w0KSf2D.gif",
<<<<<<< HEAD
                      "pleading":"http://i.imgur.com/ze297tq.gif",
                      "h":"http://i.imgur.com/k94vUhn.gif",
                      "crying":"http://i.imgur.com/j093gjm.gif"},
              NINTH:{"n":"http://i.imgur.com/rtf1Iso.gif",
                     "m":"http://i.imgur.com/XzJWHs8.gif",
                     "thinking":"http://i.imgur.com/PtZ7TOr.png"},
=======
                      "plead":"http://i.imgur.com/ze297tq.gif",
                      "h":"http://i.imgur.com/k94vUhn.gif",
                      "cry":"http://i.imgur.com/j093gjm.gif"},
              NINTH:{"n":"http://i.imgur.com/rtf1Iso.gif",
                     "m":"http://i.imgur.com/XzJWHs8.gif",
                     "th":"http://i.imgur.com/PtZ7TOr.png"},
>>>>>>> origin/master
              TENTH:{"n":"http://i.imgur.com/n9zAmzW.gif",
                     "h":"http://i.imgur.com/YhLfPbC.gif",
                     "m":"http://i.imgur.com/9Xp5tVB.gif",
                     "proud":"http://i.imgur.com/fMCt7sG.gif"},
              ELEVENTH:{"n":"http://i.imgur.com/avsQIWT.gif",
                        "point":"http://i.imgur.com/qfBI1MH.gif",
                        "w":"http://i.imgur.com/pMcA34G.gif",
<<<<<<< HEAD
                        "thinking":"http://i.imgur.com/Vr7L2bf.gif"},
=======
                        "th":"http://i.imgur.com/Vr7L2bf.gif"},
>>>>>>> origin/master
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

'''
These are the background objects that go behind each character.
The idea is that you can change the backgrounds to simulate a real room.
'''
locbg = {FIRST:["bg"],
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

'''
And these are the FOREground objects that go in FRONT of each character.
Surprise!
But you know those portrait-signs that show up in the games to replace dead
people? You know what I'm talking about? They have faces with X's over them.
Anyway, you want those to be sprites. Not foreground objects. You can do it
either way. I'm just saying it makes more sense.
Anyway, there's support for each character to have his custom podium. IDKY.
'''
locfg = {FIRST:["podium"],
              SECOND:["podium"],
              THIRD:["podium"],
              FOURTH:["podium"],
              FIFTH:["podium"],
              SIXTH:["podium"],
              SEVENTH:["podium"],
              EIGHTH:["podium"],
              NINTH:["podium"],
              TENTH:["podium"],
              ELEVENTH:["podium"],
              TWELFTH:["podium"],
              THIRTEENTH:["podium"],
              FOURTEENTH:["podium"],
              FIFTEENTH:["podium"],
              SIXTEENTH:["podium"],}

'''
This dictionary is pretty much just because Python doesn't support
switch statements.
IMPORTANT: Making a case with FEWER than 16 students is easy. You just edit
the students list and all the relevant data structures. Making a case with
MORE than 16? Gonna take a bit more work. Doable work, though.
Basically, you make some more PNG files like wide3 and wide5, so that it can
handle transitions between the extra students. Then you edit every data
structure with the word "place" in it.
For example, if you want 19 students, you're going to have to handle transitions
between 9 and 10 students now, so you'll need blank PNGs that are 2560 and 2816
pixels wide respectively (10wide and 11wide).
'''
placedict = {1:"3wide",2:"3wide",3:"7wide",4:"9wide",5:"6wide",6:"7wide",
             7:"15wide",8:"9wide",14:"15wide"}

'''
What is this? This is a data structure called a set. 'bob' is in here so Python
doesn't think it's a dictionary. They both look the same when they're empty.
The two things you have to remember about sets are that their elements aren't
in any order and they can't contain duplicates.
If you try to give them a duplicate element, they'll delete it.
Sets are important in programming and math. Just thought I'd share that.
'''
setofobjs = {'bob'}

<<<<<<< HEAD
'''
Don't call main. Main prints the results of all the functions. That's not as
useful.
Call objects to call just the functions that print objects,
And call macros to call the functions that print macros.
Then paste the results into the appropriate text folder.
'''
def main():
=======

# These are used in the deletechars function later in this file.
# Since all the places are written as [characterprefix]+[number],
# You can isolate one of the two using deletechars.
alphabetplus = "abcdefghijklmnopqrstuvwxyz+"
numberplus = "1234567890+"


'''
The idea of this list is to hold all the places that were created so they can
be used by other functions.
'''

createdPlaces = []



'''
Call objects to call just the functions that print objects,
Call frames to call only the functions that print frames,
And call macros to call the functions that print macros.
Then paste the results into the appropriate text folder.
'''
def objects():
    makePlace()
    initCourtObjs()
    
def macros():
>>>>>>> origin/master
    '''
In my attempt to make this code as customizeable as possible, you can change
the way the courtroom scrolls here.
If you don't type "none", "linear", "bezier", "ease_in", or "ease_out",
It won't type a scroll at all, and you'll have to put in a scroll type each
time, if that's your thing.
'''
    transition('ease_out')
    setemo('ease_out')
#If you think "_from_left" is too much to write, just change what's written
#here to "l", "r", and "c". Nothing else works, tho. 
    notTransition("left")
    notTransition("right")
    notTransition("center")

def frames():
    '''
<<<<<<< HEAD
    hideall()

def objects():
    makeplace("3wide",wide3)
    makeplace("6wide",wide6)
    makeplace("7wide",wide7)
    makeplace("9wide",wide9)
    makeplace("15wide",wide15)
    addEmoBgs()
    addCourtBgs()
    
def macros():
    transition()
    hideall()
    setemo()
#If you think "_from_left" is too much to write, just change what's written
#here to "l", "r", and "". Don't forget to change the bottom to match!
    not_transition("left")
    not_transition("right")
    not_transition("center")

def makeplace(strname,string):
    print("Place "+strname+" {")
    print("path: "+string)
    print("}\n")


def addCourtBgs():
#Hoo, boy. This is the Nested Loop every Python developer tells you not to do.
#The first loop iterates through the list of places.
    for place in places:
#The next layer iterates through the list of students.
        for student in students:
#The next layer iterates through the dictionary of images behind each student.
            for bg in locbg[student]:
#This layer iterates through the list of images.
    
#This layer runs once for each time the place is wider than the screen.

                for x in range(int(place.replace("wide",''))):
                    if (student != FIRST): #DEBUG
                        break #DEBUG
                    print(place + " background {")
                    print("path: " + str(bgs.get(bg)))
                    print("x: " + str(x*256))
                    print("y: 0")
                    print("name: " + bg +"_"+ str(x))
                    print("hidden: true")
                    print("}\n")
            for fg in locfg[student]:
#Okay, same deal, but for foregrounds.
                for x in range(int(place.replace("wide",''))):
                    if (student != "first"): #DEBUG
                        break #DEBUG
                    print(place + " background {")
                    print("path: " + str(fgs.get(fg)))
                    print("x: " + str(x*256))
                    print("y: 0")
                    print("name: " + fg +"_"+ str(x))
                    print("hidden: true")
                    print("}\n")
#I know this function is called "addCourtBgs". It also does fgs.
#I forgot about them until later.


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
                      # if (student != FIRST):
                       #    break
                       print(place + " background {")
                       print("path: " + emolist[emotion])
                       print("x: " + str(x*256))
                       print("y: 0")
                       print("name: " + student + "_" +emotion+"_"+ str(x))
                       print("hidden: true")
                       print("}\n")
               
=======
The first argument here is the frame anchor you use to start the routine that
changes the emotions of all the still sprite background objects, and the
second argument is the variable you will have to type repeatedly as you assign
frame anchors to it in order to get back.

If you do not understand what I just said, please read the Catalysis user guide
and a tutorial on variables in AAO. It's kind of beyond the scope of comments
in a python file.
'''
    checkall("checkAll","backFromCheckAll")


'''
There are a lot of places. How many places?
Take the number of trial participants, and divide it by 2.
Take away all the odd powers of 2 from 1 until that number, inclusive.
Take away the even numbers that aren't even powers of 2 from 1 until that
number, inclusive.
Take the number you have now, and multiply it by the number of participants.
In the program's default settings, this number is 80.
If you add to 
'''
def makePlace():
    global createdPlaces
    for place in places.keys():
        #if (place != '6wide'): #DEBUG
         #   continue #DEBUG
        for student in students:
          #  if (student != FIRST): #DEBUG
           #     continue #DEBUG
            print("Place "+student+"+"+(str(int(place.replace("wide",''))-1))+" {")
            print("path: "+places.get(place))
            print("}\n")
            createdPlaces.append(student+"+"+(str(int(place.replace("wide",''))-1)))
    createdPlaces = list(set(createdPlaces))


#This function is mostly for debugging purposes, so the other functions can
#run without running makePlace().
def harmlessMakePlace():
    global createdPlaces
    for place in places.keys():
        #if (place != '6wide'): #DEBUG
        #    continue #DEBUG
        for student in students:
         #   if (student != FIRST): #DEBUG
          #      continue #DEBUG
            #print("Place "+student+"+"+(str(int(place.replace("wide",''))-1))+" {")
            #print("path: "+places.get(place))
            #print("}\n")
            createdPlaces.append(student+"+"+(str(int(place.replace("wide",''))-1)))
            #print(student+"+"+(str(int(place.replace("wide",''))-1))) #DEBUG
    createdPlaces = list(set(createdPlaces))


'''
This function makes all the courtroom foreground and background objects, as
well as the still sprites of each character that can't be placed in a place.
Those are placed as background objects.
That's how you get 9 people in one scene!
'''
def initCourtObjs():
    if not createdPlaces:
        harmlessMakePlace()
    for place in createdPlaces:
        #if (place[2:4] == "+5"): #DEBUG
         #   break #DEBUG
        s1 = deletechars(place,numberplus)        
#If I got this right, that code is supposed to take the place name, get rid of
#the student name, and then start with the second character to get rid of the
#plus sign.
#I wrote it before I made the deletechars() function.
        for x in range(int(place.replace(s1,'')[1:])+1):
            emolist = emo[students[(students.index(s1)+x)%len(students)]]
            for bg in locbg.get(students[(students.index(s1)+x)%len(students)]):
                print(place+" background {")
                print("name: "+bg+"_"+str(x))
                print("y: 0")
                print("x: "+str(x*256))
                print("path: "+bgs.get(bg))
#all background items are always visible. If you want to change this yourself,
#nobody's stopping you.
#                print("hidden: false")
                print("}\n")
            for fg in locfg.get(students[(students.index(s1)+x)%len(students)]):
                print(place+" foreground {")
                print("name: "+fg+"_"+str(x))
                print("y: 0")
                print("x: "+str(x*256))
                print("path: "+fgs.get(fg))
#When would you hide a foreground object, though? Vanishing podiums?
 #               print("hidden: false")
                print("}\n")            
            for emotion in emolist.keys():
                if(x ==0):
                    continue
                if (students[(students.index(s1)+x)%len(students)]==
                    students[(students.index(s1)+(int(place.replace(s1,'')[1:])))%len(students)]):
                    continue
                if (int(place.replace(s1,'')[1:])/x==2):
                    continue
                print(place+" background {")
                print("name: "+students[(students.index(s1)+x)%len(students)]
                      +"_"+emotion)
                print("path: "+emolist[emotion])
                print("x: "+str(x*256))
                print("y: 0")
                print("hidden: true\n}\n")

'''
This is a companion function to the above function.
As long as the third argument is an empty string, it takes every character
in the second argument, and removes every instance of it from the first
argument.
It also can be used for other stuff. Want to change every instance of the letter
"a" in The Cat in the Hat to a "oo".
'''
def deletechars(place,string1,empty=''):
    place = place.replace(string1[0],empty)
    if (len(string1)==1):
        return place.replace(string1[0],empty)
    else:
        return deletechars(place,string1[1:],empty)

>>>>>>> origin/master

'''
This function prints macros that cause the screen to seamlessly slide from
any student to any other. It's the whole reason I did this.

<<<<<<< HEAD
... Or, at least, it's supposed to. It's not really working, and it eats a
lot of frames. If anyone, after looking at this code and at the Catalysis
guide, figures out what's wrong with it, please shoot me a message on Github
asking to collaborate.

If you can't, and you want to use a DanganRonpa courtroom in the meantime, I
recommend using the not_transition methods in the meantime. That's the poor
man's solution.
'''
def transition():
=======
For example, to scroll from a character with prefix zz to prefix xx, you'd type

zz_to_xx

zz.y
zz_y

As you can see, the transition macro needs to be a separate frame.

'''
def transition(scrollType):
>>>>>>> origin/master
    for s1 in students:
        for s2 in students:
            if (s1 == s2):
                continue
#dif is the difference in position between the two students.
            dif = (students.index(s2) - students.index(s1))
#dif must always be a positive number. There's probably a more efficient way
#to do this, but what do I care? You're only running this once.
            dif = len(students)+dif if dif < 0 else dif
#Depending on dif's size, you start on one side and scroll to the other.
            startPos = "right" if dif > len(students)/2 else "left"
#Having served its purpose, dif is now heavily operated on, becoming a new
#variable. Basically, it remains exactly the same unless dif is greater than
#half the the total number of students. Then dif becomes...
#Well, the equation is right there.
#For people who are afraid of code:
#    That percent sign means "modulus division", which is a fancy way of saying,
#    "get the remainder after you divide". len() is just a function that gets
#    you the length.
<<<<<<< HEAD
            dif = (len(students)/2)-dif%((len(students)/2)) if dif > len(students)/2 else dif
=======
            dif = int((len(students)/2))-dif%int((len(students)/2)) if dif > int(len(students)/2) else dif
>>>>>>> origin/master
            endPos = "left" if startPos == "right" else "right"
            #print("dif = "+str(dif)) #(for debugging)
            endPos = "center" if float(placedict.get(dif).replace("wide",""))/2 > dif else endPos            
            #student1_to_student2 {
            print(s1 + "_to_"+s2+ " {")
<<<<<<< HEAD
            print("hideall")
            print("erase")
            #place, $place$, right/left
            print("place, "+placedict.get(dif)+", "+startPos)
            #set_sprite, student1, n
            print("set_sprite, "+ s1 + ", "+ list(emo.get(s1).keys())[len(list(emo.get(s1).keys()))-1])
            #Okay, see what I did in the previous line? More than 80 characters?
            #Yeah, that's apparently bad ettiquette.
            #At least, according to the app I learned Python from.
            #But I don't know how to print without a line break at the end in
            #Python 3, so Long Line stays.
            print("CPos, "+startPos)
            #set_sprite, student2, n
            print("set_sprite, "+ s2 + ", "+ list(emo.get(s2).keys())[len(list(emo.get(s2).keys()))-1])
            print("CPos, "+endPos)
            #this loop goes through each "slot" in Place from right to left.
            for y in range(int(placedict.get(dif).replace("wide","")),0,-1):
                #newstudent is just the prefix for a student.
                newstudent = students[(students.index(s1) -
                    (int(placedict.get(dif).replace("wide",""))-y))%len(students)]
                if(y!=0 and y!=int(placedict.get(dif).replace("wide",""))):
                    checkemo(newstudent, dif,y)
                    print("merge")
                    print("anc $after"+newstudent+placedict.get(dif)+str(y)+":")
                for bg in locbg.get(newstudent):
                    print("RevObj")
                    print(placedict.get(dif))
                    print(bg+"_"+str(y))
                '''
You know, all this redundancy could be avoided with another dictionary.
Maybe put the name of the object as the key and "foreground"/"background" as the
value.
That would save a lot of run time because you wouldn't be iterating through the
same list as many times.
... Anyone want to do this? Because I'll just be happy if it works.
'''
                for fg in locfg.get(newstudent):
                    print("RevObj")
                    print(placedict.get(dif))
                    print(fg+"_"+str(y))
            print("scroll, linear")            
            print("}\n")


'''
this is not a function you should run by itself. It's part of transition().
I don't even think you CAN call it by itself, since it requires a string
and two ints as arguments, and where do you get those?
'''
def checkemo(student, dif,x):
    print("condit, $after" + student+placedict.get(dif)+str(x))
    for emotion in emo[student].keys():        
        print(student+"_emo = "+emotion)
        print("$"+student+emotion+str(x))
    for emotion in emo[student].keys():
        print("anc $"+student+emotion+str(x)+":")
        print("revObj")
        print(placedict.get(dif))
        print(student + "_" +emotion+"_"+ str(x))
        print("proceed, $after"+student+placedict.get(dif)+str(x))
=======
            if (startPos == 'right'):
                if(endPos=='left'):
                    print("place, "+s2+"+"+str(dif)+", "+startPos)
                else:
                    print("place, "+
                        students[int((students.index(s1)-(dif*2)+len(students))%len(students))]+"+"+str(dif*2)+", "+startPos)
            else:
                if(endPos=='right'):
                    print("place, "+s1+"+"+str(dif)+", "+startPos)
                else:
                    print("place, "+s1+"+"+str(dif*2)+", "+startPos)
            print("set_sprite, "+s1+", n")
            print("cPos, "+startPos)
            print("set_sprite, "+s2+", n")
            print("cPos, "+endPos)
            if(startPos=="left"):
                if(endPos=='right'):
                    print("set_sprite, "+students[(students.index(s1)+int(dif/2))%len(students)]+", n")
                else:
                    print("set_sprite, "+students[(students.index(s1)+int(dif*2))%len(students)]+", n")
            else:
                if(endPos=='left'):
                    print("set_sprite, "+students[(students.index(s1)-int(dif/2))%len(students)]+", n")
                else:
                    print("set_sprite, "+students[(students.index(s1)-int(dif*2))%len(students)]+", n")
            if(dif%2==0 and dif != 4):
                print("cPos, center")
            else:
                if(startPos=='left'):
                    print("cPos, right")
                else:
                    print("cPos, left")
            print("wait, 5")
            print("scroll, "+scrollType)
            print("}\n")
            
'''
This function generates a little under 200 frames, which hide all the background
objects that are emotions people who aren't currently feeling.
It then calls another function several times, revealing the correct emotions.
I can't think of a better, automatic way to do it.
I tested it in AAO, and there is a noticeable lag, so plan around that.
To use, just write the following in Catalysis:

wait, 1
varDef
backFromCheckAll, $frame: X$

wait, 1
proceed, checkAll

wait, 1
anc, X

X can be whatever you want. You'll be using a bunch of different X's as you
"call" this "function" throughout the course of your trial.
In the first frame, you set the return frame, which is the third frame.
In the second frame, you do the calling of the function, by which I mean you
go to the frame where the function starts.
'''
def checkall(checkAll, backFromCheckAll):
    #There are comments for where the code starts and ends for your convenience.
    print("//CODE STARTS HERE")
    if not createdPlaces:
        harmlessMakePlace()
    print("anc, "+checkAll)
    print("wait, 1\n")    
    for student in students:
        print("wait, 1")
        print("hideObj")
        for emotion in emo[student].keys():
            for place in createdPlaces:
                personInPlace = False
                for x in range(1,int(deletechars(place,alphabetplus))-1):
                    if(students[(students.index(deletechars(place,numberplus))+x)%len(students)]==student and x*2!=int(deletechars(place,alphabetplus))):
                        personInPlace = True
                if (personInPlace):
                    print(place+", "+student+"_"+emotion)
        print()
        checkemo(student)
        if(student != students[-1]):
            print("\nanc, after"+student)
        else:
            print("\nanc, afterCheckAll")
    print("wait, 1")
    print("proceed, {"+backFromCheckAll+"}\n")
    print("//CODE ENDS HERE")
        
        

#This function reveals one emotion of one student.
def checkemo(student):
    if not createdPlaces:
        harmlessMakePlace()
    print("wait, 1")
    if (student != students[-1]):
        print("condit, after"+student)
    else:
        print("condit, afterCheckAll")
    for emotion in emo[student].keys():
        print(student+"emo = "+emotion+", "+student+"_is_"+emotion)
    print()
    for emotion in emo[student].keys():
        print("anc, "+student+"_is_"+emotion)
        print("wait, 1")
        print("revObj")
        for place in createdPlaces:
            personInPlace = False
            for x in range(1,int(deletechars(place,alphabetplus))-1):
                if(students[(students.index(deletechars(place,numberplus))+x)%len(students)]==student and x*2!=int(deletechars(place,alphabetplus))):
                    personInPlace = True
            if (personInPlace):
                print(place+", "+student+"_"+emotion)
        print()
        if (student != students[-1]):
            print("wait, 1")
            print("proceed, after"+student)
            print()
        else:
            print("wait, 1")
            print("proceed, afterCheckAll")
            print()

>>>>>>> origin/master

'''
This function creates a series of macros of the type xx_y, where xx is the
character's prefix and y is the emotion suffix. This sets a character's
"emotion variable" to the correct emotion. 

That does mean it ends up looking something like:

<<<<<<< HEAD
xx_y
xx.y:
=======
xx.y
xx_y:
>>>>>>> origin/master
This is some text I (the character) am saying.

That's some redundant typing, I know,
but this way, you get that DanganRonpa effect where the background characters
<<<<<<< HEAD
are displaying the emotion they last had.
'''


def setemo():
=======
are displaying the emotion they last had, as long as you use the frames
generated by the frames() function to set them per the variables these macros
redefine.
'''


def setemo(scrollType):
>>>>>>> origin/master
    for student in students:
        for emotion in emo.get(student,"ERROR").keys():
            print(student+"_"+emotion+" {")
            print("pPos, auto")
            if(scrollType=="none" or
               scrollType =="linear" or
               scrollType =="bezier" or
               scrollType =="ease_in" or
               scrollType == "ease_out"):
                print("scroll, "+scrollType)
            print("varDef")
            print(student+"_emo, " + emotion + "\n}")
            print()


<<<<<<< HEAD
=======




>>>>>>> origin/master
'''
This function creates two macros that let you pan in on a character from the
starting point of... right next to the character.
That creates the illusion of panning when you're actually cutting. This is good
when you have identical backgrounds behind all the characters.
In addition to xx_from_left and xx_from_right, there's a third macro,
"xx_from_center". That lets you cut directly to the character, no pan.
This is useful when transitioning from any "judge" figure you have.
<<<<<<< HEAD
'''
def not_transition(direction):
    for student in students:
        if(len(direction)>0):
            print(student+"_from_"+direction+" {")
        else:
#this covers the case where someone wants to use short characters for this.
#I prefer the other way, because it's easier to read, so the code works for
#both.
            print(student+"_from_c {")
        print("erase")
#If you changed the arguments to be one letter long, you have to change
#" of center" to "c". Don't forget the space.
        if(direction[0]!='c'):
            print("place, 3wide, "+direction+" of center")
        else:
            print("place, 3wide, center")
        for x in range(students.index(student)-1,students.index(student)+1):
            newstudent = students[x%(len(students))]
            for bg in locbg.get(newstudent):
                print("RevObj")
                print(placedict.get(1))
                print(bg+"_"+str(x))                
            for fg in locfg.get(newstudent):
                print("RevObj")
                print(placedict.get(1))
                print(fg+"_"+str(x))
        print("set_sprite ," +student+", "+list(emo.get(student).keys())[0])
        print("cPos, center")
        print("}\n")
            
'''
This is important: This function shows the background objects of your
character's neighbors, and the foreground objects of your character's
neighbors, but it doesn't show your neighbors.
This is to conserve frames, which are a finite resource when making trials.
If enough people complain, I'll fix this.
'''



=======
... Or when you don't want to scroll all the way, but have two characters with
identical backgrounds and don't want to look like one of them shape-shifted.
'''

def notTransition(direction):
    for student in students:
        print(student+"_from_"+direction+" {")
        if(direction[0]!='c'):
            if(len(direction)==1):
                print("place, "+students[(students.index(student)-3)%len(students)]+"+6, "+direction+"c")
            else:
                print("place, "+students[(students.index(student)-3)%len(students)]+"+6, "+direction+" of center")
        else:
            print("place, "+students[(students.index(student)-3)%len(students)]+"+6, "+direction)        
        print("set_sprite, "+student+", n")
        print("wait, 1")
        print("}\n")
>>>>>>> origin/master






<<<<<<< HEAD

'''
This function's job is to hide every single foreground and background object.
Basically, everything Catalysis's erase doesn't do.
This function is necessary, because we only have 1 place of each size that we
reuse over and over with different backdrops (and... frontdrops?), like a stage
with actors. This function would be the equivalent of the stagehands taking the
props away for the next scene.
It's time-consuming even to type the macro into Catalysis manually, so can you
imagine putting this into AAO every time?
'''
def hideall():
    print("hideall {")
    for place in places:
        for student in students:
            emolist = emo[student]
            for emotion in emolist.keys():
                for x in range(int(place.replace("wide",""))):                
                    candidate = place+"_"+student + "_" +emotion+"_"+ str(x)                    
                    if(candidate not in setofobjs):
                        print("hideObj")
                        print(place)
                        print(student + "_" +emotion+"_"+ str(x)+"\n")
                        setofobjs.add(candidate)
            for bg in locbg[student]:
                for x in range(int(place.replace("wide",""))):
                    if((bg+"_"+str(x)) in setofobjs):
                       continue
                    print("hideObj")
                    print(place)
                    print(bg+"_"+ str(x))
                    setofobjs.add(bg+"_"+ str(x))
    print("}\n")
=======
>>>>>>> origin/master
