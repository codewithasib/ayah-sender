# AyahSender

AyahSender is a Python package that allows you to fetch and merge audio of Quranic verses (ayahs) from various reciters. You can save these audio clips to your local directory for easy access and listening.

## Features

- Fetch a single ayah audio.
- Merge multiple ayahs into a single audio file.
- Supports various reciters.
- Saves audio files in MP3 format.

## Installation

Install the package via pip:

```bash
pip install ayah_sender
```

## Usage

### Basic Usage

Here is an example of how to use AyahSender:

```python
from ayah_sender import AyahSender
import json

ayahSender = AyahSender()

# Show available reciters
reciters_dict = ayahSender.reciter.show_reciters()
print(reciters_dict)

# Fetch a single ayah's audio
audio_data = ayahSender.fetch_single_ayah(reciter_id=1, chapter_num=1, verse_num=1)

# Save the single ayah audio
output_file_path = ayahSender.save_audio(audio_data, output_dir='.')
print(f"Audio saved at: {output_file_path}")

# Merge multiple ayahs' audio
merged_audio_data = ayahSender.merge_ayahs(reciter_id=5, chapter_num=1, start_verse=1, end_verse=5)

# Save the merged audio file
output_file_path = ayahSender.save_audio(merged_audio_data, output_dir='.')
print(f"Audio saved at: {output_file_path}")
```

### Functions

#### `get_total_verses_in_chapter(chapter_number)`

Fetches the total number of verses in a given chapter.

#### `fetch_single_ayah(reciter_id, chapter_num, verse_num)`

Fetches a single ayah from a specified reciter, chapter, and verse.

#### `merge_ayahs(reciter_id, chapter_num, start_verse, end_verse)`

Fetches and merges a range of ayahs from a specified reciter and chapter.

#### `save_audio(audio_data, output_dir=".")`

Saves the audio data to the specified directory.

## File Structure

```
ayah-sender/
├── ayah_sender/
│   ├── __init__.py
│   ├── main.py
│   ├── reciter.py
│   ├── reciters.csv
├── setup.py
└── README.md
```

## Reciters List

The `reciters.csv` file contains the list of reciters. The `Reciter` class reads this file to fetch reciter information.

## Example

```python
from ayah_sender import AyahSender

ayahSender = AyahSender()
audio_data = ayahSender.fetch_single_ayah(reciter_id=1, chapter_num=1, verse_num=1)
ayahSender.save_audio(audio_data, output_dir='.')
```

## Contributing

Feel free to submit issues or pull requests. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT License](LICENSE)

## Contact

For any queries, contact us at [dev.asib@proton.me](mailto:dev.asib@proton.me).

---

Enjoy using AyahSender for your Quranic audio needs!