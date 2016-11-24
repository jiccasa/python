# Take an input as follows
# 53.1 miles or 53.1 kms
# If the user entered in miles convert to kms and viceversa
# print " 999.9 miles = 999.9 kms"

distance = input("Give a distance in either miles or kms: ")

dl = distance.split()

dist, scale = float(dl[0]), dl[1]

if scale == 'miles':
    print("%f miles = %f kms" % (dist, dist * 1.60934))
elif scale == 'kms':
    print("%f kms = %f miles" % (dist, dist * 0.621371))
else:
    print("You are a Deanzas. Give a proper distance")

