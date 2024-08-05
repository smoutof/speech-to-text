import subprocess
import re

def extract_time_code_and_framerate(file_path):
    result = subprocess.run(['ffmpeg', '-i', file_path], stderr=subprocess.PIPE, text=True)
    
    time_code_pattern = re.compile(r'timecode\s*:\s*(\d+:\d+:\d+:\d+)')
    time_code_match = time_code_pattern.search(result.stderr)
    
    if not time_code_match:
        raise ValueError("Time code not found in the video metadata")
    
    time_code = time_code_match.group(1)
    
    frame_rate_pattern = re.compile(r'(\d+(?:\.\d+)?)\s*fps')
    frame_rate_match = frame_rate_pattern.search(result.stderr)
    
    if not frame_rate_match:
        raise ValueError("Frame rate not found in the video metadata")
    
    frame_rate = float(frame_rate_match.group(1))
    
    return time_code, round(frame_rate)

def parse_time_code(time_code):
    pattern = re.compile(r'(\d+):(\d+):(\d+):(\d+)')
    match = pattern.match(time_code)
    
    if not match:
        raise ValueError("Invalid time code format")
    
    hours, minutes, seconds, frames = map(int, match.groups())
    return hours, minutes, seconds, frames

def time_code_to_seconds(hours, minutes, seconds, frames, frame_rate):
    total_seconds = hours * 3600 + minutes * 60 + seconds
    total_seconds += frames / frame_rate
    return total_seconds

def seconds_to_time_code(total_seconds, frame_rate):
    hours = int(total_seconds // 3600)
    total_seconds %= 3600
    minutes = int(total_seconds // 60)
    total_seconds %= 60
    seconds = int(total_seconds)
    frames = int((total_seconds - seconds) * frame_rate)
    
    return f"{hours:02}:{minutes:02}:{seconds:02}:{frames:02}"

def add_seconds_to_time_code(time_code, add_seconds, frame_rate):
    add_seconds = round(add_seconds, 1)
    
    hours, minutes, seconds, frames = parse_time_code(time_code)
    total_seconds = time_code_to_seconds(hours, minutes, seconds, frames, frame_rate) + add_seconds
    new_time_code = seconds_to_time_code(total_seconds, frame_rate)
    return new_time_code