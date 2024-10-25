def matrix_factorization_3state(E0, M0, H0, transition_matrix):
    threshold = 0.0001
    iteration = 0

    transposed_matrix = [list(row) for row in zip(*transition_matrix)]

    while True:
        new_E = (E0 * transposed_matrix[0][0] +
                  M0 * transposed_matrix[1][0] +
                  H0 * transposed_matrix[2][0])
        new_M = (E0 * transposed_matrix[0][1] +
                  M0 * transposed_matrix[1][1] +
                  H0 * transposed_matrix[2][1])
        new_H = (E0 * transposed_matrix[0][2] +
                  M0 * transposed_matrix[1][2] +
                  H0 * transposed_matrix[2][2])

        if (abs(new_E - E0) <= threshold and 
            abs(new_M - M0) <= threshold and 
            abs(new_H - H0) <= threshold):
            break

        E0, M0, H0 = new_E, new_M, new_H
        iteration += 1

    print(iteration)
    print(f"{E0:.4f} {M0:.4f} {H0:.4f}")
    