from ayah_sender import AyahSender

ayahSender = AyahSender()

# reciters = ayahSender.reciter.show_reciters()
# ayahSender.reciter.show_reciters()

audio = ayahSender.fetch_single_ayah(44, 1, 3)

print(type(audio))
ayahSender.save_audio()