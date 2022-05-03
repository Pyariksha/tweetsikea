# tweetsikea<br>
<h2>This repo contains the files used to create a GCP pipeline to get ikea tweets and store in BQ table for end user data scientists to use.</h2><br>
Contents:<br>
1. main.py -- contains python script<br>
2. requirements.txt -- contains import requirements<br>
3. main_test.py -- contains pytest unit test run in CI<br>
4. cloudbuild.yaml -- contains config steps for cloudbuild (1. build, 2. deploy)<br>
5. Keynote presentation for this project - contains flow and basic output snips<br>
6. This README.md outlining the project<br>
<h2>The flow of the batch process pipeline is as follows:</h2>
<img width="996" alt="image" src="https://user-images.githubusercontent.com/50378431/166420420-42d6a971-c321-4251-9496-3b98706a208b.png"><br>
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
  -Extra file containing bq sql DDL query - EL(T)<br>
  -Extra flow for proposed stream via databricks<br>
  </p>
  <h3>Sample output in bq:</h3><br>
  <img width="1338" alt="image" src="https://user-images.githubusercontent.com/50378431/166423045-61798236-9c0e-429c-808f-0a70edd143eb.png"
  <h3>What more can be done:</h3>
  -Streaming pipeline<br>
  -Delta tables for versions/history<br>
  -Airflow for pipeline automation<br>
  -More complex data model using twitter data for insights
