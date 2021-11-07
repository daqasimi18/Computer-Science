'''
Darab Ali Qasimi
Project 1
PDF to audio conversion
'''
# Importing necessary tools 
import PyPDF2
import os
from gtts import gTTS
import requests
import validators

while 1:
    # Ask user for the URL of an online PDF file
    input_URL = str(input("Enter the URL of the PDF file here: "))
    # Check if the user provided URL is valid
    url_valid = validators.url(input_URL)
    # Until the user doesn't provide a valid URL they can keep entering trying
    if url_valid == True:
        break
        
# Get the PDF file that exists in the URL address    
get_pdf = requests.get(input_URL)
with open('Book.pdf', 'wb') as pdf_file:
    # Write the content of the provided URL file to the new created file
    pdf_file.write(get_pdf.content)

# Opening the PDF file with python pdf reader
pdf_book = open('Book.pdf', 'rb')
pdf_read = PyPDF2.PdfFileReader(pdf_book)

# The pdf pages are assumed to start at index 0.
pdf_page = 0
while 1:
    # Ask user for PDF file page number to convert to audio. 
    get_pdf_page = int(input("Enter the page number to convert to audio: "))
    # The pdf page number entered by the user has to be within the range of pages in the PDF file
    if get_pdf_page <= pdf_read.numPages:
        pdf_page = get_pdf_page - 1
        break
    # If the entered page number is invalid they will see the following error on the screen
    else:
        raise ValueError("The entered page number is invalid")

# Store the page numbers that are converted to audio in a new file.
record = open('converted.txt', 'a+')
record.write("%s\r\n" % str(get_pdf_page))
    
# Ask the user for the speed of the audio. A speed of False is fast, and True is slow.        
speed = None
user_req = str(input("Enter 'f' for fast speed audio or 's' for slow: "))
if user_req == 'f' or 'F':
    speed = False
# Every other character that's entered is interpreted as a fast speed
else:
    speed = True

# Extracting the page, and converting it to mp3 using gtts 
for pages in range(pdf_read.numPages):
    # Convert only the page that the user has requsted
    if pages == pdf_page:
        # Extract the text from the requested page
        extract = pdf_read.getPage(pages).extractText()
        # The default language is set to English
        language = 'en'
        output = gTTS(text = extract, lang = language, slow = speed)
        output.save("output.mp3")
        os.system("start output.mp3")
        break
          
pdf_book.close()        
record.close() 




'''
Darab Ali Qasimi
Project 1
PDF to audio conversion

# Importing necessary tools 
import PyPDF2
import os
from gtts import gTTS
import requests
import validators

# Ask user for a PDF file URL 
while 1:
    input_URL = str(input("Enter the URL of the PDF file here: "))
    # Check if the user provided URL is valid
    url_valid = validators.url(input_URL)
    # Until the user don't provide a valid URL they can keep entering URLs
    if url_valid == True:
        break
        
# Write a new file which is a copy of the file that exists in the URL address    
get_pdf = requests.get(input_URL)
with open('Book.pdf', 'wb') as pdf_file:
    pdf_file.write(get_pdf.content)

# Opening the PDF file
pdf_book = open('Book.pdf', 'rb')
pdf_read = PyPDF2.PdfFileReader(pdf_book)

# Ask user for PDF file page number to convert to audio. 
# The pdf pages are assumed to start at index 0.
pdf_page = 0
while 1:
    get_pdf_page = int(input("Enter the page number to convert to audio: "))
    # The pdf page number entered by the user has to be valid
    if get_pdf_page <= pdf_read.numPages:
        pdf_page = get_pdf_page - 1
        break
# If the entered page number is not valid they will get an error on the screen
else:
    raise ValueError("The entered page number is invalid")

# Store the page numbers that are converted to audio in a new file.
record = open('converted.txt', 'a+')
record.write("%s\r\n" % str(get_pdf_page))
    
# Ask the user for the speed of the audio. A speed of False is fast, and True is slow.        
speed = None
user_req = str(input("Enter 'f' for fast speed audio or 's' for slow: "))
if user_req == 'f' or 'F':
    speed = False
else:
    speed = True

# Extracting the page, and converting it to mp3 using gtts 
for pages in range(pdf_read.numPages):
    if pages == pdf_page:
        extract = pdf_read.getPage(pages).extractText()
        language = 'en'
        output = gTTS(text = extract, lang = language, slow = speed)
        output.save("output.mp3")
        os.system("start output.mp3")
        break
          
pdf_book.close()        
record.close() 
'''
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

