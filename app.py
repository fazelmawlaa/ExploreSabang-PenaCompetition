from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

# Route untuk halaman utama
@app.route('/')
def home():
    # Flask akan mencari 'web.html' di dalam folder 'templates'
    return render_template('web.html')

# (Opsional) Jika kamu memiliki file gambar/css/js statis lainnya
# Simpan di folder bernama 'static' dan akses via folder tersebut.

if __name__ == '__main__':
    # Host='0.0.0.0' membuat server bisa diakses dari IP publik VPS
    # Port 80 adalah port web standar (membutuhkan akses root/sudo)
    # Gunakan port lain (misal 5000) jika tidak memakai sudo
    app.run(host='0.0.0.0', port=80, debug=True)