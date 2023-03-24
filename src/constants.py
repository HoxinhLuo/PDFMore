import gettext
import locale
import os
import sys
from pathlib import Path

import psutil

BASE_DIR = Path(__file__).absolute().parent
PHYSICAL_CPU_COUNT = psutil.cpu_count(logical=False)

EXEC_NAME = 'PDFMore'
APP_NAME = 'PDFMore'
APP_VERSION = '1.0.0-Release'
APP_URL = f'https://github.com/HoxinhLuo/{EXEC_NAME}'
APP_ICON = BASE_DIR / f'icon/{EXEC_NAME}32.png'
ABOUT_ICON = BASE_DIR / f'icon/{EXEC_NAME}.png'

if 'win' in sys.platform:
    os.environ['LANGUAGE'] = locale.getdefaultlocale()[0]
gettext.install(domain=APP_NAME.replace(' ', ''), localedir=str(BASE_DIR / 'locale'))

BYTE_UNIT = ('', 'K', 'M', 'G', 'T', 'P', 'E', 'Z', 'Y')

FILE_TYPES_PDF = (('PDF File', '*.pdf'),)
FILE_TYPES_TEXT = (('Text File', '*.txt'),)
FILE_TYPES_IMAGE = (
    ('Image File', '*.jpg;*.jpeg;*.png;*.gif;*.tif;*.tiff;*.bmp'),
    ('JPEG Image', '*.jpg;*.jpeg'),
    ('PNG Image', '*.png'),
    ('GIF Image', '*.gif'),
    ('TIFF Image', '*.tif;*.tiff'),
    ('BMP Image', '*.bmp')
)

FILE_TYPES_EXCEL = (
    ('Xlsx File', '*.xlsx;*.xls'),
)

TOOLBAR_BUTTON = [
    BASE_DIR / 'icon/toolbar/merge.png',
    BASE_DIR / 'icon/toolbar/split.png',
    BASE_DIR / 'icon/toolbar/rotate.png',
    BASE_DIR / 'icon/toolbar/compress.png',
    BASE_DIR / 'icon/toolbar/extractimage.png',
    BASE_DIR / 'icon/toolbar/extracttext.png',
    BASE_DIR / 'icon/toolbar/pdf2image.png',
    BASE_DIR / 'icon/toolbar/image2pdf.png',
    BASE_DIR / 'icon/toolbar/pdf2excel.png',
    BASE_DIR / 'icon/toolbar/pdf2docx.png',
]
