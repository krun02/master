1. clone this repo, using <git clone git@github.com:krun02/master.git > and cd to the folder Docker-image-build
2. docker-client should be running on your system to run docker commands,to download refer https://docs.docker.com/desktop/  
3. Build the Image  <docker build . -t sample-flask-app:v1>
4. list the images <docker image ls>
5. Run the container using the image build above, <docker container run -d -p 5000:5000 sample-flask-app:v1>
6. check the running container <docker container ls>
7. navigate to browser and type the URL "http://localhost:5000/"
8. to stop the container, <docker stop 'containerid from step 6'>
9. to remove the build image, <docker image rm 'imageid if from step 4' -f>
