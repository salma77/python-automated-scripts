import pyttsx3, PyPDF2

pdf_reader = PyPDF2.PdfReader(open('test.pdf', 'rb'))
speaker = pyttsx3.init()

for page_num in range(len(pdf_reader.pages)):
    text = pdf_reader.pages[page_num].extract_text()
    clean_text = text.strip().replace('\n', ' ')

speaker.save_to_file(clean_text, 'test.mp3')
speaker.runAndWait()

speaker.stop()