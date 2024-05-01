# Session 6
Train and use a model using Docker.

## Installation
You should create a Dockerfile and build the image using `docker build`
 
## Running the project
Once the project is done, you can train it by running the command `docker run <IMAGE_NAME> train`, and predict with the command `docker run <IMAGE_NAME> predict <INPUT_FEATURES>`. Note that you will need to mount some volumes when using `docker run`, otherwise these commands won't work.

docker build -f Dockerfile -t ml0ps6image .

docker run -v C:\Users\34639\Desktop\postgrau\labs\projects\pr6/session-6/checkpoints:/checkpoints -v  C:\Users\34639\Desktop\postgrau\labs\projects\pr6/session-6/data:/data ml0ps6image train

docker run  -v C:\Users\34639\Desktop\postgrau\labs\projects\pr6/session-6/checkpoints:/checkpoints -v  C:\Users\34639\Desktop\postgrau\labs\projects\pr6/session-6/data:/data ml0ps6image predict 0.24522,0,9.9,0,0.544,5.782,71.7,4.0317,4,304,18.4,396.9,15.94
