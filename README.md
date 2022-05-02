# tweetsikea<br>
<h2>This repo contains the files used to create a GCP pipeline to get ikea tweets and store in BQ table for end user data scientists to use.</h2>
<h2>The flow of the batch process pipeline is as follows:</h2>
<img width="967" alt="image" src="https://user-images.githubusercontent.com/50378431/166337664-3f5a031e-d2b8-40a6-b1d9-a2112504f04b.png"><br>
<p><h2>This project uses the following:</h2>
  -Python functions using tweepy library to get ikea tweets and write to big query table<br>
  -Version control with GitHub<br>
  -CI/CD with cloudbuild.yaml<br>
  -Pub Sub for event triggers<br>
  -Cloud scheduler for automating function runs to get ikea tweets data<br>
  -BigQuery table to store appended tweets per batch<br>
  -BigQuery scheduled query to deduplicate table data<br>
  -Docker containers for builds in cloud build - artifact repository stores images<br>
  -Unit testing using pytest<br>
  </p><br>
  <h3>What more can be done:</h3>
  -Streaming pipeline<br>
  -Delta tables for versions/history<br>
  -Airflow for pipeline automation<br>
  -More complex data model using twitter data for insights
