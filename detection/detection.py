from imageai.Detection import ObjectDetection
import os, csv #com
import argparse
yolo = ObjectDetection()

def detection(path, model_path, len_):
    """
    path: path of your repository
    model_path: path to yolo weight
    len_: number of frame
    """
    out = open(path+"/det/det.txt","w")
    with out:
        writer = csv.writer(out)
        #MOT Challenge format
        #<frame_index>,<target_id>,<bbox_left>,<bbox_top>,<bbox_width>,<bbox_height>,<score>,<object_category>,<truncation>,<occlusion>
        for f in range(int(len_)):
            if f%10==0: print(str(f)+" / "+str(len_))
            input_path = path+"/img1/frame"+str(f)+".jpg"
            output_path = path+"/det/img1/"+str(f)+".jpg"

            yolo.setModelTypeAsTinyYOLOv3()
            yolo.setModelPath(model_path)
            yolo.loadModel()
            detection = yolo.detectObjectsFromImage(input_image=input_path, output_image_path=output_path, minimum_percentage_probability=15)

            for eachItem in detection:
                if(eachItem["name"]=="person"):
                    loc = eachItem["box_points"]
                    loc[2] = loc[2] - loc[0]
                    loc[3] = loc[3] - loc[1]
                    writer.writerow([f,-1]+loc+[eachItem["percentage_probability"]/100,-1,-1,-1])
        out.close()
        return

def parse_args():
    """Parse command line arguments.
    """
    parser = argparse.ArgumentParser(description="detection yolo v3 model")
    parser.add_argument(
        "--project_path",
        help="Path the repository.",
        required=True)
    parser.add_argument(
        "--video_name",
        help="name of your video",
        default="video",
        required=True)
    parser.add_argument(
        "--n_frame", help="number of frame in your video. Look more into your fps video and check the number of video that the decomposition frame by frame gave you",
        default=500)
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    print("Detection Start, it will be stored in /data/det/det.txt")
    detection(args.project_path +"/data/" + args.video_name, args.project_path +"/yolo-tiny.h5", args.n_frame)
