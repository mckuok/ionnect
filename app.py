from flask import Flask, render_template, request
from m2x.client import M2XClient
import json
import tempfile
import subprocess
from threading import Thread

app = Flask(__name__)

M2X_KEY = '<INSERT KEY HERE>'


@app.route("/")
def index():
    return render_template('index.html', devices=get_devices())


def threaded_function(file):
    subprocess.call("python3 " + file, shell=True)


@app.route("/api/code", methods=['POST'])
def execute_code():
    if request.method == 'POST':
        new_file, filename = tempfile.mkstemp()
        lines = ''
        with open('execution_wrapper.py', 'r') as template:
            for line in template:
                lines = lines + line

        code = ''
        for line in str(request.get_json()['code']).split('\n'):
            code = '  ' + str(line)

        lines = lines.replace('{% CODE %}', code)
        python_file = filename + '.py'
        with open(python_file, 'w+') as execute:
            execute.write(lines)
        thread = Thread(target=threaded_function, args=(str(python_file),))
        thread.start()

    return ''

def get_devices():
    client = M2XClient(key=M2X_KEY)
    page_of_devices = client.devices()
    number_of_pages = client.last_response.json['pages']

    devices = []

    for page in range(1, number_of_pages + 1):
        for device in page_of_devices:
            devices.append([device.name, json.dumps({'name': device.name, 'id': device.id})])
        next_page = page + 1
        page_of_devices = client.devices(page=next_page)
    return devices


if __name__ == "__main__":
    if M2X_KEY == '<INSERT KEY HERE>':
        print("You need to get an api key from AT&T m2x and place it to the M2X_KEY field")
    else:
        app.debug = True
        app.run()

