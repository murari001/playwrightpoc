def gradient_descent(n, data, k, alpha, w_init, b_init):
    # Initialize w and b
    w = w_init
    b = b_init
    
    # Perform gradient descent for k iterations
    for _ in range(k):
        # Calculate the gradient for w and b
        w_gradient = 0
        b_gradient = 0
        
        for i in range(n):
            x_i = data[i][0]
            y_i = data[i][1]
            # Predicted value
            y_pred = w * x_i + b
            # Gradient calculation
            w_gradient += (y_pred - y_i) * x_i
            b_gradient += (y_pred - y_i)
        
        # Average the gradients
        w_gradient /= n
        b_gradient /= n
        
        # Update w and b
        w = w - alpha * w_gradient
        b = b - alpha * b_gradient
    
    # Print the final values of w and b, rounded to 2 decimal places
    print(f"{w:.2f} {b:.2f}")

