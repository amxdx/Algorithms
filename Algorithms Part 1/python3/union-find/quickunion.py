class quickunion(object):
	"""docstring for quickunion"""
	def __init__(self, N):
		self.N = N
		self.id = [None]*self.N
		for i in range(0,self.N):
			self.id[i] = i
	
	def root(self, i : int):
		while (i != self.id[i]): 
			i = self.id[i]
		return i

	def union(self,p: int, q: int):
		self.id[p] = self.id[q]

	def find(self, p, q):
		a = self.root(p)
		b = self.root(q)
		return (a == b)

		
if __name__ == '__main__':
	newQF = quickunion(10)
	print(newQF.id)
	newQF.union(4,3)
	print(newQF.id)
	newQF.union(3,8)
	print(newQF.find(5,6))
	newQF.union(6,5)
	print(newQF.id)
	newQF.union(9,4)
	print(newQF.find(1,9))
	newQF.union(8,9)
	print(newQF.id)
	newQF.union(8,9)
	newQF.union(2,1)
	newQF.union(7,6)
	newQF.union(5,4)
	print(newQF.id)