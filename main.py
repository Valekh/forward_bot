import requests

from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from bot_vk import longpoll

import bot_vk
from telegram import admin


def get_the_photo(sizes):

    for x in ["w", "z", "y"]:
        for i in sizes:
            if i['type'] == x:
                return i['url']

    index = len(sizes) - 1
    return sizes[index]['url']


def get_the_post(post, title):
    if title != '':
        text = title + "\n—————\n\n" + post['text']
    else:
        text = post['text']

    if 'attachments' in post:
        attachments = post['attachments']
        photos = []
        for i in attachments:
            if 'photo' in i:
                photos.append(get_the_photo(i['photo']['sizes']))
            elif i['type'] == 'poll':
                post_link = "http://vk.com/wall" + bot_vk.group_id + "_" + str(post['id'])
                text = text + "\n\nПринять участие в опросе:\n" + post_link
            elif (i['type'] == 'link') and ('vk.com/@' in i['link']['url']):
                post_link = "http://vk.com/wall" + bot_vk.group_id + "_" + str(post['id'])
                text = text + "\n\nСсылка на статью:\n" + post_link

        if len(photos) > 0:
            admin.send_media_group(photos, text)
        elif text != '':
            admin.new_post(text)

    elif text != '':
        admin.new_post(text)


print('абобус (бот запущен)')
while True:
    try:
        for event in longpoll.listen():
            print(event)

            if event.type == VkBotEventType.MESSAGE_NEW:
                print(event.object.message['text'])

            elif (event.type == VkBotEventType.WALL_POST_NEW) and (event.object['post_type'] == 'post'):
                try:
                    if "copy_history" in event.object:

                        get_the_post(event.object.copy_history[0], event.object['text'])
                    else:
                        get_the_post(event.object, '')
                except Exception as error:
                    admin.report_about_error("ошибка!!!!!: " + str(error))
    except requests.exceptions.ReadTimeout:
        continue
