from googlesearch import search
import speech_recognition as sr
import requests
from bs4 import BeautifulSoup
from text_2_sound import text_2_sound
from audio_2_text import audio_2_text


class TextFromUrl:

    def __init__(self, url):
        """
        Extract text data from url
        """
        self._url = url

    def extract_text_from_html(self):

        response = requests.get(self._url)
        data = response.content.decode('utf-8', errors="replace")

        soup = BeautifulSoup(data, "lxml")
        page = soup.findAll('p')

        sentences = []
        for pp in page:

            text = pp.getText()
            if text.strip() != '':
                sentences.append(text + " ")
            # print(text)

        paragraph = ' '.join(sentences)
        return paragraph


def explain_2_me(keyword):

    urls = search(keyword)

    for url in urls:
        try:
            extractText = TextFromUrl(url)
            text = extractText.extract_text_from_html()

            if len(text) > 10:
                file = open("news.txt", "w")
                file.write(text)
                file.close() #This close() is important

                return
        except:
            pass


if __name__=='__main__':

    #keyword = 'covid right now'
    #explain_2_me(keyword)

    for i in range(2):

        listener = sr.Recognizer()
        # Following two lines are meant to fix error about ALSA
        listener.energy_threshold = 384
        listener.dynamic_energy_threshold = True

        keyword = None
        while keyword == None:
            keyword = audio_2_text(listener)

        explain_2_me(keyword)

        with open('news.txt', 'r') as file:
            data = file.read().replace('\n', ' ')
        print(data)

        text_2_sound(data[:2000])
