import os
import shutil
from os.path import join
from typing import List

from fastapi import UploadFile

from ..core.config import *


def save_uploaded_images(images: List[UploadFile]) -> str:
	print('removing all the previous uploaded files from the image folder')
	os.system(f'rm -rf {IMAGE_FOLDER}/*')
	os.system(f'rm -rf {os.path.join(PRED_IMAGES_FOLDER,"*")}')
	os.system(f'rm -rf {os.path.join(PRED_CAGE_FOLDER,"*")}')
	os.system(f'rm -rf {os.path.join(PRED_TXT_FOLDER,"*")}')
	print(f'Saving {len(images)} to location: {IMAGE_FOLDER}')
	for image in images:
		location = join(IMAGE_FOLDER, f'{image.filename}')
		with open(location, 'wb') as f:
			shutil.copyfileobj(image.file, f)
	return IMAGE_FOLDER