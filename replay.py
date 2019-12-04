import os
import shutil
import sys

# run replay.py input_dir output_dir
# args is a list contains [pyfile, input dir, output dir]
# e.g. [replay.py, ./json_data/, ./clips/]
# most codes borrow from Dana'script

args=sys.argv
json_dir_name = args[1] # input directory
video_dir_name = args[2]  # output directory
tmp_img_dir_name = 'data/tmp_imgs/' # DO NOT CHANGE

# create video_dir if it does not exist
if not os.path.isdir(video_dir_name):
	os.mkdir(video_dir_name)

json_dir = os.listdir(json_dir_name)
json_dir.sort()
if os.path.isdir(tmp_img_dir_name):
	shutil.rmtree(tmp_img_dir_name)

for json_file in json_dir:
	if json_file[-5:] != '.json':
		continue
	print(json_file)
	print('please waiting, it keeps less than 1min to generate one video... \n\n')

	# 1. Generate tmp PNGs
	os.mkdir(tmp_img_dir_name)
	os.system('./bin/replay %s %s' % (os.path.join(json_dir_name, json_file), tmp_img_dir_name))
	
	# 2. Generate MP4 from tmp PNGs
	os.system('ffmpeg -framerate 30 -i ' + tmp_img_dir_name + '%04d.png ' + os.path.join(video_dir_name, json_file.replace('.json', '.mp4')))
	
	# 3. Remove tmp PNGs
	shutil.rmtree(tmp_img_dir_name)
	print('success!\n')
