from imageai.Detection import ObjectDetection
import os, csv
yolo = ObjectDetection()

def detection(path, model_path, len_):
    out = open(path+"/post-detection/result_detection.txt","w")
    with out:
        writer = csv.writer(out)
        #MOT Challenge format
        #<frame_index>,<target_id>,<bbox_left>,<bbox_top>,<bbox_width>,<bbox_height>,<score>,<object_category>,<truncation>,<occlusion>
        for f in range(len_):
            if f%10==0: print(str(f)+" / "+str(len_))
            input_path = path+"/pre-detection/frame"+str(f)+".jpg"
            output_path = path+"/post-detection/frame"+str(f)+".jpg"

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

if __name__ == "__main__":
    pass
    #path = "cou"
    #if os.path.exists()
    #yolo("/resultat_detection")
