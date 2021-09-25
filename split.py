import moviepy.editor as mp
import argparse

parser = argparse.ArgumentParser(description='split audio from video')
parser.add_argument('--video', default='tmp.mov', help='Path to video')
args = parser.parse_args()

my_clip = mp.VideoFileClip(r""+args.video)
my_clip.audio.write_audiofile(r"demo_audio.wav")
