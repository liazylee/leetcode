"""
@author:liazylee
@license: Apache Licence
@time: 30/12/2023 13:59
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
import sys


# convert webm file to mp3 file

def convert_webm_to_mp3(input_webm: str, output_mp3: str):
    import moviepy.editor as mp
    # check the input webm file is audio or video
    if not input_webm.endswith('.webm'):
        print('input file is not webm file')
        sys.exit(0)
    try:
        clip = mp.VideoFileClip(input_webm)
        clip.audio.write_audiofile(output_mp3)
    except Exception as e:
        print('input file is not video file')
        clip = mp.AudioFileClip(input_webm)
        clip.write_audiofile(output_mp3)


def print_help():
    help_message = """
    Usage: python webm_to_mp3.py [options] <input> <output>

    Options:
    -h, --help      Show this help message and exit
    

    <input>         Specify the input file or data
    <output>        Specify the output file or data
    """
    print(help_message)


if __name__ == '__main__':
    # Check if the user requested help
    if '-h' in sys.argv or '--help' in sys.argv:
        print_help()
        sys.exit(0)

    arsg = sys.argv
    if len(arsg) < 3:
        print('please input webm file and output mp3 file')
        sys.exit(0)
    filename = arsg[1]
    output = arsg[2]
    print(arsg)
    print('input file is %s, output file is %s' % (filename, output))
    convert_webm_to_mp3('videoplayback.webm', 'music.mp3')
