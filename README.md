# PDF Reader 
In this code, a simple implementation of PDF text reader is shown. PDF text is read to the user as audio using this code.

#### Introduction
Reading stories or essays or any text can be arduous, however an audio reading of the text is convenient and doesnt require as much concentration as reading requires. In this project, I implemented a simple PDF to audio converter. This code scans page(s) of PDF and reads it using audio, to the user. While this project is good for simple text reading, it does not perform good if a scientific paper with equations is given to it because equations are not supported to be read in pytesseract OCR library which we used to convert image to text.

#### Project Flow
Here is the project flow diagram:


![project flow](https://user-images.githubusercontent.com/41015749/68516420-9c843680-0249-11ea-8c1f-f57c38f3447e.png)


1) First, we take the PDF file and convert each page into image using PyMuPDF software.
2) Then, we take the image(s) and scan the text in the image using Pytesseract OCR software.
3) Then, we use Google Text to Speech (gTTS) library to convert text to audio file.
3) Lastly, we get the Pygame mixer to play the audio file loud.

#### Prerequisite software
The software libraries required to run this code can be installed using:
1) pip install Pillow -------- image reader library
2) pip install PyMuPDF ------- library to convert PDF page to image
3) pip install pytesseract --- Image to text converting Optical Character Recognition library
4) pip install pygame -------- pygame to play audio
5) pip install gTTS   -------- Google Text To Speech
6) pip install pysimplegui --- This library makes GUI development far simpler than tkinter.

#### Conclusion
It was seen that the code performs really well in reading straightforward PDF text files, however, if equations are involved in the text, then the reader cannot properly read the equations. Hence, the code is good for simple text but not for scientific papers as it will fumble reading the equations. However, text will be read just fine. 

#### Future Work
This code can be extended to make a book reading software or combined with machine learning to make really interesting story reader with interactive sounds based on situation depicted in the text.
