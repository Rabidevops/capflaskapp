from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <html>
    <head>
        <title>CAP CLOUD TECH</title>
        <style>
            body {
                margin: 0;
                padding: 0;
                font-family: Arial, sans-serif;
                background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
                color: white;
                text-align: center;
            }
            .container {
                margin-top: 15%;
            }
            h1 {
                font-size: 50px;
                color: #00e6e6;
            }
            p {
                font-size: 20px;
                margin-top: 20px;
            }
            .box {
                background: rgba(255,255,255,0.1);
                padding: 30px;
                border-radius: 10px;
                display: inline-block;
                box-shadow: 0 0 20px rgba(0,0,0,0.5);
            }
        </style>
    </head>
    <body>
        <div class="container">
            <div class="box">
                <h1>Welcome to CAP CLOUD TECH 🚀</h1>
                <p>DevSecOps | AWS | Real-Time Training</p>
                <p>Contact - 9676939870 for more details</p>
            </div>
        </div>
    </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
