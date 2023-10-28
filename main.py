import numpy as np

from graphics import *

A = [[5,4,3,2],
     [1,4,4,7]]

def get_p_strategies(A : list):
    p_strategy = []

    for i in range(len(A[0])):
        B_coef_p = A[0][i] - A[1][i]
        B_free_coef = A[1][i]

        H_0 = B_coef_p * 0 + B_free_coef
        H_1 = B_coef_p * 1 + B_free_coef

        B_0_point = [[0, H_0], [1, H_1]]
        p_strategy.append(B_0_point)

        print("B" + str(i + 1) + "= " + str(B_coef_p) + "*p1" + " + " + str(B_free_coef))

    return  p_strategy

def get_saddle_point(p_strategy : list):
    x = np.arange(0,1,0.0001)
    global_mins = []
    for x_point in x:
        local_mins = []
        for strategy in p_strategy:
            xa = strategy[0][0]
            xb = strategy[1][0]
            ya = strategy[0][1]
            yb = strategy[1][1]
            y = ((x_point-xa)/(xb-xa))*(yb-ya) + ya
            local_mins.append([x_point,y])
        min_y_arr = list(map(lambda el: el[1],local_mins))
        min_y_index = min_y_arr.index(min(min_y_arr))
        global_mins.append(local_mins[min_y_index])
    maxmin_y_arr = list(map(lambda el: el[1], global_mins))
    maxmin_y_index = maxmin_y_arr.index(max(maxmin_y_arr))
    saddle_point = global_mins[maxmin_y_index]
    return saddle_point

def get_active_strategies(saddle_point : list, p_strategy):
    active_strategies = {}
    for i in range(len(p_strategy) - 1):
        for j in range(i,len(p_strategy)):
            xa1 = p_strategy[i][0][0]
            xb1 = p_strategy[i][1][0]
            ya1 = p_strategy[i][0][1]
            yb1 = p_strategy[i][1][1]
            y1 = ((saddle_point[0]-xa1)/(xb1-xa1))*(yb1-ya1) + ya1

            xa2 = p_strategy[j][0][0]
            xb2 = p_strategy[j][1][0]
            ya2 = p_strategy[j][0][1]
            yb2 = p_strategy[j][1][1]
            y2 = ((saddle_point[0]-xa2)/(xb2-xa2))*(yb2-ya2) + ya2
            if abs(y2 - y1) < 0.001 and abs(y1 - saddle_point[1]) < 0.001:
                active_strategies.update({"B" + str(i+1):p_strategy[i]})
                active_strategies.update({"B" + str(j+1): p_strategy[j]})
    return active_strategies

def get_q_strategies(A, active_strategies_names : list):
    num_strat = list(map(lambda x: int(x[1:]) - 1,active_strategies_names))
    q_strategy = []
    for i in range(len(A)):
        B_coef_q = A[i][num_strat[0]] - A[i][num_strat[1]]
        B_free_coef_q = A[i][num_strat[1]]

        H_0 = B_coef_q * 0 + B_free_coef_q
        H_1 = B_coef_q * 1 + B_free_coef_q

        B_0_point = [[0, H_0], [1, H_1]]
        q_strategy.append(B_0_point)

        print("f(" + str(i + 1) + "," + "q)" + "= " + str(B_coef_q) + "*q1" + " + " + str(B_free_coef_q))

    return q_strategy

def get_q_saddle_point(q_strategy : list):
    x1 = q_strategy[0][0][0]
    y1 = q_strategy[0][0][1]
    x2 = q_strategy[0][1][0]
    y2 = q_strategy[0][1][1]
    x3 = q_strategy[1][0][0]
    y3 = q_strategy[1][0][1]
    x4 = q_strategy[1][1][0]
    y4 = q_strategy[1][1][1]

    x_res = ((x1*y2 - y1*x2)*(x3-x4) - (x1-x2)*(x3*y4 - y3*x4))/((x1-x2)*(y3-y4) - (y1-y2)*(x3-x4))
    y_res = ((x_res - x1)/(x2-x1))*(y2-y1) + y1

    return [x_res,y_res]

def get_q_optimal_vector(A : list ,q_optimal:list):
    num_strat = list(map(lambda x: int(x[1:]) - 1, active_strategies_names))
    q_optimal_vector =  [0] * len(A[0])
    for i in range(len(num_strat)):
        q_optimal_vector[num_strat[i]] = q_optimal[i]
    return q_optimal_vector


if __name__ == '__main__':
    if len(A) == 0:
       exit
    p_strategy = get_p_strategies(A)
    saddle_point = get_saddle_point(p_strategy)
    print("N =", saddle_point)

    p_optimal = [saddle_point[0],1 - saddle_point[0]]

    active_strategies = get_active_strategies(saddle_point,p_strategy)
    active_strategies_names = ",".join(active_strategies.keys()).split(",")
    print("Активные стратегии: ",end="")
    print(",".join(active_strategies_names))

    q_strategy = get_q_strategies(A,active_strategies_names)
    q_saddle_point = get_q_saddle_point(q_strategy)

    q_optimal = [q_saddle_point[0],1 - q_saddle_point[0]]
    q_optimal_vector = get_q_optimal_vector(A,q_optimal)

    print("p*= ",p_optimal)
    print("q*=",q_optimal_vector)

    game_worth = saddle_point[1]
    print("Цена игры: " + str(game_worth))

    windows_size = (9,9)
    plt.figure(figsize=windows_size)
    strategy = plt.gca()
    draw_strategies(strategy,p_strategy)
    draw_saddle_point(strategy, saddle_point)

    plt.show()


    
