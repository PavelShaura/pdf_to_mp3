from gtts import gTTS
from art import tprint
import pdfplumber
from pathlib import Path


def pdf_to_mp3(file_path="test.pdf", language="en"):
    if Path(file_path).suffix == ".pdf" and Path(file_path).is_file():

        print(f"[+] Файл оригинала: {Path(file_path).name}")
        print(f"[+] Обрабатываем....")

        with pdfplumber.PDF(open(file=file_path, mode="rb")) as pdf:
            pages = [page.extract_text() for page in pdf.pages]
        text = "".join(pages)
        #       with open("text1.txt", "w", encoding="utf-8") as file:
        #           file.write(text)
        text = text.replace("/n", "")
        #       with open("text2.txt", "w", encoding="utf-8") as file:
        #           file.write(text)
        my_audio = gTTS(text=text, lang=language, slow=False)
        file_name = Path(file_path).stem
        my_audio.save(f"{file_name}.mp3")

        return f"[+] {file_name}.mp3 успешно сохранен!\n ---Поздравляю!---"

    else:
        return "Файл не поддерживается, проверьте формат"


def main():
    tprint("PDF > TO > MP3", font="bulbhead")
    file_path = input("Укажите путь до файла...")
    #/Users/peer/PycharmProjects/home_work_11/home_work_11/PDF_to_mp3/pdf_files/kosmicheskoy-sfere.pdf
    language = input("Выберите язык: например 'en' или 'ru'")
    print(pdf_to_mp3(file_path=file_path, language=language))


if __name__ == "__main__":
    main()
