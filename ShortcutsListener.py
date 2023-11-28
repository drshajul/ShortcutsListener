from flask import Flask, request
import os, pyperclip

app = Flask(__name__)
debug = False  # set to True to print debug messages

UPLOAD_FOLDER = os.path.join(os.path.expanduser('~'), 'Downloads')
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

def message(msg, code=200):
    if debug: print(msg)
    return msg, code

@app.route('/', methods=['POST'])
def upload_file():
    content_length = int(request.headers.get('Content-Length'))

    if 'clipboard' in request.headers:
        data = request.get_data().decode('utf-8')
        pyperclip.copy(data)
        print('Data copied to clipboard: ' + data)
        return message('Data copied to clipboard', 200)

    if 'filename' in request.headers:
        filename = request.headers.get('filename')
    
    # read the binary data from the request body
    binary_data = request.get_data()

    # check if the binary data length matches the content length
    if len(binary_data) != content_length:
        return message('Content length does not match the actual data length', 400)

    save_path = os.path.join(UPLOAD_FOLDER, filename)
    with open(save_path, 'wb') as f:
        f.write(binary_data)
    print('File saved: ' + filename)
    return 'File uploaded successfully', 200

if __name__ == '__main__':
    print('Saving to location: ' + UPLOAD_FOLDER)
    app.run(debug=debug, host='0.0.0.0', port=2560)  # Change the port number as needed
