#date :2013-1-16
#author :zhaoliang
#function:
print "%s's height is %dcm,%s's weight is %d kg"% \
      ("xinran",168,"xinran",60);

print "%(name)s's height is %(height)dcm," \
      "%(name)s's weight is %(weight)dkg" % \
      {"name":"zhao","height":172,"weight":70};
raw_input("press<Enter>")
#name should be bracketed by ""  and  %(name) not   %(name)s yes
