
class quickfind(object):

	def __init__(self, N):
		self.N = N
		self.id = [None]*self.N
		for i in range(0,self.N):
			self.id[i] = i

	def find(self, p: int,q: int) -> bool : 
		if (self.id[p] == self.id[q]):
			return True
		else:
			return False

	def union(self, p: int, q: int):
		b = self.id[p]
		a = self.id[q] 
		if a == b:
			pass
		else: 
			self.id[q] = a
			for i in range(0,self.N):
				if self.id[i] == b:
					self.id[i] = a
