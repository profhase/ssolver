class Entity(object):

	def __init__(self, fields):
		self.fields = fields
		values = [f.values for f in fields]
		self.values = set(values)

	def is_valid(self,values):
		# TODO check for redundant values
		if not all([values in range(1,10),
					len(values==9)]):
			return False
		else:
			return True

	@property
	def options(self):
		return set(range(1,10))-self.values


class Line(Entity):

	def __init__(self, num, fields):
		self.num = num
		super(Line, self).__init__(fields)

		
class Square(Entity):

	def __init__(self,ko):
		self.ko = ko
		super(Square,self).__init__(fields)
