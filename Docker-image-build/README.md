1. clone this repo, using <git clone > and cd to 
2. docker-client should be running on your system to run docker commands.  
3. Build the Image  <docker build . -t sample-flask-app:v1>
4. list the images <docker image ls>
5. Run the container using the image build above, <docker container run -d -p 5000:5000 sample-flask-app:v1>
6. check the running container <docker container ls>
7. navigate to browser and type the URL "http://localhost:5000/"
8. to stop the container, <docker stop 'containerid from step 6'>
9. to remove the build image, <docker image rm 'image if from step 4' -f>
