import requests
from pydub import AudioSegment
from io import BytesIO
from .reciter import Reciter


class AyahSender:
    BASE_URL = "https://everyayah.com/data"

    def __init__(self):
        self.reciter = Reciter()

    def get_total_verses_in_chapter(self, chapter_number):
        url = f"https://api.quran.com/api/v4/chapters/{chapter_number}"
        response = requests.get(url)
        if response.status_code == 200:
            total_verses = response.json()['chapter']['verses_count']
            return total_verses
        else:
            return 0

    def fetch_single_ayah(self, reciter_id, chapter_num, verse_num):
        verse_str = f"{verse_num:03d}"
        chapter_str = f"{chapter_num:03d}"
        reciter_name = self.reciter.get_reciter_name(reciter_id)
        url = f"{self.BASE_URL}/{reciter_name}/{chapter_str}{verse_str}.mp3"
        print(url)
        response = requests.get(url)
        if response.status_code == 200:
            total_verses = self.get_total_verses_in_chapter(chapter_num)
            if chapter_num <= 114:
                if verse_num <= total_verses:
                    audio_segment = AudioSegment.from_file(BytesIO(response.content))
                    return {
                        "audio_segment": audio_segment,
                        "reciter_id": reciter_id,
                        "chapter_num": chapter_num,
                        "start_verse": verse_num,
                        "end_verse": verse_num
                    }
                else:
                    raise Exception(f"Verse number cannot be greater than total_verses ({total_verses}) of a chapter.")
            else:
                raise Exception(f"Chapter number cannot be greater than 114.")
        else:
            raise Exception(f"Failed to establish a request to the server.\nCheck your internet connection and try "
                            f"again!")

    def merge_ayahs(self, reciter_id, chapter_num, start_verse, end_verse):
        merged_audio = AudioSegment.silent(duration=0)
        for verse_num in range(start_verse, end_verse + 1):
            verse_data = self.fetch_single_ayah(reciter_id, chapter_num, verse_num)
            merged_audio += verse_data["audio_segment"]
        return {
            "audio_segment": merged_audio,
            "reciter_id": reciter_id,
            "chapter_num": chapter_num,
            "start_verse": start_verse,
            "end_verse": end_verse
        }

    def save_audio(self, audio_data, output_dir="."):
        reciter_name = self.reciter.get_reciter_name(audio_data["reciter_id"])
        file_name = f"{reciter_name}_Surah{audio_data['chapter_num']}_Ayah{audio_data['start_verse']}-{audio_data['end_verse']}.mp3"
        output_file_path = f"{output_dir}/{file_name}"
        with open(output_file_path, 'wb') as output_file:
            audio_data["audio_segment"].export(output_file, format="mp3")
        return f'{output_file_path} saved successfully!'
