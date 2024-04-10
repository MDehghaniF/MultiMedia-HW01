#Source from GPT bot

# import the opencv library 
import cv2       
  
# define a Webcam stream as a video capture object 
NewStream = cv2.VideoCapture(0) 

#Error handling of webcam connection
if not NewStream.isOpened():
    print("Cannot open camera")
    exit()


# Define the codec and create VideoWriter object
record_Mode = True
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('Captured_video/output.avi', fourcc, 20.0, (640,  480))

while(True): 
      
    # Capture the video frame 
    # by frame 
    ret, frame = NewStream.read() 

    # Display the resulting frame 
    if record_Mode == True :
        out.write(frame)
        cv2.imshow('Recording', frame)
    else :
        cv2.imshow('webcam', frame)  

    # the 'q' button is set as the 
    # quitting button you may use any 
    # desired button of your choice 
    if cv2.waitKey(1) & 0xFF == ord('q'): 
        break
  
# After the loop release the cap object 
NewStream.release() 
out.release()
# Destroy all the windows 
cv2.destroyAllWindows() 


# class VideoRecorder:
#     def __init__(self):
#         self.open = True
#         self.device_index = 0
#         self.fps = 6
#         self.fourcc = "MJPG"
#         self.frameSize = (640, 480)  # Adjust video format and size as needed

#     def record_video(self):
#         #cap = cv2.VideoCapture(self.device_index)
#         out = cv2.VideoWriter("output.avi", cv2.VideoWriter_fourcc(*self.fourcc), self.fps, self.frameSize)

#         while self.open:
#             ret, frame = cap.read()
#             if ret:
#                 out.write(frame)
#                 # Display the video on the screen (optional)
#                 cv2.imshow("Recording", frame)
#                 if cv2.waitKey(1) & 0xFF == ord("q"):
#                     break

#         cap.release()
#         out.release()
#         cv2.destroyAllWindows()

# # Usage:
# recorder = VideoRecorder()
# recorder.record_video()