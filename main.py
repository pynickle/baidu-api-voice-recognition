import os

from src import cut_wav
from src import wav_to_pcm
from src import combine_txt
from src import baidu_request


DIR = [".\\video", ".\\output", ".\\text"]
for i in DIR:
    if not os.path.exists(i):
        os.mkdir(i)
    else:
        os.system("rmdir /S /Q " + i)
        os.mkdir(i)

cut_wav.main()
print("切割wav文件完成！即将进入wav转pcm！")
os.system("pause")
print("\n" * 10)

wav_to_pcm.main()
print("wav文件转换pcm完成！即将进入请求api！")
os.system("pause")
print("\n" * 10)

files_num = baidu_request.main()
print("识别并写入txt成功！即将进入合并！")
os.system("pause")
print("\n" * 10)

combine_txt.main(files_num)
print("合并txt成功！程序完成！")
os.system("pause")
