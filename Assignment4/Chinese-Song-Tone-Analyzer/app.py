from flask import Flask, request, render_template
from google.cloud import translate
from google.oauth2 import service_account
from watson_developer_cloud import ToneAnalyzerV3
from watson_developer_cloud import WatsonApiException

app = Flask(__name__)


# input lyrics
@app.route('/')
def index():
    return render_template('input.html')


# help
@app.route('/help')
def help():
    return render_template('help.html')


# analyze result
@app.route('/result', methods=['GET', 'POST'])
def result():
    if request.method == 'POST':
        lyrics = request.form['lyrics']
        text = deal_with_lyrics(lyrics)
        document_tones, sentence_tones = tone_analyzer_api(text)
    return render_template('result.html', document_tones=document_tones, sentence_tones=sentence_tones)


# Google Translate API
def deal_with_lyrics(text):
    credentials = service_account.Credentials.from_service_account_file('gcp_certification.json')
    translate_client = translate.Client(credentials=credentials)
    translation = translate_client.translate(text, 'en')
    print(translation['translatedText'])
    return translation['translatedText']


# Tone Analyzer API
def tone_analyzer_api(text):
    tone_analyzer = ToneAnalyzerV3(
        version='2017-09-21',
        iam_apikey='NQ3FJIhxaF7zet8o4SXXpZvFnVePls-pyj6kMugqj4Yb',
        url='https://gateway-wdc.watsonplatform.net/tone-analyzer/api'
    )
    try:
        tone_analysis = tone_analyzer.tone(text, 'text/html').get_result()
        for tone in tone_analysis['document_tone']['tones']:
            print(tone)
        # for sentence in tone_analysis['sentences_tone']:
        #     print(sentence)
        if 'sentences_tone' in tone_analysis:
            return tone_analysis['document_tone']['tones'], tone_analysis['sentences_tone']
        else:
            return tone_analysis['document_tone']['tones'], None
    except WatsonApiException as ex:
        print("Method failed with status code " + str(ex.code) + ": " + ex.message)


if __name__ == '__main__':
    app.run(debug=True)
