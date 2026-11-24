import numpy as np

#두 벡터
u = np.array([3, 1, 0])
v = np.array([1, 3, 2])

#외적
cross_product = np.cross(u, v)

#넓이 = 외적 벡터의 길이
sqr_length = np.dot(cross_product, cross_product)
area = np.linalg.norm(cross_product)

print("u ' v =", cross_product)
print(f"넓이의 제곱 = {sqr_length}")
print(f"평행사변형의 넓이 = {area:.6f}")