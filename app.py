from flask import Flask, flash, render_template, request, redirect, send_file
from werkzeug.utils import secure_filename
import os, shutil
from revealMessage import deform
from steg import perform
import string

def is_ascii(s):
    """Return True if string s is ASCII, False otherwise."""
    return all(c in string.printable for c in s)

UPLOAD_FOLDER = 'static/uploads/'
ALLOWED_EXTENSIONS = {'png'}

app = Flask(__name__)
app.secret_key = "image_stego_awsm"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/")
@app.route("/home")
def Image_steg():
    if os.path.isdir(UPLOAD_FOLDER):
        shutil.rmtree(UPLOAD_FOLDER)
    os.mkdir(UPLOAD_FOLDER)
    return render_template('home.html')

@app.route('/', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        flash('No file part')
        return redirect('/home')
    file = request.files['file']
    method = request.form['etype']
    key1 = request.form['key1']
    key2 = request.form['key2']
    if file.filename == '':
        flash('No selected file')
        return redirect('/home')
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        addr = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        
        # Save the file and ensure it's fully written
        file.save(addr)
        file.flush()
        os.fsync(file.fileno())

        if method == 'Encryption':
            msg = request.form['msg']
            try:
                perform(addr, msg, key1, key2)
                return send_file(addr, as_attachment=True)
            except Exception as e:
                flash(f"Error in encryption: {e}")
                return redirect('/home')

        elif method == 'Decryption':
            try:
                # Freshly load the image for each request to avoid state issues
                msg = deform(addr, key1, key2)
                count = 0
                while not is_ascii(msg) and count < 4:
                    # Log intermediate states for debugging
                    print(f"Decryption attempt {count+1}: {msg}")
                    msg = deform(addr, key1, key2)
                    count += 1
                flash(f"Decrypted Message: {msg}")
                return redirect('/home')
            except Exception as e:
                flash(f"Error in decryption: {e}")
                return redirect('/home')
    else:
        flash("Allowed image type is png only!!")
        return redirect('/home')

app.run(host='0.0.0.0',port=5000,debug=False)
