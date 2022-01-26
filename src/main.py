from flask import Flask, jsonify, request
import time

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def styling():
    if request.method == 'POST':
        # id = request.form['id']
        # styling_text = request.form['styling_text']
        # img_bytes = file.read()
        id = 1643228220
        styling_text = 'hi-fade style'

        try:
            time.sleep(2)
            result_s3_base_url = 'https://bidi-ai.s3.ap-northeast-2.amazonaws.com/ai/results/1643228220/'
            return jsonify({'status': "success", 's3_base_url': result_s3_base_url})
        except:
            return jsonify({'status': "error"})
    else:
        time.sleep(2)
        result_s3_base_url = 'https://bidi-ai.s3.ap-northeast-2.amazonaws.com/ai/results/1643228220/'
        return jsonify({'status': "success", 'msg': result_s3_base_url})

if __name__ == '__main__':
    app.run(debug=True)