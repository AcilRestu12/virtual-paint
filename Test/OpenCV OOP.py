import cv2
class Camera():
    def __init__(self):
        self.cap = cv2.VideoCapture(0)  # Prepare the camera...
        print("Camera warming up ...")


    def get_frame(self):

        s, img = self.cap.read()
        if s:  # frame captures without errors...

            pass

        return img

    def release_camera(self):
        self.cap.release()


def main():
    while True:
        cam1 = Camera().get_frame()
        # frame = cv2.resize(cam1, (0, 0), fx = 0.75, fy = 0.75)
        cv2.imshow("Frame", cam1)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    Camera().release_camera()
    return ()

if __name__ == '__main__':
    main()
    cv2.destroyAllWindows()