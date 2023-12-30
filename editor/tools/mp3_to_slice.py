"""
@author:liazylee
@license: Apache Licence
@time: 30/12/2023 22:09
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
import subprocess
import sys


# transfer big mp3 file to small mp3 file


def slice_mp3_ffmpeg(input_file, silence_duration=2, output_format="mp3") -> None:
    # The command to use ffmpeg to split the audio file
    cmd = [
        'ffmpeg', '-i', input_file, '-af',
        f'silencedetect=noise=-30dB:d={silence_duration}', '-f', 'null', '-'
    ]
    print(f"Running command: {' '.join(cmd)}")
    result = subprocess.run(cmd, stderr=subprocess.PIPE)
    print(f"Result: {result}")

    timestamps = []
    filename = input_file.split('.')[0].split('/')[-1]
    print(f'filename: {filename}', f'result: {result.stderr}')
    # Parse the output to get the timestamps
    for line in result.stderr.decode('utf-8').split('\n'):
        if 'silence_start' in line:
            timestamps.append(line.split('silence_start: ')[1].split('.')[0])

    print(f"Found {len(timestamps)} timestamps: {timestamps}")
    if not os.path.exists(filename):
        os.mkdir(filename)
    with open(f"{filename}/{filename}.txt", 'w') as f:
        for i, timestamp in enumerate(timestamps):
            f.write(f"{i + 1}. {timestamp}\n")
    # Split the audio at the detected timestamps
    for i, timestamp in enumerate(timestamps):
        output_file = f"{filename}/{filename}_{i + 1}.{output_format}"
        cmd = [
            'ffmpeg', '-i', input_file, '-ss', str(timestamp),
            '-to', str(timestamps[i + 1]) if i + 1 < len(timestamps) else '',
            '-c', 'copy', output_file
        ]
        subprocess.run(cmd)
        print(f"Exported '{output_file}'")


if __name__ == '__main__':
    arsg = sys.argv
    if len(arsg) == 1:
        print('please input the mp3 file path')
        sys.exit(0)
    # arsg[2] and [3] is an optional parameter
    if len(arsg) == 2:
        slice_mp3_ffmpeg(arsg[1])
    elif len(arsg) == 3:
        slice_mp3_ffmpeg(arsg[1], arsg[2])
    elif len(arsg) == 4:
        slice_mp3_ffmpeg(arsg[1], arsg[2], arsg[3])
    else:
        print('please input the mp3 file path')
        sys.exit(0)
