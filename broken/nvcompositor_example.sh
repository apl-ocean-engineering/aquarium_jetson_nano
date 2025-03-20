

gst-launch-1.0 nvcompositor \
     name=comp sink_0::xpos=1440 sink_0::ypos=0 sink_0::width=1440 \
     sink_0::height=1080 sink_1::width=1440 sink_1::height=1080 ! \
     'video/x-raw(memory:NVMM)' ! queue ! filesink location=test.mp4  \
     nvarguscamerasrc sensor-id=0 ! \
     'video/x-raw(memory:NVMM), width=(int)1440, height=(int)1080, \
     format=(string)NV12, framerate=30/1' ! comp. 
     
    #  \
    #  nvarguscamerasrc sensor-id=1 ! \
    #  'video/x-raw(memory:NVMM), width=(int)1440, height=(int)1080, \
    #  format=(string)NV12, framerate=30/1' ! comp. -e