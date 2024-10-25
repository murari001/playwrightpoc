def matrix_factorization_2state(E0, M0, time_periods):

    transition_matrix = [[0.50, 0.25], [0.50, 0.75]]  

    E, M = E0, M0
    
    for i in range(1, time_periods + 1):

        E_new = E * transition_matrix[0][0] + M * transition_matrix[1][0]
        M_new = E * transition_matrix[0][1] + M * transition_matrix[1][1]
        
        E, M = E_new, M_new
        
        print(f"After iteration {i}: E = {E:.4f}, M = {M:.4f}")
    
    print(f"Final market shares after {time_periods} iterations:")
    print(f"Region A = {E:.4f}, Region B = {M:.4f}")


