# tweetsikea<br>
###This repo contains the files used to create a pipeline to get ikea tweets and stor in BQ table for end user data scientists to use.<br>
###Overall the flow of the batch process pipeline is as follows:<br>
<img width="967" alt="image" src="https://user-images.githubusercontent.com/50378431/166337664-3f5a031e-d2b8-40a6-b1d9-a2112504f04b.png"><br>
<p>This project uses the following tools,functions and methodologies:<br>
  -Python functions using tweepy library to get ikea tweets and write to big query table<br>
  -Version control with GitHub<br>
  -CI/CD with cloudbuild.yaml<br>
  -Pub Sub for event triggers<br>
  -Cloud scheduler for automating function runs to get ikea tweets data<br>
  -Docker containers for builds in cloud build - artifact repository stores images<br>
  -Unit testing using pytest<br>
  </p><br>
  ####What more can be done:<br> 
  -Streaming pipeline<br>
  -Delta tables for versions/history<br>
  -Airflow for pipeline automation
  -More complex data model using twitter data for insights
