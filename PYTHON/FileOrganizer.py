import os
from pathlib import Path

DIRECTORIES = {
    "HTML" : [".html5", ".html", ".htm", ".xhtml"],
    "IMAGE" : [".jpeg", ".jpg", ".gif", ".bmp", ".png", ],
    "VIDEO" : [".flv", ".mp4", ".mov", ".webm", ".mpg", ".mpeg", ".3gp"],
    "DOCUMENTS" : [".epub", ".pages", ".docx", ".doc", ".xps", ],
    "ARCHIVE" : [".rz", ".rar", ".xar", ".tar", ".zip"],
    "AUDIO" : [".aac", ".mp3", ".wav"],
    "TEXT" : [".txt", ".in", ".out"],
    "PDF" : [".pdf"],
    "PYTHON" : [".py"],
    "JAVA" : [".java"],
    "SHELL" : [".sh"],
    "XML" : [".xml"],
    "EXE" : [".exe"]
}

FILE_FORMATS = {file_format : directory
                for directory, file_formats in DIRECTORIES.items()
                for file_format in file_formats}

def file_orgaize():
    for entry in os.scandir():
        if entry.is_dir():
            continue
        file_path = Path(entry)
        file_format = file_path.suffix.lower()
        if file_format in FILE_FORMATS:
            directory_path = Path(FILE_FORMATS[file_format])
            directory_path.mkdir(exist_ok=True)
            file_path.rename(directory_path.joinpath((file_path)))
        for dir in os.scandir():
            try:
                os.rmdir(dir)
            except:
                pass

if __name__ == "__main__":
    file_orgaize()
