def update_parameters(row_U, column_U, U, row_V, column_V, V, row_gradients_U, column_gradients_U, gradients_U, row_gradients_V, column_gradients_V, gradients_V, learning_rate):
    # Update the user matrix U
    for i in range(row_U):
        for j in range(column_U):
            U[i][j] -= learning_rate * gradients_U[i][j]
    
    # Update the movie matrix V
    for i in range(row_V):
        for j in range(column_V):
            V[i][j] -= learning_rate * gradients_V[i][j]
    
    # Return the updated matrices
    return U, V
