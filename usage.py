from ayah_sender import AyahSender
import json

ayah_sender = AyahSender()
reciters_dict = ayah_sender.reciter.show_reciters()

formatted_dict = json.dumps(reciters_dict, indent=4)
# print(formatted_dict)

# Fetch a single ayah's audio
audio_data = ayah_sender.fetch_single_ayah(1, 1, 1)

# Save the single ayah audio
output_file_path = ayah_sender.save_audio(audio_data, output_dir='.')
print(f"Audio saved at: {output_file_path}")

# Merge multiple ayahs' audio
merged_audio_data = ayah_sender.merge_ayahs(5, 1, 1, 5)

# Save the merged audio file
output_file_path = ayah_sender.save_audio(merged_audio_data, output_dir='.')
print(f"Audio saved at: {output_file_path}")
