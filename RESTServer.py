import web
import pycld2
import json

urls = (
    '/', 'index'
)


"""
The class specified in the URL, it will get called when connecting to /
"""
class index:
    def GET(self):
        """
        Defines what happens when a GET request is sent. It is a language detection tool and tells the
        probability, reliability and language of a given text
        :return:
        """
        user_data = web.input(text="no data")
        isReliable, textBytesFound, details = pycld2.detect(user_data.text)
        return json.JSONEncoder().encode({'reliable': isReliable, 'language': details[0][0], 'prob': details[0][2]})


"""
starts the web server
"""
if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
