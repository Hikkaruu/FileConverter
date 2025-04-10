import ffmpeg
import os

def convert_audio(args):
    if not args.output.endswith(f".{args.format}"):
        args.output = f"{os.path.splitext(args.output)[0]}.{args.format}"

    stream = ffmpeg.input(args.input)
    if hasattr(args, 'volume') and args.volume != '1.0':
        stream = stream.filter('volume', args.volume)

    if hasattr(args, 'tempo') and args.tempo != '1.0':
        stream = stream.filter('atempo', args.tempo)
    
    if hasattr(args, 'start') and hasattr(args, 'end'):
        stream = stream.filter('atrim', start=args.start, end=args.end)

    try:
        stream.output(args.output, 
                      format=args.format, 
                      audio_bitrate=args.bitrate,
                      ar=args.sample_rate,
                      ).run()

        print(f'Audio convertion completed: {args.output}')
    except ffmpeg.Error as e:
        print('Audio convertion failed: ', e)
