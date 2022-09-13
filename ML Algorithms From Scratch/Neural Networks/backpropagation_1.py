x = [1.0, -2.0, 3.0]
w = [-3.0, -1.0, 2.0]
b = 1.0

# forward pass
xw0 = x[0] * w[0]
xw1 = x[1] * w[1]
xw2 = x[2] * w[2]

z = xw0 + xw1 + xw2
y = max(z, 0)

# backward pass
dvalue = 1.0 # assume gradient received from the next layer
drelu_dz = dvalue * (1. if z > 0 else 0.)

# partial differentiation of a sum is 1
dsum_dxw0 = 1
dsum_dxw1 = 1
dsum_dxw2 = 1
dsum_db = 1

# partial differentiation wrt to the sum
drelu_dxw0 = drelu_dz * dsum_dxw0
drelu_dxw1 = drelu_dz * dsum_dxw1
drelu_dxw2 = drelu_dz * dsum_dxw2
drelu_db = drelu_dz * dsum_db

# partial differentiation of the multiplication
dmul_dx0 = w[0]
dmul_dw0 = x[0]

dmul_dx1 = w[1]
dmul_dw1 = x[1]

dmul_dx2 = w[2]
dmul_dw2 = x[2]

# with respect to inputs
drelu_dx0 = drelu_dxw0 * dmul_dx0
drelu_dx1 = drelu_dxw1 * dmul_dx1
drelu_dx2 = drelu_dxw2 * dmul_dx2

# with respect to weights
drelu_dw0 = drelu_dxw0 * dmul_dw0
drelu_dw1 = drelu_dxw1 * dmul_dw1
drelu_dw2 = drelu_dxw2 * dmul_dw2


print(drelu_dx0, drelu_dx1, drelu_dx2)
print(drelu_dw0, drelu_dw1, drelu_dw2)

dx = drelu_dx0 + drelu_dx1 + drelu_dx2
dw = drelu_dw0 + drelu_dw1 + drelu_dw2
db = drelu_db
print(dx, dw, db)