import time
import webbrowser

TotalBreak = 3
BreakCount = 0

print ("The current time is "+time.ctime() )
while (BreakCount < TotalBreak) :
    time.sleep(5)
    webbrowser.open("https://classroom.udacity.com/courses/ud036/lessons/993460168/concepts/9977893120923")
    print ("The current time is "+time.ctime() )
    print BreakCount
    BreakCount = BreakCount + 1