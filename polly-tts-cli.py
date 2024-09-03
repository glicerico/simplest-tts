import boto3
import pygame
from tempfile import NamedTemporaryFile

def text_to_speech(text, voice_id="Nicole"):
    # Initialize the Polly client
    polly_client = boto3.client('polly', region_name='us-west-2')
    
    try:
        # Request speech synthesis
        response = polly_client.synthesize_speech(
            Text=text,
            OutputFormat='mp3',
            VoiceId=voice_id
        )
    except Exception as e:
        print(f"Error synthesizing speech: {str(e)}")
        return None

    # Save the audio stream to a temporary file
    if "AudioStream" in response:
        with NamedTemporaryFile(delete=False, suffix=".mp3") as temp_file:
            temp_file.write(response['AudioStream'].read())
            temp_file_path = temp_file.name
        return temp_file_path
    else:
        print("Could not find AudioStream in the response.")
        return None

def play_audio(file_path):
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

def main():
    print("Welcome to the AWS Polly CLI Interface!")
    print("Enter your text and press Enter to hear it spoken.")
    print("Press CTRL+C to exit.")

    try:
        while True:
            text = input("Enter text: ").strip()
            
            if text:
                audio_file = text_to_speech(text)
                
                if audio_file:
                    print(f"Playing audio for: {text}")
                    play_audio(audio_file)
                else:
                    print("Failed to generate speech.")
            else:
                print("Please enter some text.")
    except KeyboardInterrupt:
        print("\nExiting. Goodbye!")

if __name__ == "__main__":
    main()
