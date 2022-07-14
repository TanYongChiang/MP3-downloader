#ask for the link from user
type_ = 2
# type:
#       1: singles
#       2: series

links = ["https://space.bilibili.com/3471379/channel/seriesdetail?sid=993998&ctype=0"]

import asyncio
from bilix import Downloader

async def single_vid(link):
    d = Downloader(video_concurrency=1)
    a = d.get_video(url=link,
                    quality=0,
                    only_audio=True)
    await asyncio.gather(a)
    await d.aclose()

async def series(link):
    d = Downloader(video_concurrency=1)
    a = d.get_collect_or_list(url=link,
                              quality=0,
                              only_audio=True)
    await asyncio.gather(a)
    await d.aclose()

if __name__ == '__main__':
    if type_ == 1:
        [asyncio.run(single_vid(link=link)) for link in links]
    elif type_ == 2:
        [asyncio.run(series(link=link)) for link in links]
    