from image_conversion import convert_image
from audio_conversion import convert_audio
from video_conversion import convert_video
import argparse

parser = argparse.ArgumentParser(description="File conversion tool")

subparsers = parser.add_subparsers(dest='command')

# Image section
image_parser = subparsers.add_parser('image', help="Image conversion")
image_parser.add_argument('-i', '--input', type=str, required=True, help="input image path")
image_parser.add_argument('-o', '--output', type=str, required=True, help="output image path with desired format [PNG, JPEG, BMP, TIFF, WEBP, ICO]")
image_parser.add_argument('-wh', '--width', type=int, help="[Optional] width for resizing")
image_parser.add_argument('-ht', '--height', type=int, help="[Optional] height for resizing")
image_parser.add_argument('-r', '--rotate', type=int, help="[Optional] Rotation angle")
image_parser.add_argument('-q', '--quality', type=int, help="[Optional] Quality for JPEG/WebP (1-100)", 
                          choices=range(1, 101), default=95, metavar='QUALITY')
image_parser.add_argument('--remove-metadata', action='store_true', 
                          help="Remove metadata (EXIF, ICC profiles) from the output image")
image_parser.set_defaults(func=convert_image)

# Audio section
audio_parser = subparsers.add_parser('audio', help="Audio conversion")
audio_parser.add_argument('-i', '--input', type=str, required=True, help="Input audio path")
audio_parser.add_argument('-o', '--output', type=str, required=True, help="Output audio path")
audio_parser.add_argument('-f', '--format', type=str, choices=['mp3', 'wav', 'flac', 'ogg', 'aac'], 
                          default='mp3', help="Audio format to convert to")
audio_parser.add_argument('-br', "--bitrate", type=str, help="Bitrate", choices=['128k', '160k', '192k', '256k', '320k'], 
                    default="192k")
audio_parser.add_argument('-sr', '--sample-rate', type=int, help="Sample rate", choices=[44100, 48000], default=44100)
audio_parser.add_argument('-v', '--volume', type=float, help="Volume adjustment (e.g. 1.5 for 50%% louder)", default=1.0)
audio_parser.add_argument('-t', '--tempo', type=float, help="Tempo adjustment (e.g. 1.5 for 50%% faster)", default=1.0)
audio_parser.add_argument('-cs', '--cut-start', type=float, help="Trim video start")
audio_parser.add_argument('-ce', '--cut-end', type=float, help="Trim video end")
audio_parser.set_defaults(func=convert_audio)
    
# Video section

video_parser = subparsers.add_parser('video', help="Video conversion")
video_parser.add_argument('-i', '--input', type=str, required=True, help="Input video path")
video_parser.add_argument('-o', '--output', type=str, required=True, help="Output video path")
video_parser.add_argument('-f', '--format', type=str, 
                         choices=['mp4', 'avi', 'mov', 'mkv', 'flv', 'webm'], 
                         default='mp4', help="Video format to convert to")
video_parser.add_argument('-c', '--codec', type=str, 
                         choices=['h264', 'mpeg4', 'hevc', 'rawvideo', 'libvpx'], 
                         default='h264', help="Video codec")
video_parser.add_argument('-br', "--bitrate", type=str, 
                         help="Bitrate", choices=['500k', '1M', '2M', '5M', '10M'], 
                         default="2M")
video_parser.add_argument('-sr', '--sample-rate', type=int, 
                         help="Audio sample rate", choices=[44100, 48000], 
                         default=44100)
video_parser.add_argument('-fr', '--frame-rate', type=int, 
                         help="Frame rate", choices=[24, 30, 48, 60], 
                         default=30)
video_parser.add_argument('-s', '--size', type=str, 
                         help="Resolution (e.g. 1280x720)")
video_parser.add_argument('-v', '--volume', type=float, 
                         help="Volume adjustment (e.g. 1.5 for 50%% louder)", 
                         default=1.0)
video_parser.add_argument('-t', '--tempo', type=float, 
                         help="Tempo adjustment (e.g. 1.5 for 50%% faster)", 
                         default=1.0)
video_parser.add_argument('-cs', '--cut-start', type=float, 
                         help="Trim video start (seconds)")
video_parser.add_argument('-ce', '--cut-end', type=float, 
                         help="Trim video end (seconds)")
video_parser.add_argument('--no-audio', action='store_true', 
                         help="Remove audio from output")
video_parser.add_argument('--no-video', action='store_true', 
                         help="Remove video from output (extract audio only)")
video_parser.set_defaults(func=convert_video)

args = parser.parse_args()

if args.command:
    args.func(args)
else:
    print("you have to select 'image', 'audio' or 'video'")


