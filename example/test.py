
import lintel
import time
import traceback
import numpy as np
from PIL import Image


filename = '1000016779.mp4'

start = time.perf_counter()
try:
    # new to get video frame num
    frame_count = lintel.frame_count(filename, timeout=1)
    frame_nums = list(range(0, frame_count, int(frame_count/5)))    
    result = lintel.loadvid_frame_nums(filename,
                                       frame_nums=frame_nums,
                                       resize=224, # add for resize video frame
                                       should_key=True, # add for video key frame
                                       timeout=1 # add for read video url timeout
                                       )
    decoded_frames, width, height = result

    decoded_frames = np.frombuffer(decoded_frames, dtype=np.uint8)
    decoded_frames = np.reshape(decoded_frames,
                                    newshape=(len(frame_nums), height, width, 3))
except Exception as err:
    traceback.print_exc()
end = time.perf_counter()
print('time: {}'.format(end - start))

for i in range(len(frame_nums)):
    frame = decoded_frames[i]
    Image.fromarray(frame).save('frame_idx_{}.jpeg'.format(frame_nums[i]))
