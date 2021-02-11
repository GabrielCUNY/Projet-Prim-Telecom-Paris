# Projet-Prim-Telecom-Paris
Projet Prim Telecom Paris Tracking Football Player

The objective of this project is to use a football video to track the players and record their speed throughout the match in a JSON file.

## Installation
`git clone --recurse-submodules --remote-submodules`

# in the directory project 
`make install`

## Run the video test.
`make all`

## If you want your proper video

`make all_new video_path=YourVideoPATH n_frame=(The number of frames you want. Make sure your video is long enough.)`

## Generate a video with the last result 
`make video`

## Distance calculation is not yet implemented.