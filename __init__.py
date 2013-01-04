from django.db import models
from .constants import DEFAULT_NUMBER_BITS
from .version import Version
from utils import convert_version_string_to_int, convert_version_int_to_string

class VersionField(models.PositiveIntegerField):
	"""
	A Field where version numbers are input/output as strings (e.g. 3.0.1)
	but stored in the db as converted integers for fast indexing
	"""
	description = "A version number (e.g. 3.0.1)"

	__metaclass__ = models.SubfieldBase

	def __init__(self, number_bits=DEFAULT_NUMBER_BITS, *args, **kwargs):
		self.number_bits = number_bits
		super(VersionField, self).__init__(*args, **kwargs)

	def to_python(self,value):
		if isinstance(value, Version):
			return Version
		
		if isinstance(value,basestring):
			return Version(value,self.number_bits)

		return Version(convert_version_int_to_string(value,self.number_bits),self.number_bits)

	def get_prep_value(self,value):
		if isinstance(value,basestring):
			return int(Version(value,self.number_bits))
		return int(value)