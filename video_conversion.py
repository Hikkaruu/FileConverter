import os
from moviepy import VideoFileClip
from moviepy import vfx

def convert_video(args):
    if not args.output.endswith(f".{args.format}"):
        args.output = f"{os.path.splitext(args.output)[0]}.{args.format}"
    
    audio_codec = 'aac'
    
    # avi format special treatment
    if args.format == "avi":
        args.codec = "mpeg4"

    # webm format special treatment
    if args.format == "webm":
        args.codec = "libvpx"
        audio_codec='libvorbis'
        args.bitrate = "500K"

    try:
        video = VideoFileClip(args.input)
        
        # Crop video
        if args.cut_start or args.cut_end:
            start = args.cut_start if args.cut_start else 0
            end = args.cut_end if args.cut_end else video.duration
            video = video.subclipped(start, end)
        
        # Change tempo
        if args.tempo and args.tempo > 0:
            video = video.with_effects([vfx.MultiplySpeed(args.tempo)])
        
        # Change resolution
        if args.size:
            resolution = args.size.split("x")
            if len(resolution) != 2:
                raise Exception("Wrong resolution, format: heightxwidth")
            try:
                int(resolution[0]), int(resolution[1])
            except ValueError:
                print("Invalid resolution format. Both parts have to be natural numbers")
                return
            video = video.with_effects([vfx.Resize((resolution[1], resolution[0]))])
        
        # Change volume
        if not args.no_audio and args.volume != 1.0:
            video = video.with_volume_scaled(args.volume)
        
        # Extract audio from video
        if args.no_video:
            args.output = f"{os.path.splitext(args.output)[0]}.{'mp3'}"
            audio = video.audio
            audio.write_audiofile(
                args.output,
                codec='mp3',
                bitrate=args.bitrate,
                fps=args.sample_rate
            )
            return
        
        # Remove audio from video
        if args.no_audio:
            video = video.without_audio()
        
        # Create video
        if not args.no_video:
            video.write_videofile(
                args.output,
                codec=args.codec,
                bitrate=args.bitrate,
                fps=args.frame_rate,
                audio_codec= audio_codec if not args.no_audio else None,
                audio_bitrate=args.bitrate if not args.no_audio else None,
                threads=4
            )
        
        print(f"Video conversion completed: {args.input} -> {args.output}")
        
    except Exception as e:
        print(f"Video convertion failed: {str(e)}")
    finally:
        if 'video' in locals():
            video.close()