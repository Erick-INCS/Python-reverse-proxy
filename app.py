from flask import Flask, request, Response
import requests

app = Flask(__name__)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    query = request.query_string
    url = 'http://localhost/' + path

    if query:
        url += f'?{query.decode("utf-8")}'

    print('redirect to', url)
    req = requests.get(url)

    response = Response(req.content.replace(b'https://201.151.252.116:9105', b'http://192.168.1.199:5000'))
    response.headers['Content-Type'] = req.headers['Content-Type']

    return response

if __name__ == '__main__':
    app.run()
