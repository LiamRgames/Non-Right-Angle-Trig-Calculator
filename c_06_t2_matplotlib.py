#Importing Modules
import matplotlib.pyplot as plt
#Data Values
sides = [5,10,7]
#Graph Styling/Plotting
plt.plot(-7.5,2.5,marker='o')
plt.plot(-2.5,2.5,marker='o')
plt.plot(-5,7.5,marker='o')
plt.plot((-7.5, -2.5, -5.0, -7.5), (2.5, 2.5, 7.5, 2.5))

#Labels
plt.title("Your Triangle")
plt.axis('off')
plt.annotate("A",(-7.5,2.5),textcoords="offset points",xytext=(-10,-10))
plt.annotate("B",(-2.5,2.5),textcoords="offset points",xytext=(7,-10))
plt.annotate("C",(-5,7.5),textcoords="offset points",xytext=(0,5))
plt.annotate(f"Side AB: {sides[2]}m",(-5,2.5),textcoords="offset points",xytext=(0,-15))
plt.annotate(f"Side BC: {sides[0]}m",(-3.75,5),textcoords="offset points",xytext=(0,10))
plt.annotate(f"Side AC: {sides[1]}m",(-6,5),textcoords="offset points",xytext=(-90,10))

#Show Graph
plt.show()