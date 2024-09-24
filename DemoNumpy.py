import numpy as np

#com: Tổ hợp; perm: Chỉnh hợp; factorial: Giai thừa
from math import comb, factorial, perm

import scipy.stats as ss

x = range(1, 96) # giá trị lớn nhất của k là 95

# tham số của numpy.array() là 1 mảng. 
# Tức là phải truyền mảng cho function numpy.array()
x = np.array(x) 

# Tạo ra mảng
px = []
for i in range (1, 96):
    p = comb(99 - i, 4) / comb(99, 5)
    px.append(p) 
px = np.array(px)

# Tạo phân phối của X (hàm phân phối xác suất pmf của biến ngẫu nhiên rời rạc - rv_discrete())
pmf = ss.rv_discrete(values=(x, px))

#Tính kỳ vọng
EX = pmf.mean()
print(EX)

#Tính phương sai
VX = pmf.var()
print(VX)

#Tính độ lệch chuẩn
sigma = pmf.std()
print(sigma)

cdf = ss.rv_discrete.cdf(x, px)
print(cdf)
# Tính toán trước khi import scipy.stats
# EX = np.sum(x*px)
# print(EX)

# VX = np.sum(x*x*px) - pow(EX, 2)
# print(VX)