def dot_product(vector_x, vector_y):
    if len(vector_x) != len(vector_y):
        raise ValueError(len(vector_x) + "!=" + len(vector_y))
    vector_length = len(vector_x)
    result = 0
    for i in range(vector_length):
        result += vector_x[i] * vector_y[i]
    print(f"dot product result is {result}.")
    return result

