import time
from polly_tts_cli import text_to_speech

def test_region_speed(regions, text, voice_id="Nicole"):
    results = []
    for region in regions:
        start_time = time.time()
        audio_file = text_to_speech(text, voice_id=voice_id, region_name=region)
        end_time = time.time()
        
        if audio_file:
            duration = end_time - start_time
            results.append((region, duration))
        else:
            results.append((region, None))
    
    return results

def main():
    regions = ["us-east-1", "eu-west-1", "ap-southeast-2", "ap-southeast-1", "ap-east-1"]
    test_text = "This is a test of the AWS Polly text-to-speech service in different regions."
    
    print("Testing AWS Polly speed in different regions...")
    results = test_region_speed(regions, test_text)
    
    print("\nResults:")
    for region, duration in results:
        if duration is not None:
            print(f"{region}: {duration:.2f} seconds")
        else:
            print(f"{region}: Failed to generate speech")
    
    if results:
        fastest_region = min(results, key=lambda x: x[1] if x[1] is not None else float('inf'))
        print(f"\nFastest region: {fastest_region[0]} ({fastest_region[1]:.2f} seconds)")

if __name__ == "__main__":
    main()