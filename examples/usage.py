from ayah_sender import AyahSender

ayahSender = AyahSender()
reciters_dict = ayahSender.reciter.show_reciters()

# Show Reciter's info
print(reciters_dict)

# Fetch a single ayah's audio
audio_data = ayahSender.get_single_ayah(1, 1, 1)

# Save the single ayah audio
ayahSender.save_audio(audio_data, output_dir='..')

# Merge multiple ayahs' audio
merged_audio_data = ayahSender.merge_ayahs(5, 1, 1, 5)

# Save the merged audio file
ayahSender.save_audio(merged_audio_data, output_dir='..')

# Getting png image of an ayah
ayahSender.get_image(chapter_num=2, verse_num=255, output_dir='ayah-png')
