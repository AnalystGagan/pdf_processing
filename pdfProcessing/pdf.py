import PyPDF2

with open('dummy.pdf','rb') as file:
	reader = PyPDF2.PdfFileReader(file) #readfile
	page = reader.getPage(0) #selectthe page that needed action
	page.rotateCounterClockwise(90) #rotate page by 90deg ccw
	writer = PyPDF2.PdfFileWriter() #
	writer.addPage(page) #add page to the writer object
	with open('tilt.pdf','wb') as new_file:
		writer.write(new_file) #write new pahe to a new_file


