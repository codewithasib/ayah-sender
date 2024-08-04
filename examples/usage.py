from ayah_sender import AyahSender

ayah_sender = AyahSender()
reciters_dict = ayah_sender.reciter.show_reciters()

# Show Reciter's info
print(reciters_dict)

# Fetch a single ayah's audio
audio_data = ayah_sender.get_single_ayah(1, 1, 1)

# Save the single ayah audio
ayah_sender.save_audio(audio_data, output_dir='..')

# Merge multiple ayahs' audio
merged_audio_data = ayah_sender.merge_ayahs(5, 1, 1, 5)

# Save the merged audio file
ayah_sender.save_audio(merged_audio_data, output_dir='..')
