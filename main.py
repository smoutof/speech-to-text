import functions
import os
import datetime, traceback
from sendemail import send_email
import config

INPUT_DIR = "input"
OUTPUT_DIR = "output"

def get_input_files(input_dir):
    file_list = []
    for file in os.listdir(input_dir):
        file_list.append((f"{input_dir}/{file}", f"{file[:-4]}"))
    
    return file_list

def create_dir(dir):
    try:
        os.makedirs(dir, exist_ok=False)
        print(f"Directory '{dir}' created successfully.")
    except Exception as e:
        print(f"Error creating directory '{dir}': {e}")

def log_error(exception, input_video_name, output_dir):
    file = f'{output_dir}/error_log.txt'
    with open(file, 'a') as f:
        f.write(f"Timestamp: {datetime.datetime.now().isoformat()}\n")
        f.write(f"An error occured while handling {input_video_name}: {str(exception)}\n\n") 
        f.write("Traceback:\n")
        traceback.print_exc(file=f)
        f.write("\n")

def run():
    video_names = ""
    videos = get_input_files(INPUT_DIR)
    model = config.model
    device = config.device
    compute_type = config.compute_type
    language = config.language

    for video in videos:
        video_file = video[0]
        video_name = video[1]
        output_dir = f"{OUTPUT_DIR}/{video_name}"
        create_dir(output_dir)

        video_names += f"{video_name}, "

        print("Extracting audio...")
        audio = functions.extract_audio(input_video=video_file, input_video_name=video_name, output_dir=output_dir)
        print("Audio exctracted.\n")
        print("Starting transcription...")
        segments = functions.transcribe(audio=audio, model=model, device=device, compute_type=compute_type, language=language)
        print("Transcription done.\n")
        print("Generating subtitle file...")
        srt = functions.generate_srt_file(segments=segments, input_video_name=video_name, output_dir=output_dir)
        print(f"Subtitle file generated at {srt}\n")
        print("Generating timecode file...")
        try:
            timecode = functions.generate_timecode_file(segments=segments, input_video=video_file, input_video_name=video_name, output_dir=output_dir)
            print(f"Timecode file generated at {timecode}\n")
        except Exception as e:
            print("Couldn't generate timecode file.")
            print(e)
            log_error(e, video_name, output_dir)
        print("Generating word file...")
        try:
            word = functions.generate_doc_file(segments=segments, input_video=video_file, input_video_name=video_name, output_dir=output_dir)
            print(f"Word file generated at {word}\n")
        except Exception as e:
            print("Couldn't generate word file.")
            print(e)
            log_error(e, video_name, output_dir)
            print("Generating word file without timecode...")
            try:
                word_no_timecode = functions.generate_doc_file_no_timecode(segments=segments, input_video_name=video_name, output_dir=output_dir)
                print(f"Word file without timecode generated at {word_no_timecode}\n")
            except Exception as exception:
                print("Couldn't generate word file without timecode.")
                print(exception)
                log_error(exception, video_name, output_dir)

    if config.GMAIL_SENDING == True:
        print("Sending email...")
        send_email("Transcription done!", f"Transcription for {video_names[:-2]} done at {datetime.datetime.now()}!\n\nThis message was sent with Python.")
        print("All done! :)")


run()