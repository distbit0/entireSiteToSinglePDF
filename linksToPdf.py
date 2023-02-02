import os
from flask import Flask, render_template
from multiprocessing import Process

app = Flask(__name__)

@app.route('/sitemap.xml')
def sitemap():
    urls = []
    with open('inputUrls.txt', 'r') as f:
        for line in f:
            urls.append(line.strip())
    return render_template('sitemap.xml', urls=urls)

if __name__ == '__main__':
    server = Process(target=app.run, kwargs={'port': 8972})
    server.start()
    print("Server is running on port 8972")
    os.system('./siteToPdf.sh http://localhost:8972/sitemap.xml')
