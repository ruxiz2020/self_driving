from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
import os
import pandas as pd
from datetime import date
import speech_recognition as sr
from text_2_sound import text_2_sound
from audio_2_text import audio_2_text






def record_single_memo(idx, text):

    print("Memo:" + text)

    text_2_sound("Memo number " + str(int(idx)) + " is: " + text)
    status = False

    return idx, text, status



def record_daily_memo():

    text_2_sound("Hi dear, let us record the list of tasks for today!")

    list_memo = []
    for idx in range(5):

        text_2_sound("What is memo number " + str(int(idx)) + " for today?")

        memo_dict = {}

        listener = sr.Recognizer()
        # Following two lines are meant to fix error about ALSA
        listener.energy_threshold = 384
        listener.dynamic_energy_threshold = True

        memo = None
        while memo == None:
            memo = audio_2_text(listener)

        idx, text, status = record_single_memo(idx, memo)
        memo_dict['idx'] = idx
        memo_dict['task'] = text
        memo_dict['status'] = status
        list_memo.append(memo_dict)

    df_memo = pd.DataFrame(list_memo)

    today = date.today().strftime('%Y-%m-%d')
    df_memo.to_csv('memo'+ today + ".csv", index=False)


def update_daily_memo():

    today = date.today().strftime('%Y-%m-%d')
    df_memo = pd.read_csv('memo'+ today + ".csv")
    print(df_memo)

    list_memo = []
    for index, row in df_memo.iterrows():

        if len(str(row)) != 0:

            memo_dict = {}

            text_2_sound("Did you finish memo number " + str(int(row['idx'])) + " " + row['task'] + " ?")

            listener = sr.Recognizer()
            # Following two lines are meant to fix error about ALSA
            listener.energy_threshold = 384
            listener.dynamic_energy_threshold = True

            status = None
            while status == None:
                status = audio_2_text(listener)
            print(status)
            memo_dict['idx'] = row['idx']
            memo_dict['task'] = row['task']
            memo_dict['status'] = status

            list_memo.append(memo_dict)
        else:
            pass

    df_memo = pd.DataFrame(list_memo)

    today = date.today().strftime('%Y-%m-%d')
    df_memo.to_csv('memo'+ today + ".csv", index=False)




if __name__=='__main__':

    #record_daily_memo()

    update_daily_memo()
