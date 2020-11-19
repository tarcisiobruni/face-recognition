## install dlib requirements
sudo apt-get update
sudo apt-get install build-essential cmake
sudo apt-get install libopenblas-dev liblapack-dev 
# sudo apt-get install libx11-dev libgtk-3-dev
sudo apt-get install python python-dev python-pip
sudo apt-get install python3 python3-dev python3-pip

## install dlib
pip3 install dlib

## create enviroment variable context inside directory folder
python3 -m venv venv/

## activate virtual env
source venv/bin/activate

## install face recognition
pip3 install face_recognition