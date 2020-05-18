from PIL import Image
import numpy
im=Image.open(r'c:\Users\rajes\Pythoncode\.vscode\qstp.jpg')
np_im=numpy.array(im)
# inverting the image
invert=255-np_im
finalim=Image.fromarray(invert)
finalim.show()
finalim.save(r'c:\Users\rajes\Pythoncode\.vscode\finalqstp.jpg')
# converting into grayscale image
grayim=numpy.mean(np_im, axis=2)
finalgrayim=Image.fromarray(grayim)
finalgrayim=finalgrayim.convert("L")
finalgrayim.show()
finalgrayim.save(r'c:\Users\rajes\Pythoncode\.vscode\finalgrayqstp.jpg')
