import numpy as np
from scipy.optimize import minimize

# 定义目标函数
def objective(x):
    return (x[0] - 2)**2 + (x[1] - 3)**2

# 定义等式约束
def constraint_eq(x):
    return 2*x[0] - x[1] - 1

# 定义不等式约束
def constraint_ineq(x):
    return (x[0] - 1)**2 - x[1]

# 初始猜测
initial_guesses = [
    np.array([0, 0]),
    np.array([1, 1]),
    np.array([3, 3]),
    np.array([1.2, -1]),
    np.array([-1.2, -1])
]

# 定义约束
constraints = [
    {'type': 'eq', 'fun': constraint_eq},
    {'type': 'ineq', 'fun': constraint_ineq}
]

# 终止条件
tol = 0.0139

# 进行优化
for i, x0 in enumerate(initial_guesses):
    solution = minimize(objective, x0, method='SLSQP', constraints=constraints, tol=tol)
    print(f'Initial guess {i+1}: {x0}')
    print('Optimal solution:', solution.x)
    print('Objective value:', solution.fun)
    print('Success:', solution.success)
    print('Message:', solution.message)
    print('-----------------------------------')