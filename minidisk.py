import numpy as np
from copy import deepcopy
from collections import namedtuple

Circle = namedtuple("Circle", ["center", "radius"], defaults=[np.array([0,0]), 0])
def circle_through(points: list) -> Circle:
	if len(points) == 0:
		return Circle()

	a = points[0]
	if len(points) == 1:
		return Circle(a, 0)

	b = points[1] - a
	if len(points) == 2:
		return Circle(a + b/2, float(np.linalg.norm(b))/2)

	if len(points) == 3:
		c = points[2] - a
		b_sq = np.dot(b, b)
		c_sq = np.dot(c, c)
		d = np.linalg.det([b,c])
		u = np.array([
			c[1] * b_sq - b[1] * c_sq,
			b[0] * c_sq - c[0] * b_sq
		])
		u /= d
		return Circle(a + u/2, float(np.linalg.norm(u))/2)

	return Circle()

def inside_circle(p, circle: Circle) -> bool:
	offset = p - circle.center
	return np.dot(offset, offset) <= circle.radius**2

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
