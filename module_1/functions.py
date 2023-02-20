import random

index = 0
degree = random.randint(3, 6)
coefs = []

for i in range(degree + 1):
    coefs.append(random.randint(1, 100))

def get_derivative(degree, coefs, idx):
    new_coefs = []
    
    for i in coefs:
        i = i * (degree - idx)
        new_coefs.append(i)
        idx += 1
    
    return new_coefs    
    
derivative_1_coefs = get_derivative(degree, coefs, index)
derivative_2_coefs = get_derivative(degree - 1, derivative_1_coefs, index)
derivative_3_coefs = get_derivative(degree - 2, derivative_2_coefs, index)

print(coefs)
print(derivative_1_coefs)
print(derivative_2_coefs)
print(derivative_3_coefs)

final_array = [coefs, derivative_1_coefs, derivative_2_coefs, derivative_3_coefs]
print(final_array)