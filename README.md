# PDF_to_audio_converter
In this code, a simple implementation of PDF to audio converter is shown. R

#### Introduction
Reading stories or essays or any text can be arduous, however an audio reading of the text is convenient and doesnt require much concentration as reading requires. In this project, I implemented a simple PDF to audio converter. This code scans page(s) of PDF and reads it using audio, to the user. While this project is good for simple text reading, it does not perform good if a scientific paper with equations is given to it because equations are not supported to be read in pytesseract library which we used to convert PDF image to text.

#### Project Flow:
Here is the project flow diagram:




1) First, we take the PDF file and convert each page into image using PyMuPDF software.
2) Then, we take the image(s) and scan the text in the image using Pytesseract OCR software.
3) Lastly, we get the Pygame mixer to read the text loud.
