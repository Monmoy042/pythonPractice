# Some methods in python
for i in range(0,21):
    # print i
    print str(i).rjust(2)

s= "100"
print s.rjust(10) # Right justify
print s.ljust(10) # Left justify
print s.center(10) # Center justify

# zfill method
p = "360"
print p.zfill(6)
p = 377
print str(p).zfill(5)
q = -360
print str(q).zfill(10)

# Format method
print "{0} vs {1}".format("Bangladesh","Srilanka")
print "{1} vs {0}".format("Bangladesh","Srilanka")
print "{team1} vs {team2}".format(team1="England",team2="India")
