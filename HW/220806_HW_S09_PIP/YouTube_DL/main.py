# coding: utf8
from pyrogram.handlers import MessageHandler
import time
from pyrogram import Client, filters
import logging
import requests
import download
import download_a
import random
import os
import validation

av = -1
logging.basicConfig(level=logging.INFO)
bot = Client(
    "ses1",
    api_id=348759,
    api_hash="5dc6f4b54b1985199b42a069a5745306",
    workers=5,
    bot_token="5594001840:AAGCWPqFiIxH1t3rsvylSw_LL6a6eL063Us",
)


@bot.on_message(filters.command("start", ["!", "/"]))
def connect(chat, m):
    try:
        userID = m.chat.id
        bot.send_message(
            userID, "Привет! Я умею скачивать /1 -АУДИО /2- ВИДЕО из YouTube."
        )
    except Exception as e:
        print(e)


@bot.on_message(filters.command("1", ["!", "/"]))
def connect1(chat, m):
    global av
    av = 1
    bot.send_message(
        m.chat.id,
        "Отправь мне ссылку на ВИДЕО — а я отправлю тебе скачанное АУДИО.")


@bot.on_message(filters.command("2", ["!", "/"]))
def connect2(chat, m):
    global av
    av = 2
    bot.send_message(
        m.chat.id,
        "Отправь мне ссылку на ВИДЕО — а я отправлю тебе скачанное ВИДЕО.")


@bot.on_message(filters.text)
def get(chat, m):
    global av
    url = m.text
    userID = m.chat.id
    if av != -1:
        try:
            VID_ID = ""
            VID_ID = validation.to_valid(
                url, VID_ID
            )  # валидация регуляркой из validation.py
            if av == 1:
                av = -1
                bot.send_message(m.chat.id, "Начинаем загрузку аудио...")
                download_a.worker(VID_ID)  # скачивание аудио
                bot.send_message(m.chat.id, "Аудио " + str(VID_ID) + ".mp3 загружено!")
                bot.send_video(
                    m.chat.id, str(VID_ID) + ".mp3"
                )  # отправляем аудио в чат
                # os.remove(VID_ID + ".mp3")  # удаляем аудио на диске
            elif av == 2:
                av = -1
                bot.send_message(m.chat.id, "Начинаем загрузку видео...")
                download.worker(VID_ID)  # скачивание видео
                bot.send_message(m.chat.id, "Видео " + str(VID_ID) + ".mp4 загружено!")
                bot.send_video(
                    m.chat.id, str(VID_ID) + ".mp4"
                )  # отправляем видео в чат
                os.remove(VID_ID + ".mp4")  # удаляем видео на диске
            else:
                bot.send_message("Напиши:\n/1 - скачать аудио\n2 - скачать видео")
        except Exception as e:
            bot.send_message(m.chat.id, f"Что-то пошло не так! Ошибка `{e}`")
    else:
        bot.send_message("Напиши:\n/1 - скачать аудио\n2 - скачать видео")


bot.run()
