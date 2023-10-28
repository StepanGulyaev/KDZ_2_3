
A = [[5,4,3,2],[1,4,4,7]]

if __name__ == '__main__':
    if len(A) == 0:
       exit

    B_strategy = []

    for i in range(len(A[0])):
        B_coef_p = A[0][i] - A[1][i]
        B_free_coef = A[1][i]
        
        H_0 = B_coef_p * 0 + B_free_coef
        H_1 = B_coef_p * 1 + B_free_coef

        B_0_point = [[0,H_0],[1,H_1]]
        B_strategy.append(B_0_point)

        print("B" + str(i+1) + "= " + str(B_coef_p) + "*p1" + " + " + str(B_free_coef))

    
