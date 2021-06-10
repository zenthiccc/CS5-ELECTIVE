filler = "--------------------------------"

class node:
    def __init__(self,slang=None,meaning=None,usage=None):
    	self.slang=slang
    	self.meaning=meaning
    	self.usage=usage
    	self.left_child=None
    	self.right_child=None

      
class binary_search_tree:
	def __init__(self):
		self.root=None

	def add(self,slang,meaning,usage):
		if self.root==None:
			self.root=node(slang,meaning,usage)
		else:
			self.recursive_add(slang,meaning,usage, self.root)

	def recursive_add(self,slang,meaning,usage,current_node):
		if slang<current_node.slang:
			if current_node.left_child==None:
				current_node.left_child=node(slang,meaning,usage)

			else:
				self.recursive_add(slang,meaning,usage,current_node.left_child)
		elif slang>current_node.slang:
			if current_node.right_child==None:
				current_node.right_child=node(slang, meaning, usage)

			else:
				self.recursive_add(slang,meaning,usage,current_node.right_child)

	def display(self):
		if self.root!=None:
			self.recursive_display(self.root)
		else: 
			print("Dictionary is empty...")
			print(filler)
			
	def recursive_display(self,current_node):
		if current_node!=None:
			self.recursive_display(current_node.left_child)
			print("Slang: " + str(current_node.slang))
			print("Meaning: " + str(current_node.meaning))
			print("Usage: " + str(current_node.usage))
			print(filler)
			self.recursive_display(current_node.right_child)

	def search(self,slang):
		if self.root!=None:
			return self.recursive_search(slang,self.root)
		else:
			return None


	def recursive_search(self,slang,current_node):
		if slang==current_node.slang:
			print(filler)
			print("Found a match!")
			print(filler)
			print("Slang: " + str(current_node.slang))
			print("Meaning: " + str(current_node.meaning))
			print("Usage: " + str(current_node.usage))
			print(filler)
		elif slang<current_node.slang and current_node.left_child!=None:
			return self.recursive_search(slang,current_node.left_child)
		elif slang>current_node.slang and current_node.right_child!=None:
			return self.recursive_search(slang,current_node.right_child)

	def verify(self,slang):
		if self.root!=None:
			return self.recursive_verify(slang,self.root)
		else:
			return False

	def recursive_verify(self,slang,current_node):
		if slang==current_node.slang:
			return True	
		elif slang<current_node.slang and current_node.left_child!=None:
			return self.recursive_verify(slang,current_node.left_child)
		elif slang>current_node.slang and current_node.right_child!=None:
			return self.recursive_verify(slang,current_node.right_child)
		return False
