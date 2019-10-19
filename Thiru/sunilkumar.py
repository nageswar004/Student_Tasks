cricket = """ country opponent score
india srilanka 98
srilanka aus 106
aus eng 104
india wi 146
srilanka india 98
pak srilanka 68
aus india 60
pak aus 36 """

s = {}
for row in cricket.splitlines()[1:]:
	dt= row.split()
	if dt[0] not in s:
		s[dt[0]]=[int(dt[-1])]
	else:
		s[dt[0]].append(int(dt[-1]))
		print([i for i in s if max(s[i])<100])
	#
	def check_denom(f):
		def wrapper(a,b):
			if b!=0:
				return f(a,b)
			else:
				return "denom is not 0"
		return wrapper
@check_denom 
def div(a,b):
	return a/b

print(div(10,2))


a =10 
b =20
c =30
d =40
	