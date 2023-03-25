import os
import cv2
import numpy as np
from flask import Flask, flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename
from PIL import Image

app = Flask(__name__)

@app.route('/')
def upload_form():
    return render_template('upload.html')

@app.route('/', methods=['POST'])
def upload_image():
	# getting the selected image file which the user has uploaded
   image_file = request.files['file']

   # getting the degree which the user has entered in the input field
   degree = int(request.form['text'])

   # securing the image file
   filename = secure_filename(image_file.filename) # <-- this passes the name of the image file

   # saving the uploaded image file
   image_file.save(os.path.join('static/', 'filename'))

   # opening the image file
   image = Image.open(image_file)

   # rotating the image
   image_rotation_degree = image.rotate(degree)

   # saving the rotated image (we are naming it rotated_image)in the static folder
   image_rotation_degree.save(os.path.join('static', 'rotated_image.jpg'))

   # storing the rotated image in a variable
   img_rotate = 'rotated_image.jpg'

   # returning the rotated image
   return render_template('upload.html', filename=img_rotate)


@app.route('/display/<filename>')
def display_image(filename):
    return redirect(url_for('static', filename=filename))


if __name__ == "__main__":
    app.run()
