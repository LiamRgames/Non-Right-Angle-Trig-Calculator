#Importing Modules
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import rotate_axes

#Data Values
side_a = 5
side_b = 10
side_c = 7
#Graph Styling/Plotting
plt.plot(-7.5,2.5,marker='o')
plt.plot(-2.5,2.5,marker='o')
plt.plot(-5,7.5,marker='o')
plt.plot((-7.5, -2.5, -5.0, -7.5), (2.5, 2.5, 7.5, 2.5))

#Labels
plt.title("Your Triangle")
plt.annotate("A",(-7.5,2.5),textcoords="offset points",xytext=(-10,-10))
plt.annotate("B",(-2.5,2.5),textcoords="offset points",xytext=(7,-10))
plt.annotate("C",(-5,7.5),textcoords="offset points",xytext=(0,5))
plt.annotate(f"Side AB: {side_c}m",(-5,2.5))
plt.annotate(f"Side BC: {side_a}m",(-3.75,5))
plt.annotate(f"Side AC: {side_b}m",(-6,5))

#Show Graph
plt.show()