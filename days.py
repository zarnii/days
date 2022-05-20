import openpyxl


book = openpyxl.open("lessons.xlsx", read_only = True)
sheet = book.active

teacher_name = input('Введите свою фамилию: ')

def Mоnday():
	answer_given = False

	if answer_given == False:
		num = 26
		teacher = sheet[f'K{num}'].value
		if teacher_name != None:
			teacher = teacher[:-5]  
			if teacher_name == teacher:
				time = sheet[f'H{num}'].value
				lesson = sheet[f'I{num}'].value
				room = sheet[f'L{num}'].value
				group = sheet[f'I{num}'].value
				print(f'{teacher_name} время: {time}, дисциплина: {lesson}, аудитория: {room}, группа: {group}')
				answer_given = True
	

	if answer_given == False:
		#27
		num += 1
		teacher = sheet[f'K{num}'].value
		if teacher_name != None:
			teacher = teacher[:-5] 
			if teacher_name == teacher:
				time = sheet[f'H{num}'].value
				lesson = sheet[f'I{num}'].value
				room = sheet[f'L{num}'].value
				group = sheet[f'I{num}'].value
				print(f'{teacher_name} время: {time}, дисциплина: {lesson}, аудитория: {room}, группа: {group}')
				answer_given = True


	if answer_given == False:
		#28
		num += 1
		teacher = sheet[f'K{num}'].value
		if teacher_name != None:
			teacher = teacher[:-5] 
			if teacher_name == teacher:
				time = sheet[f'H{num}'].value
				lesson = sheet[f'I{num}'].value
				room = sheet[f'L{num}'].value
				group = sheet[f'I{num}'].value
				print(f'{teacher_name} время: {time}, дисциплина: {lesson}, аудитория: {room}, группа: {group}')
				answer_given = True


	if answer_given == False:
		#29
		num += 1
		teacher = sheet[f'K{num}'].value
		if teacher_name != None:
			teacher = teacher[:-5] 
			if teacher_name == teacher:
				time = sheet[f'H{num}'].value
				lesson = sheet[f'I{num}'].value
				room = sheet[f'L{num}'].value
				group = sheet[f'I{num}'].value
				print(f'{teacher_name} время: {time}, дисциплина: {lesson}, аудитория: {room}, группа: {group}')
				answer_given = True


	if answer_given == False:
		#30
		num += 1
		teacher = sheet[f'K{num}'].value
		if teacher_name != None:
			teacher = teacher[:-5] 
			if teacher_name == teacher:
				time = sheet[f'H{num}'].value
				lesson = sheet[f'I{num}'].value
				room = sheet[f'L{num}'].value
				group = sheet[f'I{num}'].value
				print(f'{teacher_name} время: {time}, дисциплина: {lesson}, аудитория: {room}, группа: {group}')
				answer_given = True


	if answer_given == False:
		#31
		num += 1
		teacher = sheet[f'K{num}'].value
		if teacher_name != None:
			teacher = teacher[:-5] 
			if teacher_name == teacher:
				time = sheet[f'H{num}'].value
				lesson = sheet[f'I{num}'].value
				room = sheet[f'L{num}'].value
				group = sheet[f'I{num}'].value
				print(f'{teacher_name} время: {time}, дисциплина: {lesson}, аудитория: {room}, группа: {group}')
				answer_given = True


	if answer_given == False:
		#32
		num += 1
		teacher = sheet[f'K{num}'].value
		if teacher_name != None:
			teacher = teacher[:-5] 
			if teacher_name == teacher:
				time = sheet[f'H{num}'].value
				lesson = sheet[f'I{num}'].value
				room = sheet[f'L{num}'].value
				group = sheet[f'I{num}'].value
				print(f'{teacher_name} время: {time}, дисциплина: {lesson}, аудитория: {room}, группа: {group}')
	
			
Mоnday()