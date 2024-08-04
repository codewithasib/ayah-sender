<p align="center">
  <img alt="" style="{max-height: 50px}" src="./img/ayah-sender-v0.1.6.png">
</p>

# AyahSender

AyahSender is a Python package that allows you to have `Quranic audio `and `images` easily.

## Features

- Fetch a single ayah audio.
- Merge multiple ayahs into a single audio file.
- Supports various reciters.
- Saves audio files in MP3 format.
- Save transparent .png file of an ayah

## Installation

Install the package via pip:

```bash
pip install ayah-sender
```

## Requirements

- `requests`
- `pydub`
- `ffmpeg` - PyDub requires `ffmpeg` to perform its operations. 

Follow the articles to install ffmpeg on your system if you don't have it installed.

- [Windows](https://www.geeksforgeeks.org/how-to-install-ffmpeg-on-windows/)
- [Linux](https://www.geeksforgeeks.org/how-to-install-ffmpeg-in-linux/)
- [MacOS](https://phoenixnap.com/kb/ffmpeg-mac)

## Usage

### Basic Usage

Here is an example of how to use AyahSender:

```python
from ayah_sender import AyahSender

ayahSender = AyahSender()

# Show available reciters
reciters_dict = ayahSender.reciter.show_reciters()
print(reciters_dict)

# Fetch a single ayah's audio
audio_data = ayahSender.get_single_ayah(reciter_id=1, chapter_num=1, verse_num=1)

# Save the single ayah audio
ayahSender.save_audio(audio_data, output_dir='.')

# Merge multiple ayahs' audio
merged_audio_data = ayahSender.merge_ayahs(reciter_id=5, chapter_num=1, start_verse=1, end_verse=5)

# Save the merged audio file
ayahSender.save_audio(merged_audio_data, output_dir='.')

# Getting png image of an ayah
ayahSender.get_image(chapter_num=2, verse_num=255, output_dir='ayah-png')
```

### Functions

#### `get_total_verses_in_chapter(chapter_number)`

- Fetches the total number of verses in a given chapter.

#### `get_single_ayah(reciter_id, chapter_num, verse_num)`

- Fetches a single ayah from a specified reciter, chapter, and verse.

#### `merge_ayahs(reciter_id, chapter_num, start_verse, end_verse)`

- Fetches and merges a range of ayahs from a specified reciter and chapter.

#### `save_audio(audio_data, output_dir=".")`

- Saves the audio data to the specified directory.

#### `get_image(chapter_num, verse_num, output_dir='.')`

- Fetches and saves png image of an ayah

## Reciters List

The `reciters.csv` file contains the list of reciters. The `Reciter` class reads this file to fetch reciter information.

## Example

See [examples](examples) folder for examples.

## Contributing

Feel free to submit issues or pull requests. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT License](LICENSE)

## Contact

For any queries, contact us at [dev.asib@proton.me](mailto:dev.asib@proton.me).

## Acknowledgement

- [**everyayah.com**](https://everyayah.com/)   - Jazahumullahu Khairan to them for the `audio files`.
- [**Quran.com**](https://quran.com/)  - Jazahumullahu Khairan to them for the `API`.



---

Enjoy using `AyahSender` for your Quranic audio needs!