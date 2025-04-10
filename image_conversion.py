from PIL import Image
import os

def convert_image(args):
    output_message = ""
    output_format = os.path.splitext(args.output)[1].replace('.', '').upper()
    if output_format == "JPG":
        output_format = "JPEG"
    try:
        with Image.open(args.input) as img: 
            if img.mode == "RGBA" and output_format in ["JPEG", "BMP", "DIB"]:
                img = img.convert("RGB")
            
            if args.width or args.height:
                width = args.width if args.width else img.width
                height = args.height if args.height else img.height
                img = img.resize((width, height))
                output_message += f", size {width}x{height}"

            if args.rotate:
                img = img.rotate(args.rotate, expand=True)
                output_message += f", rotated by {args.rotate} degrees"

            save_params = {}
            if output_format in ["JPEG", "WEBP"] and args.quality:
                save_params['quality'] = args.quality
                output_message += f", quality {args.quality}"

            if args.remove_metadata:
                img.info.clear()
                output_message += ", metadata has been removed"

            img.save(args.output, format=output_format, **save_params)
            print(f"{args.input} has been converted to {args.output}" + output_message)
    
    except Exception as e:
        print(f"Conversion error: {e}")
        if e not in ["PNG", "JPEG", "BMP", "TIFF", "WEBP", "ICO"]:
            print("Supported formats: PNG, JPEG, BMP, TIFF, WEBP, ICO")