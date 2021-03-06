""" Site object, which handles parsing a site/game for Update posts.  """


class Site:
	def __init__(self, name, icon=None, homepage=None):
		self.enabled = False  # Off by default.
		self.name = name
		self.icon = icon
		self._homepage = homepage

	def load(self, values):
		for k, v in values.items():
			if str(k).startswith('_') or k == 'name' or k not in vars(self):
				continue  # !cover
			setattr(self, k, v)
		#  self.__dict__.update(**values)

	def get_save_obj(self):
		ret = {}
		for k, v in vars(self).items():
			if not k.startswith('_') and k != 'name':
				ret[k] = v
		return ret

	def scan(self):
		""" Generator that should yield any Update() objects it's able to generate. """
		return []  # !cover

	def formatted_name(self, name=None):
		""" Returns this object's name, stripped of invalid characters. If provided, it formats that name instead. """
		name = name if name else self.name
		return (''.join(s for s in name.lower() if s.isalnum() or s == ' ')).title()

	def get_homepage(self):
		return self._homepage  # !cover

