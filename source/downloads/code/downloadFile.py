# -*- coding: utf-8 -*-
import aiohttp
import asyncio
import os
import shutil

audio_path = ''
final_audio = ''


# 合并多个音频文件
def merge_file():
    path = os.path.join(os.getcwd(), 'audio')
    audios = os.listdir(path)  # 得到文件夹下的所有文件名称
    global final_audio
    final_audio = open('final_audio.mp3', 'wb')
    for audioIdx in range(len(audios)):
        name = str(audioIdx) + '.mp3'
        print(audioIdx)
        audiocode = open(os.path.join(path, name), 'rb')
        final_audio.write(audiocode.read())
        audiocode.close()
    final_audio.flush()
    final_audio.close()


# 声明为异步函数
async def job(session, url, idx):
    # 获得名字
    # name = url.split('/')[-1]
    suffix = url.split('.')[-1]
    name = str(idx) + '.' + suffix
    # 触发到await就切换，等待get到数据
    audio = await session.get(url)
    # 读取内容
    audiocode = await audio.read()

    # 写入至文件
    with open(audio_path + "/" + str(name), 'wb') as f:
        f.write(audiocode)
        return str(url)


async def main(loop, fileurl):
    # 建立会话 session
    async with aiohttp.ClientSession() as session:
        # 建立所有任务
        tasks = [loop.create_task(job(session, fileurl[_], _)) for _ in range(len(fileurl))]
        print(len(fileurl))
        # 触发await，等待任务完成
        finished, unfinished = await asyncio.wait(tasks)
        # 获取所有结果
        # all_results = [r.result() for r in finished]
        # print("ALL RESULT:"+str(all_results))


def done_callback(futu):
    print('Done')
    merge_file()


def init():
    path = os.getcwd()  # 文件夹目录
    global audio_path
    audio_path = os.path.join(path, 'audio')

    # 如果目录存在，直接删除
    if os.path.exists(audio_path):
        shutil.rmtree(audio_path)

    os.mkdir(audio_path)

    url = [
        "https://delta-oss.ivykid.com/base/__k30ar459__mst1.mp3",
        "https://delta-oss.ivykid.com/base/__k30ar45t__mst2.mp3",
        "https://delta-oss.ivykid.com/base/__k30ar461__mst3.mp3",
        "https://delta-oss.ivykid.com/base/__k30ar4ue__mst4.mp3",
        "https://delta-oss.ivykid.com/base/__k30ar4ul__mst5.mp3",
        "https://delta-oss.ivykid.com/base/__k30arh7c__words.mp3",
        "https://delta-oss.ivykid.com/base/__k30armjy__1.1Y1.mp3",
        "https://delta-oss.ivykid.com/base/__k3132wap__2.1Y2%2520%25E5%25A4%258D%25E5%2588%25B6.mp3",
        "https://delta-oss.ivykid.com/base/__k31330ha__3.1Y3%2520%25E5%25A4%258D%25E5%2588%25B6.mp3",
        "https://delta-oss.ivykid.com/base/__k30atgfg__ok0.mp3",
        "https://delta-oss.ivykid.com/base/__k30atgfu__ok1.mp3",
        "https://delta-oss.ivykid.com/base/__k30atgym__ok2.mp3",
        "https://delta-oss.ivykid.com/base/__k30ath0v__ok3.mp3",
        "https://delta-oss.ivykid.com/base/__k30athla__ok4.mp3",
        "https://delta-oss.ivykid.com/base/__k30athnr__ok5.mp3",
        "https://delta-oss.ivykid.com/base/__k30athpi__ok6.mp3",
        "https://delta-oss.ivykid.com/base/__k30au5f0__take0.mp3",
        "https://delta-oss.ivykid.com/base/__k30au5fb__take1.mp3",
        "https://delta-oss.ivykid.com/base/__k30au5ku__take2.mp3",
        "https://delta-oss.ivykid.com/base/__k30au5lx__take3.mp3",
        "https://delta-oss.ivykid.com/base/__k30aui60__tree.mp3",
        "https://delta-oss.ivykid.com/base/__k30avcek__rp1.mp3",
        "https://delta-oss.ivykid.com/base/__k30avcev__rp2.mp3",
        "https://delta-oss.ivykid.com/base/__k30avckl__rp3.mp3",
        "https://delta-oss.ivykid.com/base/__k30avcss__rp4.mp3"]

    loop = asyncio.get_event_loop()
    futu = asyncio.ensure_future(main(loop, url))
    futu.add_done_callback(done_callback)
    # loop.run_until_complete(main(loop, url))
    loop.run_until_complete(futu)
    loop.close()


init()
