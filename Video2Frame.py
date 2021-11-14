import cv2

dir_video = 'Directory of your video'
dir_frames = 'Directory to save your video'
vidcap = cv2.VideoCapture(dir_video)
success,image = vidcap.read()

count = 0
success = True


while success:
    success, frame = vidcap.read()
    dir_frame = dir_frames + '/%d.jpg' % count
    cv2.imwrite(dir_frame,frame)

    if cv2.waitKey(100) == 30:
        break
    count += 1
