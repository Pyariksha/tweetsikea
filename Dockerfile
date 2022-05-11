FROM python:3.9-slim

# Copy local code to the container image.
ENV APP_HOME /app
WORKDIR $APP_HOME
COPY ..
COPY requirements.txt ./

# Install production dependencies.
RUN pip install -r requirements.txt

# Run the python script
CMD ['python', 'main.py']
