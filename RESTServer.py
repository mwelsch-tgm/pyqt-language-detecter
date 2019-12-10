import web
import pycld2
import json

urls = (
    '/', 'index'
)

class index:
    def GET(self):
        user_data = web.input(text="no data")
        isReliable, textBytesFound, details = pycld2.detect(user_data.text)
        return json.JSONEncoder().encode({'reliable':isReliable, 'language': details[0][0], 'prob':details[0][2]})

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()