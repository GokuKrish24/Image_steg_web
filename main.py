from flask import Flask,flash,render_template,request,redirect
from werkzeug.utils import secure_filename
import os

UPLOAD_FOLDER = 'static/uploads/'
# ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
ALLOWED_EXTENSIONS = {'png'}

app = Flask(__name__)
app.secret_key="image_stego_awsm"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/")
@app.route("/home")
def Image_steg():
    return render_template('home.html')

@app.route('/',methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        flash('No file part')
        return redirect('/home')
    file = request.files['file']
    
    if file.filename == '':
        flash('No selected file')
        return redirect('/home')
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        # return redirect('/home')
        return "Image uploaded successfully"
    else:
        flash("Allowed image type is png only!!")
        return redirect('/home')

app.run(debug=True)
