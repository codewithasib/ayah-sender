import os
import requests
from pydub import AudioSegment
from io import BytesIO
from ayah_sender.reciter import Reciter


class AyahSender:
    BASE_URL = "https://everyayah.com/data"
    BASE_URL2 = "https://everyayah.com/data/images_png/"
    BASE_URL3 = "https://api.quran.com/api/v4/"

    def __init__(self):
        self.reciter = Reciter()

    def get_chapter_name(self, chapter_number):
        """
        This function is to get the name of a chapter.
        :param chapter_number:
        :return: chapter name
        """
        url = f"{self.BASE_URL3}chapters/{chapter_number}"
        response = requests.get(url)
        if response.status_code == 200:
            chapter_name = response.json()['chapter']['name_simple']
            return chapter_name
        else:
            return 0

    def get_total_verses_in_chapter(self, chapter_number):
        """
        This function is to get the total verses count in a chapter.
        :param chapter_number:
        :return: total_verses
        """
        url = f"{self.BASE_URL3}chapters/{chapter_number}"
        response = requests.get(url)

        if response.status_code == 200:
            total_verses = response.json()['chapter']['verses_count']
            return total_verses
        else:
            return 0

    def get_single_ayah(self, reciter_id, chapter_num, verse_num):
        """
        This function fetches a single ayah/verse from a chapter number.
        It takes the following parameters:
        :param reciter_id: Reciter ID
        :param chapter_num: Surah / Chapter number
        :param verse_num: The ayah/verse number
        And returns the following:
        :return: audio_data dict
        """
        verse_str = f"{verse_num:03d}"
        chapter_str = f"{chapter_num:03d}"
        reciter_name = self.reciter.get_reciter_name(reciter_id)
        chapter_name = self.get_chapter_name(chapter_num).replace("-", "_")

        url = f"{self.BASE_URL}/{reciter_name}/{chapter_str}{verse_str}.mp3"
        response = requests.get(url)

        if response.status_code == 200:
            total_verses = self.get_total_verses_in_chapter(chapter_num)
            print(f'Downloading file from {url}')
            if chapter_num <= 114:
                if verse_num <= total_verses:
                    audio_segment = AudioSegment.from_file(BytesIO(response.content))
                    return {
                        "audio_segment": audio_segment,
                        "reciter_id": reciter_id,
                        "chapter_num": chapter_num,
                        "chapter_name": chapter_name,
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
        """
        This function fetches a range of ayahs/verses from a chapter.
        It takes the following parameters:
        :param reciter_id: Reciter ID
        :param chapter_num: Surah / Chapter number
        :param start_verse: First ayah of the range
        :param end_verse: Last ayah of the range
        And returns the following
        :return: audio_data dict
        """
        merged_audio = AudioSegment.silent(duration=0)

        chapter_name = self.get_chapter_name(chapter_num).replace("-", "_")

        for verse_num in range(start_verse, end_verse + 1):
            verse_data = self.get_single_ayah(reciter_id, chapter_num, verse_num)
            merged_audio += verse_data["audio_segment"]
        return {
            "audio_segment": merged_audio,
            "reciter_id": reciter_id,
            "chapter_num": chapter_num,
            "chapter_name": chapter_name,
            "start_verse": start_verse,
            "end_verse": end_verse
        }

    def save_audio(self, audio_data, output_dir="."):
        """
        This function saves the audio, whether it's a single ayah or multiple.
        It takes the audio_data dict and output_dir params.
        :param audio_data: Necessary info about the audio
        :param output_dir: The directory user wishes to save the audio file to. Default is the root directory.
        :return:
        """
        global file_name
        reciter_name = self.reciter.get_reciter_name(audio_data["reciter_id"])

        if audio_data['start_verse'] != audio_data['end_verse']:
            file_name = f"{reciter_name}_Surah_{audio_data['chapter_name']}({audio_data['chapter_num']})_Ayah{audio_data['start_verse']}-{audio_data['end_verse']}.mp3"
            print(f'Merging {file_name}')
        elif audio_data['start_verse'] == audio_data['end_verse']:
            file_name = f"{reciter_name}_Surah_{audio_data['chapter_name']}({audio_data['chapter_num']})_Ayah{audio_data['start_verse']}.mp3"

        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        output_file_path = f"{output_dir}/{file_name}"
        with open(output_file_path, 'wb') as output_file:
            audio_data["audio_segment"].export(output_file, format="mp3")
        print(f'{output_file_path} saved successfully!')

    def get_image(self, chapter_num: int, verse_num: int, output_dir='.'):
        """
        Fetches and saves png image of an ayah
        :param chapter_num:
        :param verse_num:
        :param output_dir:
        :return:
        """
        chapter_name = self.get_chapter_name(chapter_num).replace("-", "_")
        total_verses = self.get_total_verses_in_chapter(chapter_num)

        assert chapter_num <= 114, f'Chapter number \'{chapter_num}\' can\'t be greater than 114'
        assert verse_num <= total_verses, f'Verse number \'{verse_num}\' can\'t be greater than the total number of verses: \'{total_verses}\'. Chapter \'Surah_{chapter_name}({chapter_num})\' has a total of {total_verses} verses.'

        url = f'{self.BASE_URL2}{chapter_num}_{verse_num}.png'
        r = requests.get(url)

        try:
            if r.status_code == 200:
                if not os.path.exists(output_dir):
                    os.makedirs(output_dir)

                filename = f'Surah_{chapter_name}({chapter_num})_{verse_num}.png'
                print(f'Downloading {filename}...')

                filepath = os.path.join(output_dir, filename)
                with open(filepath, 'wb') as f:
                    f.write(r.content)
                print(f'{filepath} saved successfully!')
            else:
                print(f'Failed to download {chapter_num}_{verse_num}.png')
                print(f'Status code: {r.status_code}')
        except Exception as e:
            print(f"{e}")
