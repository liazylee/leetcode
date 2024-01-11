"""
@author:liazylee
@license: Apache Licence
@time: 04/01/2024 19:22
@contact: li233111@gmail.com
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
              ┏┓      ┏┓
            ┏┛┻━━━┛┻┓
            ┃      ☃      ┃
            ┃  ┳┛  ┗┳  ┃
            ┃      ┻      ┃
            ┗━┓      ┏━┛
                ┃      ┗━━━┓
                ┃  神兽保佑    ┣┓
                ┃　永无BUG！   ┏┛
                ┗┓┓┏━┳┓┏┛
                  ┃┫┫  ┃┫┫
                  ┗┻┛  ┗┻┛
"""
import os
import sys
from typing import Optional  # noqa

from pytubefix import Playlist
from pytubefix import YouTube  # noqa


class YoutubeDownload:
    def __init__(self, url: str, playlist: bool = False):
        self.url = url
        if playlist:
            self.playlist = Playlist(self.url)
            self.videos = self.playlist.videos
            self.title = self.playlist.title
            self.video_urls = self.playlist.video_urls
        else:
            self.video = YouTube(self.url)
            self.title = self.video.title
            self.video_urls = [self.video.streams.get_highest_resolution().url]
            self.videos = [self.video]
        if not os.path.exists(os.path.join(os.path.expanduser('~'), 'Downloads/youtube')):
            os.mkdir(os.path.join(os.path.expanduser('~'), 'Downloads/youtube'))
        self.path = os.path.join(os.path.expanduser('~'), 'Downloads/youtube')

    def download_mp4(self, quality: Optional[str] = None):
        # quality
        if not quality:
            quality = '720p'
        for video in self.videos:
            video.streams.get_by_resolution(quality).download(self.path, timeout=3600, max_retries=3)
            video.captions.get_by_language_code('en').download(self.path, )

    def download_audio(self, quality: Optional[str] = None):
        # quality
        if not quality:
            quality = '320kbps'
        for video in self.videos:
            print(
                f'downloading {video.title}, the abr is {video.streams.get_audio_only().abr}, the bitrate is {video.streams.get_audio_only().bitrate}')
            video.streams.get_audio_only().download(self.path, timeout=3600, max_retries=3)


# Compare this snippet from editor/tools/youtube_download.py:

def print_help():
    help_message = """
    Usage: python youtube_download.py [options] <url> <mp3 or mp4>  <playlist>

    Options:
    -h, --help      Show this help message and exit
    <playlist>      Specify the playlist or not default is false
    
    <url>           Specify the url of the video or playlist
    <mp3 or mp4>    Specify the download type default is mp3
    """
    print(help_message)


if __name__ == '__main__':
    # Check if the user requested help
    if '-h' in sys.argv or '--help' in sys.argv:
        print_help()
        sys.exit(0)

    arsg = sys.argv
    if len(arsg) < 2:
        print('please input url')
        sys.exit(0)
    url = arsg[1]
    if len(arsg) > 2:
        type = arsg[2]
    else:
        type = 'mp3'
    if len(arsg) > 3:
        playlist = arsg[3]
    else:
        playlist = False
    print(arsg)
    youtube_download = YoutubeDownload(url, playlist)
    if type == 'mp3':
        youtube_download.download_audio()
    else:
        youtube_download.download_mp4()
