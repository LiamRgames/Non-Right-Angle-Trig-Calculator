#Importing Modules
import matplotlib.pyplot as plt
import matplotlib.patches as patches

#Data Values
sides = [5,10,7]
angles = [65,35,80]

#Graph Styling/Plotting
fig, ax = plt.subplots()
plt.plot(-7.5,2.5,marker='o')
plt.plot(-2.5,2.5,marker='o')
plt.plot(-5,7.5,marker='o')
plt.plot((-7.5, -2.5, -5.0, -7.5), (2.5, 2.5, 7.5, 2.5))
plt.title("Your Triangle")
plt.axis('off')
plt.annotate("A",(-7.5,2.5),textcoords="offset points",xytext=(-10,-10))
plt.annotate("B",(-2.5,2.5),textcoords="offset points",xytext=(7,-10))
plt.annotate("C",(-5,7.5),textcoords="offset points",xytext=(0,5))
plt.annotate(f"Side AB: {sides[2]}m",(-5,2.5),textcoords="offset points",xytext=(0,-15))
plt.annotate(f"Side BC: {sides[0]}m",(-3.75,5),textcoords="offset points",xytext=(0,10))
plt.annotate(f"Side AC: {sides[1]}m",(-6,5),textcoords="offset points",xytext=(-90,10))

#Angle Arc Plotting
angle_arc_A = patches.Arc(xy=(-7.5,2.5),width=1,height=1,angle=360,theta1=0,theta2=65)
angle_arc_B = patches.Arc(xy=(-2.5,2.5),width=1,height=1,angle=115,theta1=0,theta2=65)
angle_arc_C = patches.Arc(xy=(-5,7.5),width=1,height=1,angle=245,theta1=0,theta2=55)
ax.add_patch(angle_arc_A)
ax.add_patch(angle_arc_B)
ax.add_patch(angle_arc_C)
plt.annotate(f"{angles[0]}°",(-7.5,2.5),textcoords="offset points",xytext=(30,12))
plt.annotate(f"{angles[1]}°",(-2.5,2.5),textcoords="offset points",xytext=(-50,12))
plt.annotate(f"{angles[2]}°",(-5,7.5),textcoords="offset points",xytext=(-8,-30))

#Limits
plt.xlim((-10,0))
plt.ylim((0,10))

#Show Graph
plt.show()