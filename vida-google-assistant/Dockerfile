FROM python:3.8-alpine

# Install bash, uuid-runtime (uuidgen in Alpine is part of the util-linux package), curl, jq
# and nginx. Note that Alpine uses apk instead of apt
RUN apk add --no-cache nginx

# Install gcc and musl-dev for compiling Python packages, if necessary for Flask extensions
RUN apk add --no-cache gcc musl-dev

# Copy the requirements file
COPY ./requirements.txt /requirements.txt

# Install Flask and other Python dependencies from the requirements file
RUN pip install -r requirements.txt

# Copy the flask app
COPY app.py /app.py

# Copy the templates directory
COPY templates /templates

# Copy the run script
COPY run.sh /run.sh

# Since you mentioned nginx configuration, adjust the path according to where nginx expects it in Alpine
# Adjust the nginx configuration path as per Alpine's nginx package structure
COPY ingress.conf /etc/nginx/conf.d/default.conf

# Set up a directory for the Nginx run files (might not be necessary in Alpine as the nginx package takes care of this)
RUN mkdir -p /run/nginx

# Make the run script, backup script, and start script executable
RUN chmod a+x /run.sh

# Use start.sh as the default command
CMD ["/run.sh"]