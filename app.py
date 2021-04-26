from flask import Flask, request
import storage
import requests
import json
app = Flask(__name__)


@app.route("/")
def index():
    test = request.args['url']
    res = json.loads(test)
    for url in res:
        blob_name = url.replace('/', '_')
        container_name = request.args['hashtag'].lower()
        response = requests.get(url, stream=True)
        if response.status_code == 200:
            response.raw.decode_content = True
            size = len(response.content)
            storage.genBlobContainer(container_name)
            storage.uploadBlob(container_name, blob_name, response.content)
            # del response
    return "<h1>size_pic_content = " + str(size) + " </h1>"
