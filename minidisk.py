import numpy as np
import numpy.linalg as linalg
from copy import deepcopy
from collections import namedtuple

EPSILON = 1e-5

Circle = namedtuple("Circle", ["center", "radius"], defaults=[np.array([0,0]), 0])
def circle_through(points: list) -> Circle:
	if len(points) == 0:
		return Circle(np.zeros(2), 0)

	a = points[0]
	if len(points) == 1:
		return Circle(a, 0)

	b = points[1] - a
	if len(points) == 2:
		return Circle(a + b/2, float(linalg.norm(b))/2)

	c = points[2] - a
	b_sq = np.dot(b, b)
	c_sq = np.dot(c, c)
	d = linalg.det([b,c])
	u = np.array([
		c[1] * b_sq - b[1] * c_sq,
		b[0] * c_sq - c[0] * b_sq
    ])
	u /= d
	return Circle(a + u/2, float(linalg.norm(u))/2)

def inside_circle(p, circle: Circle) -> bool:
	offset = p - circle.center
	return np.dot(offset, offset) <= circle.radius**2 + EPSILON

def minidisk(P: list, R: list = []):
	P_ = deepcopy(P)
	R_ = deepcopy(R)
	if len(P_) == 0 or len(R_) == 3:
		S = circle_through(R_)
	else:
		p = P_.pop()
		S = minidisk(P_, R_)
		if S.radius == 0 or not inside_circle(p, S):
			S = minidisk(P_, R_ + [p])
	return S
