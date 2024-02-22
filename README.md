1. The PDF must be located in the same directory as the Python-File.
2. The PDF must be named "test.pdf"

All of the pages in the PDF are going to be converted to high quality jpgs.

The Tkinter-Window that opens next can be ignored (closed) if not needed.
The Buttons copy the seperate pages or (in case of the last Button) all of them at once.
The Pages are in an Base64-format, with the prefix "
var imgData_[Page number] = 'data:image/jpeg;base64,/9j/'
".

I've created this script for an personal Project to enter PDFs to a website. I've used "jsPDF" to create these PDFs.
Thats why  the prefix exists.