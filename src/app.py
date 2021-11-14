from flask import Flask, flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename
import os
import img_compress

app = Flask(__name__)

# directory untuk menyimpan gambar yang diupload melalui web
UPLOAD_FOLDER = 'static/uploads/'

app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# ekstensi file yang valid
IMG_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif', 'bmp', 'tif', 'tiff'])
 
def allowed_extension(filename):
# mengecek ekstensi file yang valid
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in IMG_EXTENSIONS

# render web.html ke browser
@app.route('/')
def home():
    return render_template('web.html')

# fungsi untuk mengolah input form
@app.route('/', methods=['POST'])
def form():
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)
    file = request.files['file']
    if file and allowed_extension(file.filename):
        filename = secure_filename(file.filename)
        quality = request.form.get('quality')
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        # proses kompresi gambar
        init_size, comp_size, percentage, time, c_img = img_compress.main(filename, int(quality))
        c_img_filename = "compressed"+filename
        c_img.save(os.path.join(app.config['UPLOAD_FOLDER'], c_img_filename))
        return render_template('web.html', filename=filename, quality=quality, init_size=init_size, comp_size=comp_size, percentage=percentage, time=time, c_img_filename=c_img_filename)
    else:
        flash('Allowed file type is image')
        return redirect(request.url)
 
# menampilkan gambar before and after ke web
@app.route('/display/<filename>')
def display(filename):
    return redirect(url_for('static', filename='uploads/' + filename))
 
if __name__ == "__main__":
    app.run(debug=True)