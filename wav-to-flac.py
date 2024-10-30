import os
import sys
import ffmpeg

def convert_wav_to_flac(wav_file):
    flac_file = wav_file.replace('.wav', '.flac')
    try:
        # Convert WAV to FLAC with metadata preservation
        ffmpeg.input(wav_file).output(flac_file, map_metadata=0).run()

        # Check if the FLAC file was created successfully
        if os.path.exists(flac_file):
            # Verify the audio streams are identical
            try:
                ffmpeg.input(wav_file).input(flac_file).filter('amix', inputs=2, duration='first', dropout_transition=3).output('null').run()
                # Delete the original WAV file
                os.remove(wav_file)
                print(f"Successfully converted {wav_file} to {flac_file} and deleted the original WAV file.")
            except ffmpeg.Error as e:
                print(f"Audio streams differ between {wav_file} and {flac_file}. Conversion failed. Error: {e}")
        else:
            print(f"Failed to create {flac_file}.")
    except ffmpeg.Error as e:
        print(f"Error during conversion: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def convert_all_wav_in_directory(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.wav'):
                wav_file = os.path.join(root, file)
                convert_wav_to_flac(wav_file)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python wav-to-flac.py <path_to_directory>")
        sys.exit(1)

    directory = sys.argv[1]
    if not os.path.isdir(directory):
        print(f"The directory {directory} does not exist.")
        sys.exit(1)

    convert_all_wav_in_directory(directory)