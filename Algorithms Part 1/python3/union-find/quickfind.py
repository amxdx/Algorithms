
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

if __name__ == '__main__':
	newQF = quickfind(10)
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