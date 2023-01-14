from flask import Flask, render_template,request
import spotifyNhook as snh
app = Flask('app')

@app.route('/',methods=["GET","POST"])
def hello_world():
    if request.method == 'POST':
        try:
            album_data = snh.get_album_info(request.form.get('link'))
            snh.send(album_data)
        except:pass
        return render_template("volver.html")
    else:
        return render_template("index.html")


app.run(host='0.0.0.0', port=8080)
