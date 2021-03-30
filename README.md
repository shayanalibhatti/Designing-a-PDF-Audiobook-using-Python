# Designing a PDF Audiobook using Python
In this code, a simple implementation of PDF Audiobook is shown. PDF text is read to the user as audio using this code.

#### Introduction
Reading stories or essays or any text can be arduous, however an audio reading of the text is convenient and doesnt require as much concentration as reading requires. In this project, I implemented a simple PDF to audio converter. This code scans page(s) of PDF and reads it using audio, to the user. While this project is good for simple text reading, it does not perform good if a scientific paper with equations is given to it because equations are not supported to be read in pytesseract OCR library which we used to convert image to text.

#### Project Flow
Here is the project flow diagram:

![project flow](https://github.com/shayanalibhatti/PDF_text_to_audio_converter/blob/master/audiobook%20image.png?raw=true)

1) First, we take the PDF file and convert each page into image using PyMuPDF software.
2) Then, we take the image(s) and scan the text in the image using Pytesseract OCR software.
3) Then, we use Google Text to Speech (gTTS) library to convert text to audio file.
3) Lastly, we get the Pygame mixer to play the audio file loud.

#### Prerequisite software
The software libraries required to run this code can be installed using:

pip install -r requirements.txt

#### Conclusion
It was seen that the code performs really well in reading straightforward PDF text files, however, if equations are involved in the text, then the reader cannot properly read the equations. Hence, the code is good for simple text but not for scientific papers as it will fumble reading the equations. However, text will be read just fine. 

Please give a star to the repo to let me know if the work helped you.
