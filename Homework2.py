from math import sqrt


#Question 1
a= int(input("Please enter how many coordinates you want to enter: "))
coordinates = []
i=1
while i<a+1:
    x= input("enter x" + str(i) +" : ")
    y= input("enter y" + str(i) + ": ")
    coor = (float(x),float(y))
    coordinates.append(coor)
    i=i+1

print("List of entered coordinates is: " + str(coordinates))

#Question 2
j=0
x_coordinates= []
y_coordinates=[]
while j<a:
    x_coordinates.append(coordinates[j][0])
    y_coordinates.append(coordinates[j][1])
    j=j+1

x_mean=sum(x_coordinates)/len(x_coordinates)
y_mean=sum(y_coordinates)/len(y_coordinates)

Center_of_Mass=(float(x_mean),float(y_mean))
print("Center of Mass is: " + str(Center_of_Mass))

#Question 3
distances = []
for i in range(0,a):
        dist= sqrt((coordinates[i][0]-Center_of_Mass[0])**2+(coordinates[i][1]-Center_of_Mass[1])**2)
        distances.append(dist)

print(distances)

#Question 4
index_maxDist = distances.index(max(distances))
index_minDist = distances.index(min(distances))



print("farthest point is: " + str(coordinates[index_maxDist]) + " and its distance to the center of mass is: " + str(distances[index_maxDist]))
print("closest point is: " + str(coordinates[index_minDist]) + " and its distance to the center of mass is: " + str(distances[index_minDist]))


