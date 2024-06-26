#!/bin/sh

# Start Nginx with specified options
nginx -g 'daemon off; error_log /dev/stdout debug;' &

# Start the Flask app in the background
gunicorn -b 0.0.0.0:8100 app:app &

wait
