# tweetsikea<br>
<h2>This repo contains the files used to create a GCP pipeline to get ikea tweets and store in BQ table for end user data scientists to use.</h2><br>
<h3>This repo contains the following:</h3><br>
1. main.py -- contains python script<br>
2. requirements.txt -- contains import requirements<br>
3. main_test.py -- contains pytest unit test run in CI<br>
4. cloudbuild.yaml -- contains config steps for cloudbuild (1. build, 2. deploy)<br>
6. This README.md outlining the project<br>
7. Presentations (keynote file and pdf version) - contains flow and basic output snips<br>
8. Extra file containing bq sql DDL query - EL(T)<br>
9. Draft extra flow diagram for proposed stream<br>
<h3>Contents:</h3><br>
1. The flow of the batch process pipeline<br>
2. The SE principles, languages and cloud tools this project uses<br>
3. Sample output in bq<br>
4. What more can be done<br>
5. Extra draft stream flow<br>
<h2>1. The flow of the batch process pipeline</h2>
<img width="996" alt="image" src="https://user-images.githubusercontent.com/50378431/166420420-42d6a971-c321-4251-9496-3b98706a208b.png"><br>
<p><h2>2. The SE principles, languages and cloud tools this project uses</h2>
  SE principles:<br>
  -Version control with GitHub<br>
  -CI/CD with cloudbuild.yaml<br>
  -Unit testing using pytest: see below unit test run successful in cloud build<br>
  <img width="1036" alt="image" src="https://user-images.githubusercontent.com/50378431/166442423-ff39d457-3b7c-4d5f-b563-e4ee0208e5a5.png"><br>
  Google cloud resources:<br>
  -Cloud build
  -Pub Sub for event triggers<br>
  -Cloud scheduler for automating function runs to get ikea tweets data<br>
  -BigQuery table to store appended tweets per batch<br>
  -Docker containers - artifact repository images (Not included in cloudbuild but script is created)<br><br>
  Languages/scripts:<br>
  -Python functions using tweepy library to get ikea tweets and write to big query table<br>
  -BigQuery scheduled query to deduplicate table data<br>
  </p>
  <h2>3. Sample output in bq</h2>
  <img width="1338" alt="image" src="https://user-images.githubusercontent.com/50378431/166423045-61798236-9c0e-429c-808f-0a70edd143eb.png"<br>
  <h2>4. What more can be done</h2>
  -Streaming pipeline<br>
  -Great expectations<br>
  -Delta tables for versions/history<br>
  -Airflow for pipeline automation<br>
  -More complex data model using twitter data for deeper insights<br>
  <h2>5. Extra draft stream flow</h2>
