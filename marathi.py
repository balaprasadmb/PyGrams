# -*- coding: utf-8 -*-
from datetime import date
bala = u'बालाप्रसाद'
print bala
s = u'बोला : '
b = "maze naav 'python' ase aahe. mee ek sangank aadnyawali bhasha aahe."
dd = 19
mm = 3
yyyy = 1991
todays_date = date.today()
age_string = 'maze vay ' + str(abs(todays_date.year - yyyy)) + ' varshe ' + str(abs(todays_date.month - mm)) + ' mahine ' + str(abs(todays_date.day)) + ' divas evadhe aahe.'
print age_string
grammer = {'tuze':{'naav':{'kay':{'aahe?': b,'aahe': b, 'aahe ?': b, 'sang': b, '*': b}}, 'vay':{'kay':{'aahe?': age_string,'aahe': age_string, 'aahe ?': age_string, 'sang': age_string}}}}
value = {}
while True:
	dummy = grammer
	print s
	input_str = raw_input()
	tokens = input_str.split()
	for token in tokens:
		print 'token: ' + str(token)
		if dummy.has_key(token):
			print 'has key'
			value = dummy[token]
		elif dummy.has_key(token):
			print 'not matching'
			value = dummy['*']
		else:
			print 'kahich nahi'
			value = 'tumche grammer chukat aahe'
		dummy = value
		print 'Val:' + str(value)
		if type(value)==str:
			print str(value)
			break
