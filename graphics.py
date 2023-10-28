import matplotlib
import numpy as np
import matplotlib.pyplot as plt

matplotlib.use('TkAgg')

def draw_strategies(strategy,p_strategy : list):

    strategy.set_title('Strategies')
    strategy.set_aspect(0.1)
    strategy.set_xlim((0,1))
    strategy.set_ylim((0,8))

    plt.xlabel(r'$p1$')
    plt.ylabel(r'$H$')

    #make grid

    major_x_ticks = np.arange(0, 1, 0.1)
    minor_x_ticks = np.arange(0, 1, 0.1)

    major_y_ticks = np.arange(0, 8, 1)
    minor_y_ticks = np.arange(0, 8, 1)

    strategy.set_xticks(major_x_ticks)
    strategy.set_xticks(minor_x_ticks, minor=True)
    strategy.set_yticks(major_y_ticks)
    strategy.set_yticks(minor_y_ticks, minor=True)
    strategy.tick_params(axis='both', which='major', labelsize=10)
    strategy.tick_params(axis='both', which='minor', labelsize=10)
    strategy.grid(which='both')

    plt.grid(True)

    #make axis

    plt.axhline(0, color='orange')
    plt.axvline(0, color='orange')

    #make lines

    for i in range(len(p_strategy)):
        x = np.linspace(0,1,1000)
        xa = p_strategy[i][0][0]
        xb = p_strategy[i][1][0]
        ya = p_strategy[i][0][1]
        yb = p_strategy[i][1][1]
        y = ((x-xa)/(xb-xa))*(yb-ya) + ya
        strategy.plot(x, y, linestyle='-', linewidth=2, color='black')
        strategy.annotate("B"+str(i+1), xy=(xb,((1-xa)/(xb-xa))*(yb-ya) + ya), fontsize=22)

def draw_saddle_point(strategy,saddle_point : list):
    #draw point
    dot_size = 8
    strategy.plot(saddle_point[0], saddle_point[1], 'r.', markersize=dot_size)
    strategy.annotate("N", xy=(saddle_point[0] - 0.035,saddle_point[1]-0.5), fontsize=22)

    #draw line
    x = np.linspace(saddle_point[0], saddle_point[0], 20)
    y = np.linspace(0, saddle_point[1], 20)
    strategy.plot(x, y, linestyle='--', linewidth=2, color='black')
    strategy.annotate("p1*", xy=(saddle_point[0], 0+0.15), fontsize=22)







