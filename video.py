from os import listdir
from os.path import isfile, join
import cv2

dest_folder = 'output_images'
video_image_files = [join(dest_folder, f) for f in listdir(dest_folder) if isfile(join(dest_folder, f))]

fourcc = cv2.VideoWriter_fourcc(*'DIVX')
out = cv2.VideoWriter('output.mp4',fourcc, 20.0, (640,480))

for i, file in enumerate(video_image_files[1:]):
    image = cv2.imread(file)
    cv2.imshow('image', image)
    cv2.waitKey(1)
    out.write(image)
	
out.release()