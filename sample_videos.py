import imageio
import numpy as np

VIDEO_DIR = './data/video'
SAMPLES_DIR = './data/samples'
FRAME_SPACING = 100

for vid_idx in range(700, 801):
    filename = '{}.mp4'.format(vid_idx)
    try:
      reader = imageio.get_reader('{}/{}'.format(VIDEO_DIR, filename))
      for idx in range(5000, reader.get_length(), FRAME_SPACING):
          print(idx)
          imageio.imwrite('{}/{}.png'.format(SAMPLES_DIR, filename[:3] + str(idx)), reader.get_data(idx))
    except Exception as e:
        print('Warning: {}'.format(e))
