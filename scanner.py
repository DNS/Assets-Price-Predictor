
import json



#s = json.loads('   {"one" : 111, "two" : 222, "three" : 333}   ')

#print( s['two'] )


# load json from file or url
s = json.load('http://localhost/json.html')
print( s['two'] )

