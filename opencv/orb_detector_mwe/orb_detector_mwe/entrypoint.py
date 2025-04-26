
import argparse
from rosbags.highlevel import AnyReader
from rosbags.typesys import Stores, get_typestore
from rosbags.image import message_to_cvimage
import cv2

from pathlib import Path

class OutputDirs:
    def __init__(self, root):
        self.root = root

    def write_img( self, subdir, msg, img ):

        outdir = self.root / subdir
        outdir.mkdir(parents=True, exist_ok=True)

        ts = int(msg.header.stamp.sec * 1e9 + msg.header.stamp.nanosec)
        outfile = outdir / f"img_{ts}.jpg"
        print(f"Writing to {outfile}")

        cv2.imwrite(outfile, img)


class OrbDetector:
    def __init__(self):
        # Defaults from documentation 
        # create (int nfeatures=500, float scaleFactor=1.2f, int nlevels=8, int edgeThreshold=31, int firstLevel=0, int WTA_K=2, ORB::ScoreType scoreType=ORB::HARRIS_SCORE, int patchSize=31, int fastThreshold=20)

        self.detector = cv2.ORB.create()

    def detectAndCompute(self, img):
        kp,desc = self.detector.detectAndCompute(img, mask=None)
        return OrbResult(kp,desc)


class OrbResult:
    def __init__(self, keypoints, descriptors):
        self.keypoints = keypoints
        self.descriptors = descriptors

    def nKeypoints(self):
        return len(self.keypoints)

    def draw(self,img):
        outimg = img.copy()

        for kp in self.keypoints:
            center = [int(x) for x in kp.pt]
            cv2.circle(outimg, center, int(kp.size), (0,255,0), 2 )

        return outimg


def main():
    parser = argparse.ArgumentParser(prog="orb_detect", description="Evaluates RB Detector")

    parser.add_argument("bagfiles", nargs="+", type=Path, help="Bagfile(s) to process")

    parser.add_argument("--topic", default="/left/image_raw", help="Image topic to process")
    parser.add_argument("--count", metavar="N", type=int, default=None, help="Stop after N frames")

    parser.add_argument("--output-dir","-o", default="output", type=Path, help="Directory for output")

    args = parser.parse_args()


    typestore = get_typestore(Stores.ROS2_HUMBLE)
    outdirs = OutputDirs(args.output_dir)

    orb_detector = OrbDetector()


    frame_count = 0
    with AnyReader(args.bagfiles, default_typestore=typestore) as reader:
        connections = [x for x in reader.connections if x.topic == args.topic]

        for connection, timestamp, rawdata in reader.messages(connections=connections):
            msg = reader.deserialize(rawdata, connection.msgtype)
            
            if "Image" not in connection.msgtype:
                continue

            frame_count+=1
            img = message_to_cvimage(msg, 'bgr8')
            outdirs.write_img("raw", msg, img)


            orb_result = orb_detector.detectAndCompute(img)

            print(f"Found {orb_result.nKeypoints()} keypoints")

            kp_img = orb_result.draw(img)

            outdirs.write_img("orb_kps", msg, kp_img)


            if args.count and frame_count >= args.count:
                break

    print(f"Processed {frame_count} frames")