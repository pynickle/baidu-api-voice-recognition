import os

from aip import AipSpeech


def main():
    files = os.listdir(".\\output")
    files_num = len(files)

    APP_ID = '16799063'
    API_KEY = 'pKZkOBI1Fc4HnelKsNwWDv1y'
    SECRET_KEY = 'dYr6yk1ApFCOdO06zh6xnHiBtohREb4q'


    def get_file_content(filePath):
        with open(filePath, 'rb') as fp:
            return fp.read()


    client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)


    for i in files:
        print(".\\output\\" + i)
        result = client.asr(get_file_content(".\\output\\" + i), 'pcm', 16000, {
            'dev_pid': 1537,
        })
        print(result)
        if result["err_no"] == 0:
            with open(".\\text\\" + i[:-4] + ".txt", "a", encoding="utf-8") as f:
                f.write(result["result"][0])
        else:
            with open(".\\text\\" + i[:-4] + ".txt", "a", encoding="utf-8") as f:
                f.write(i[:-4] + "转换失败！")
    return files_num
