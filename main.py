from monday import Monday
from tuesday import Tuesday
from wednesday import Wednesday
from thursday import Thursday
from friday import Friday
from saturday import Saturday

day = input('На какой день выдать рассписание: ')
if day == '1': 
	Monday()
elif day == '2':
	Tuesday()
elif day == '3':
	Wednesday()
elif day == '4':
	Thursday()
elif day == '5':
	Friday()
elif day == '6':
	Saturday()
