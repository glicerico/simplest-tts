import time
import statistics
from polly_tts_cli import text_to_speech
from tqdm import tqdm

def test_region_speed(regions, text, voice_id="Nicole", num_runs=5):
    results = []
    for region in tqdm(regions, desc="Testing regions"):
        region_times = []
        for _ in range(num_runs):
            start_time = time.time()
            audio_file = text_to_speech(text, voice_id=voice_id, region_name=region)
            end_time = time.time()
            
            if audio_file:
                duration = end_time - start_time
                region_times.append(duration)
        
        if region_times:
            avg_duration = statistics.mean(region_times)
            results.append((region, avg_duration))
        else:
            results.append((region, None))
    
    return results

def main():
    regions = ["us-east-1", "eu-west-1", "ap-southeast-2", "ap-southeast-1", "ap-east-1"]
    test_text = "This is a test of the AWS Polly text-to-speech service in different regions."
    num_runs = 5
    
    print(f"Testing AWS Polly speed in different regions ({num_runs} runs per region)...")
    results = test_region_speed(regions, test_text, num_runs=num_runs)
    
    print("\nResults:")
    for region, avg_duration in results:
        if avg_duration is not None:
            print(f"{region}: {avg_duration:.2f} seconds")
        else:
            print(f"{region}: Failed to generate speech")
    
    if results:
        fastest_region = min(results, key=lambda x: x[1] if x[1] is not None else float('inf'))
        print(f"\nFastest region: {fastest_region[0]} ({fastest_region[1]:.2f} seconds)")

if __name__ == "__main__":
    main()