import numpy as np
import matplotlib.pyplot as plt

def plot(distances):
    circle1 = plt.Circle(positions[0],distances[0],color='b',fill=False)
    circle2 = plt.Circle(positions[1],distances[1],color='g',fill=False)
    circle3 = plt.Circle(positions[2],distances[2],color='r',fill=False)
    circle4 = plt.Circle(positions[3],distances[3],color='m',fill=False)

    fig = plt.figure(figsize=(9,9))
    plt.xlim(-10,10)
    plt.ylim(-10,10)
    plt.plot(positions[0][0], positions[0][1], 'bo')
    plt.text(positions[0][0] + 0.25, positions[0][1] + 0.25, "B1", color='b')
    plt.plot(positions[1][0], positions[1][1],'go')
    plt.text(positions[1][0] + 0.25, positions[1][1] + 0.25, "B2", color='g')
    plt.plot(positions[2][0], positions[2][1],'ro')
    plt.text(positions[2][0] + 0.25, positions[2][1] + 0.25, "B3", color='r')
    plt.plot(positions[3][0], positions[3][1],'mo')
    plt.text(positions[3][0] + 0.25, positions[3][1] + 0.25, "B4", color='m')
    fig.gca().add_patch(circle1)
    fig.gca().add_patch(circle2)
    fig.gca().add_patch(circle3)
    fig.gca().add_patch(circle4)
    plt.grid(b=True, which='both', color='0.65',linestyle='-')
    
def plot_point(pt):
    plt.plot(pt[0],pt[1],'ko')
    plt.text(pt[0] + 0.25, pt[1] + 0.25, "R", color='k')
    
def register(**kwargs):
    for key, val in kwargs.items():
        globals()[key] = val
        
def distance_between_points(pt1, pt2):
    return ((pt1[0] - pt2[0])**2 + (pt1[1] - pt2[1])**2)**(1/2)

        
def plot_cost(distances, cost_function):
    xvals = np.linspace(-10,10,200)
    yvals = np.linspace(-10,10,200)

    x, y = np.meshgrid(xvals,yvals)

    zvals = np.zeros([200,200])

    for i in range(200):
        for k in range(200):
            pt = [xvals[i],yvals[k]]
            zvals[i][k] = cost_function(pt, distances)


    a = list(zip(xvals, yvals, [sum(x) for x in zvals]))
    b = np.asarray(a)
    plt.pcolormesh(x, y, zvals.reshape(len(y), len(x)), cmap="plasma")
    plt.colorbar()
    plt.show()