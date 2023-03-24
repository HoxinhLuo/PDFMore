# -*- coding: utf-8 -*-
import os
import glob
import platform
import subprocess
from shutil import rmtree, copy2
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile
from src.constants import APP_NAME, APP_VERSION

SYSTEM = platform.system()
ARCH = platform.architecture()[0][:2]

# C:\Users\E1388477\Envs\pack\Lib\site-packages\tkinterdnd2\tkdnd\win64
DND2_PYTHON = Path('C:/Users/E1388477/Envs/pack/Lib/site-packages/tkinterdnd2/tkdnd/win64/')
BUILD_DIR = Path('build')
DIST_DIR = Path('dist')
OUTPUT_DIR = DIST_DIR / f'{APP_NAME}'

RELEASE_DIR = Path('release') / APP_VERSION

ADD_DATA_PREFIX = '--add-data '


def get_data(data, dest='.', sep=';'):
    script = ''
    for src in data:
        dest = '\\'.join(src.split('\\')[1:-1])
        # tmp = ADD_DATA_PREFIX + src + f'{sep}' + dest + " "
        tmp = f'{ADD_DATA_PREFIX}{src}{sep}{dest} '
        script += tmp
    return script


def prepare_pyinstall():

    ICON = glob.glob('src\\icon\\*.ico')
    PNGS = glob.glob('src\\icon\\*.png') + glob.glob('src\\icon\\toolbar\\*.png')
    PYS = glob.glob("src\\*.py") + glob.glob("src\\*\\*.py")
    
    CMD = ['pyi-makespec ', '-D -w ', f'-i {ICON[0]} ', f'--name {APP_NAME} ', get_data(ICON, dest='icon'),
           get_data(PNGS, dest=''), ' '.join(PYS)]

    CMD = ''.join(CMD)
    return CMD


def run_pyinstaller():
    CMD = prepare_pyinstall()

    process = subprocess.run(CMD, shell=True)

    if process.returncode != 0:
        raise ChildProcessError('pyi-makespec execute failed.')

    CMD = "pyinstaller {}.spec".format(APP_NAME)
    process = subprocess.run(CMD, shell=True)

    if process.returncode != 0:
        raise ChildProcessError('Pyinstaller building failed.')

    # copy tkinterdnd2 tcl/dll/lib file to installed dir
    dnd_tcl = glob.glob(str(DND2_PYTHON / '*.tcl'))
    copy_x(dnd_tcl)
    dnd_lib = glob.glob(str(DND2_PYTHON / '*.lib'))
    copy_x(dnd_lib)
    dnd_dll = glob.glob(str(DND2_PYTHON / '*.dll'))
    copy_x(dnd_dll)

    os.remove("{}.spec".format(APP_NAME))
    if BUILD_DIR.exists():
        rmtree(BUILD_DIR.absolute())


def copy_x(src: list):
    for tcl in src:
        copy2(Path(tcl), OUTPUT_DIR / 'tk')


def create_portable():
    if not RELEASE_DIR.exists():
        RELEASE_DIR.mkdir(parents=RELEASE_DIR.parent)
    if BUILD_DIR.exists():
        rmtree(BUILD_DIR.absolute())

    portable_file = RELEASE_DIR / f'{APP_NAME}-{APP_VERSION}-Portable-{SYSTEM}-{ARCH}.zip'

    print('Creating portable package...')
    zf = ZipFile(portable_file, 'w', compression=ZIP_DEFLATED)
    src = str(OUTPUT_DIR.absolute())
    for dirpath, _, filenames in os.walk(src):
        fpath = dirpath.replace(src, '')
        fpath = fpath and fpath + os.sep or ''
        for filename in filenames:
            print(filename)
            zf.write(os.path.join(dirpath, filename), fpath+filename)
    zf.close()
    print('Creating portable package done.')
    if DIST_DIR.exists():
        rmtree(DIST_DIR.absolute())


# create_portable()
if __name__ == '__main__':
    run_pyinstaller()
    is_create_portable = input('Creating a portable installer?(yes/no):')
    if is_create_portable.upper() in ['Y', 'YES']:
        create_portable()
