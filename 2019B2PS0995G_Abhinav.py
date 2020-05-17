{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'numpy.ndarray'>\n",
      "(1000, 1000, 3)\n",
      "<class 'PIL.Image.Image'>\n",
      "RGB\n",
      "(1000, 1000)\n"
     ]
    }
   ],
   "source": [
    "from PIL import Image\n",
    "import numpy as np\n",
    "# load the image\n",
    "image = Image.open('kratos.jpg')\n",
    "# convert image to numpy array\n",
    "data = asarray(image)\n",
    "print(type(data))\n",
    "# summarize shape\n",
    "print(data.shape)\n",
    "\n",
    "# create Pillow image\n",
    "image2 = Image.fromarray(data)\n",
    "print(type(image2))\n",
    "\n",
    "# summarize image details\n",
    "print(image2.mode)\n",
    "print(image2.size)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [],
   "source": [
    "#inverse\n",
    "im = np.array(Image.open('kratos.jpg').resize((256, 256)))\n",
    "\n",
    "im_i = 255 - im\n",
    "\n",
    "Image.fromarray(im_i).save('kratos_inverse.jpg')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'numpy.ndarray'>\n"
     ]
    }
   ],
   "source": [
    "#greyscale\n",
    "im = np.array(Image.open('kratos.jpg').convert('L')) #you can pass multiple arguments in single line\n",
    "\n",
    "gr_im= Image.fromarray(im).save('gr_kratos.png')"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
