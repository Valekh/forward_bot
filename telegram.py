import telebot
from telebot import util
from telebot.types import InputMediaPhoto

bot = telebot.TeleBot('5876153082:AAGLWRIbjAlFTaFoOidMbTxb-nq8g8CcKDU')


class TelegramAdmin:
    def __init__(self):
        self.tg_channel = "@testovy_kanal123"

    def new_post(self, text):
        if len(text) > 4000:
            splitted_text = util.smart_split(text, chars_per_string=4000)
            for mini_text in splitted_text:
                bot.send_message(self.tg_channel, mini_text)
        else:
            bot.send_message(self.tg_channel, text)

    def post_and_photo(self, url, text):
        if len(text) > 1000:
            text = self.get_text_for_caption(text)
            bot.send_photo(self.tg_channel, url, caption=text[0])
            for mini_text in text[1:]:
                bot.send_message(self.tg_channel, mini_text)

        else:
            bot.send_photo(self.tg_channel, url, caption=text)

    def send_media_group(self, urls, text):
        if len(text) > 1000:
            text = self.get_text_for_caption(text)
            photos = self.pack_photos(urls, text[0])
            bot.send_media_group(self.tg_channel, photos)
            for mini_text in text[1:]:
                bot.send_message(self.tg_channel, mini_text)
        else:
            photos = self.pack_photos(urls, text)
            bot.send_media_group(self.tg_channel, photos)

    def pack_photos(self, urls, caption):
        photos = [InputMediaPhoto(urls[0], caption=caption)]
        for i in urls[1:]:
            photos.append(InputMediaPhoto(i))
        return photos

    def send_photo(self, url):
        bot.send_photo(self.tg_channel, url)

    def send_audio(self, url):
        bot.send_audio(self.tg_channel, url)

    def get_text_for_caption(self, text):
        splitted_text = util.smart_split(text, chars_per_string=900)
        result = [splitted_text[0]]
        #текст под фото

        text = " ".join(splitted_text[1:])
        splitted_text = util.smart_split(text, chars_per_string=4000)
        #оставшийся текст

        result = result + splitted_text
        return result

    def report_about_error(self, error):
        bot.send_message("870458957", error)


admin = TelegramAdmin()

# bot.infinity_polling()
