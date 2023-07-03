# Given a word w 
# and some text t, find whether w is in t. 
# For example: 
#w="nest", t="I built a nest and tested it."
#output: "here"
#example 2:
#w="runs", t="The dog"
#output: "not here"
#Example 3: 
#w="April", t="april showers bring may flowers"
#output: "not here"


# eval the word (w) and see if its in text (t)

def isithere(w, t):
    t1 = t.split()
    if w in t1:
        return "here"
    else:
        return "not here"
    

print(isithere("April", "april showers bring may flowers"))

t2 = "I built a nest and tested it."
print(t2.split())