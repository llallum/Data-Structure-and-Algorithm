#Array insertion

LA = [1, 2, 3, 4, 5 ];
item = "AV"
k = 3
length = len(LA)

print "before insertion: ",  LA

while (length>= k):
        if length == len(LA):
                LA.append(item)
        else:
                LA[length+1] = LA[length]
        length-=1
LA[length] = item

print "after insertion ",  LA
