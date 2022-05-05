<table><tr><td> <em>Assignment: </em> Mini Project 3 - Flask AdvCalc</td></tr>
<tr><td> <em>Student: </em> Saidarshini Nannapuraju(sn745)</td></tr>
<tr><td> <em>Generated: </em> 06/05/2022 05:09:42</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-004-S22/mini-project-3---flask-advcalc/grade/sn745" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <ol>
<li>Create a new branch called MP3-Flask-AdvCalc</li>
<li>Add the ability to load a basic csv file of mixed sets of data/equations for add/sub/div/mult</li>
<li>Add UI support for your 5 stats functions from MP2 (buttons on the screen that trigger the equation) The user should be able to enter data and run each of your stats functions as expected</li>
<li>Add the ability to load an advanced csv file of fixed data/equations for the 5 stats functions (or load in 5 different files separately)</li>
<li>Give the ability for the user to delete a single history item of theirs</li>
<li>Give the ability for the user to delete all of their history (this should not affect any other user&#39;s history)</li>
<li>Add test cases to <ol>
<li>Register a user</li>
<li>Login the user</li>
<li>To run a calc function for the user and record/create a SimpleHistory (verify this gets created with proper data)</li>
<li>Make sure the User and SimpleHistory data get deleted after the test phase</li>
</ol>
</li>
<li>Fill in the below deliverables (make sure screenshots load properly)</li>
<li>Create an mp3_submission.md file in your project/app folder</li>
<li>Paste the generated markdown into this file</li>
<li>git add/commit/push to MP3-Flask-AdvCalc</li>
<li>Merge to dev</li>
<li>Merge dev to prod</li>
<li>Find the mp3_submission.md in the prod branch on github</li>
<li>Submit the direct link to that file to Canvas</li>
</ol>
</td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Basic CSV Loading </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot of the mixed csv data of add/sub/mult/div</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/99361267/167039013-e91288c0-e2dd-4653-8a96-216019a582b1.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Here i am loading a CSV and taking which operation to perform from<br>the API<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot of the history after uploading the csv file</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/99361267/167039734-6b019dc2-a9de-499e-baee-b0357cf6cf91.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Here we are taking csv file and user defined basic math operations<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain how the csv is processed and the data is sent to the calculator</td></tr>
<tr><td> <em>Response:</em> <p>We are iteration row by row using the CSV module<br>we took input from<br>API on whether to perform add/sub/div/mult<br>based on the operator we are using AdvCalc<br>which inherited Mycal<br>We are reusing the same code<br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Adv Calc Functions </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot showing the new Advanced buttons on the UI</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/99361267/167040847-fbbe2c20-ffb8-47cf-98c3-85639b62010b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>We added all 5 under one drop down<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot showing the aggregated history of each 5 advanced function being ran</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/99361267/167041205-02097620-04dd-4b46-a816-50c6fbeac918.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Here user entered 1,2,3,6,10 as input values and selects Mean and submits<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Explain how you updated the calculator to handle the advanced function interaction</td></tr>
<tr><td> <em>Response:</em> <p>Listed all the advanced functions under a drop-down<br>Provided an input box to get<br>input from the user(comma separated)<br>Once the user selects any one of the advanced<br>functions and clicks on submit button we show a text at the bottom<br>of the calculator<br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Advanced CSV Loading </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://via.placeholder.com/400x120/f2c037/000000?text=Partial"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot of mixed advanced csv data (or separate csv files if you wish)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/99361267/167042334-14c09b66-b590-45dd-988b-dc81648f7dd1.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>We used pandas and calculated<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot showing the aggregated history the csv file execution</td></tr>
<tr><td><table><tr><td>Missing Image</td></tr>
<tr><td> <em>Caption:</em> (missing)</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Explain how you updated the calculator to handle the advanced function interaction</td></tr>
<tr><td> <em>Response:</em> <p>We used most of the reusable code which we already coded as part<br>of previous assignments<br>Once the user enters input and clicks on submit button we<br>will redirect to the results page and clear input box and show results<br>at the bottom next to form <br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> History Management </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://via.placeholder.com/400x120/f2c037/000000?text=Partial"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Show a before and after screenshot of deleting a single history item</td></tr>
<tr><td><table><tr><td>Missing Image</td></tr>
<tr><td> <em>Caption:</em> <p>We tried using JavaScript but it is making us easy for logging history<br>but i did not find option to delete history one by one<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Show a before and after screenshot showing the history being cleared (all of it for this user)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/99361267/167043652-6d27048b-ac21-487f-adaf-67c7bd488fef.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Clearing of history is not added<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Show that the history is still present for other users (that task 2 didn't delete it for other users)</td></tr>
<tr><td><table><tr><td>Missing Image</td></tr>
<tr><td> <em>Caption:</em> (missing)</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Explain how you implemented single delete of the history</td></tr>
<tr><td> <em>Response:</em> <p>We tried to implement it by deleting that index from the given text.<br>but is is not handy<br></p><br></td></tr>
<tr><td> <em>Sub-Task 5: </em> Explain how you implemented deleting all of the logged in user's history</td></tr>
<tr><td> <em>Response:</em> <p>(missing)</p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 5: </em> Test Cases </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://via.placeholder.com/400x120/f2c037/000000?text=Partial"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot the test case code to register a test user via pytest</td></tr>
<tr><td><table><tr><td>Missing Image</td></tr>
<tr><td> <em>Caption:</em> <p>We use pytest as an alternative to unit test. but in pytest we<br>have more functionalities available<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshot the passing test case from pytest for task 1</td></tr>
<tr><td><table><tr><td>Missing Image</td></tr>
<tr><td> <em>Caption:</em> (missing)</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshot the test case code for logging in the test user via pytest</td></tr>
<tr><td><table><tr><td>Missing Image</td></tr>
<tr><td> <em>Caption:</em> (missing)</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Screenshot the passing test case from pytest for task 3</td></tr>
<tr><td><table><tr><td>Missing Image</td></tr>
<tr><td> <em>Caption:</em> (missing)</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 5: </em> Screenshot the test case code for recording a SimpleHistory for the test user (should be a valid generation from the calculator)</td></tr>
<tr><td><table><tr><td>Missing Image</td></tr>
<tr><td> <em>Caption:</em> (missing)</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 6: </em> Screenshot the passing test case from pytest for task 5</td></tr>
<tr><td><table><tr><td>Missing Image</td></tr>
<tr><td> <em>Caption:</em> (missing)</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 7: </em> Explain the flow/process of these new test cases that pass the test user around</td></tr>
<tr><td> <em>Response:</em> <p>(missing)</p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 6: </em> Add a link to your deployed app </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://via.placeholder.com/400x120/ff0000/000000?text=Incomplete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add the link here to the hosted instance</td></tr>
<tr><td>Not provided</td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-004-S22/mini-project-3---flask-advcalc/grade/sn745" target="_blank">Grading</a></td></tr></table>
