# WP9 has *not* published yet any recommended Docker images
# Here we are using an existing python3+numpy+panda+etc third
# party published Docker image (weighting at 60MB only!!!)
FROM frolvlad/alpine-python-machinelearning 

# Install more dependencies here (if needed)
# RUN pip install some-package
