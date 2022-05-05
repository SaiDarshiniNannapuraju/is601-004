<table><tr><td> <em>Assignment: </em> Mini Project 2_Advanced Calculator</td></tr>
<tr><td> <em>Student: </em> Saidarshini Nannapuraju(sn745)</td></tr>
<tr><td> <em>Generated: </em> 06/05/2022 03:39:04</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-004-S22/mini-project-2_advanced-calculator/grade/sn745" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <p>Prepare your workspace</p>
<ol>
<li><code>git checkout dev</code></li>
<li><code>git pull origin dev</code></li>
<li><code>git checkout -b MP2-AdvCalc</code></li>
</ol>
<p>In this project, you&#39;ll decorate or extend one of the given MyCalc samples (do not edit MyCalc directly).
For every added calculation you&#39;ll need to provide a positive and negative test case.
<strong>Note:</strong> negative test cases will throw and capture exceptions to generate a positive test case
Negative test cases test for invalid input and/or invalid operations. These test cases will be via csv files as well 
(just like the changes to addition, subtraction, multiplication, division, square, and square root)</p>
<p>HINT 1: You can generate a normal distribution of random distribution of numbers with excel to use for your data:  Here (<a href="http://howtoexcel.org/statistics/normal-distribution/">http://howtoexcel.org/statistics/normal-distribution/</a>)</p>
<p>HINT 2: You can create another excel file that contains the answers to your calculations that you can use in your unit tests.</p>
<p><strong>Your program needs to additionally calculate the following:</strong></p>
<ol>
<li>Square</li>
<li>Square Root</li>
<li>Pick 5 from below<ul>
<li>Population Mean</li>
<li>Median</li>
<li>Mode</li>
<li>Population Standard Deviation</li>
<li>Variance of population proportion</li>
<li>Z-Score</li>
<li>Standardized score</li>
<li>Population Correlation Coefficient</li>
<li>Confidence Interval</li>
<li>Population Variance</li>
<li>P Value</li>
<li>Proportion</li>
<li>Sample Mean</li>
<li>Sample Standard Deviation</li>
<li>Variance of sample proportion</li>
</ul>
</li>
</ol>
<ul>
<li>You&#39;ll update your previous test cases to read from csv files for the input and output values.</li>
<li>Use the below csv files for your existing test cases of addition, subtraction, multiplication, and division.
As well as testing the new square and square root modifications.</li>
</ul>
<p><strong>Note</strong>: You may need to view the data via the &quot;Raw&quot; button on the gist.
<a href="https://gist.github.com/MattToegel/958ad17cc2c94337a5260126639eefbe">https://gist.github.com/MattToegel/958ad17cc2c94337a5260126639eefbe</a> </p>
<p>Once done do the following:</p>
<ol>
<li>Git add all changes (including the test case csv files)</li>
<li>Git commit with relevant messages</li>
<li>Git push origin MP2-AdvCalc</li>
<li>Create a Pull Request on Github to dev (keep it open)</li>
<li>Fill out the details here</li>
<li>Save and Generate the markdown (any changes require this step to be repeated)</li>
<li>Paste the content into a <code>mp2_submission.md</code> file</li>
<li>Git add/commit/push the submission file change</li>
<li>Complete the pull request merge</li>
<li>Create a new pull request from dev to prod and complete it</li>
<li>Navigate to prod branch&#39;s <code>mp2_submission.md</code> file and paste the direct link to Canvas</li>
</ol>
</td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Added Functionality: Square </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot of the new function (include your ucid and date)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/99361267/167027510-ca2458c0-662c-45b0-9520-3a9a0d14bc13.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>defined a function square which takes number as arguments and return number*number<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshot of the passing test cases from the csv file</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/99361267/167027986-85194a37-4d9b-4498-abe1-16d4c5350a3f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Read both input and expected data from csv file and compare actual and<br>expected<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Added Functionality: Square Root </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot of the new function (include your ucid and date)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/99361267/167027529-d3c658a3-b9ed-46db-9fab-8eb72f83f398.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>defined a function square_root which takes number as arguments and return square root<br>of given number. Here i used math module<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshot of the passing test cases from the csv file</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/99361267/167028015-3b4f288b-5976-4dec-8df9-5fedcfce3c40.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Read both input and expected data from csv file and compare actual and<br>expected<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Choice 1 </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://via.placeholder.com/400x120/f2c037/000000?text=Partial"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Label what your choice was and explain the usage/purpose from the math perspective</td></tr>
<tr><td> <em>Response:</em> <p>Mean</p><br><ul><br><li>It is used to calculate the average value from the data set<br></li><br></ul><br></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshot of the new function (include your ucid and date)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/99361267/167027543-878cb631-b8ec-4172-8e58-b6740bf593ad.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>formula for mean is sum of values divided with number fo values<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshot of positive test case execution</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/99361267/167031678-5437de97-56b3-4036-9ed3-de6b1aec4325.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Compared b/w expected and actual mean value<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Screenshot of negative test case execution</td></tr>
<tr><td><table><tr><td>Missing Image</td></tr>
<tr><td> <em>Caption:</em> (missing)</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> Choice 2 </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://via.placeholder.com/400x120/f2c037/000000?text=Partial"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Label what your choice was and explain the usage/purpose from the math perspective</td></tr>
<tr><td> <em>Response:</em> <p>Median</p><br><ul><br><li>middle value in a list ordered from smallest to largest.<br></li><br></ul><br></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshot of the new function (include your ucid and date)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/99361267/167027575-86f7dbb4-b417-44e9-bc04-9b9a20ba42e0.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Sort data set and find the middle index value and return corresponding value<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshot of positive test case execution</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/99361267/167031862-3f366509-df31-4831-a9d5-09515e993424.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Compare b/w expected and actual median value<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Screenshot of negative test case execution</td></tr>
<tr><td><table><tr><td>Missing Image</td></tr>
<tr><td> <em>Caption:</em> (missing)</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 5: </em> Choice 3 </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Label what your choice was and explain the usage/purpose from the math perspective</td></tr>
<tr><td> <em>Response:</em> <p>Mode</p><br><p>most frequently occurring value on the list.<br></p><br></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshot of the new function (include your ucid and date)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/99361267/167029945-b42029f5-f716-4257-8ed8-ade87a6b96cd.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>count occurence of each element in a list and find the most occured<br>element<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshot of positive test case execution</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/99361267/167032347-2e8692f0-984a-4767-89c0-4b0fa3fea664.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>given data set 1,2,3,3 the most repeated element is 3<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Screenshot of negative test case execution</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/99361267/167032347-2e8692f0-984a-4767-89c0-4b0fa3fea664.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>given data set 1,2,3 as we don&#39;t have most repeated element return &quot;No<br>mode found&quot;<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 6: </em> Choice 4 </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Label what your choice was and explain the usage/purpose from the math perspective</td></tr>
<tr><td> <em>Response:</em> <p>Standard deviation<br>represents the distance between any two values from the mean<br></p><br></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshot of the new function (include your ucid and date)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/99361267/167030537-a808f224-c04c-4b89-81cd-0da152d98568.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>calculate mean for given set of data and then sum of differences and<br>pow 0.5<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshot of positive test case execution</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/99361267/167032868-5673b1bb-34de-4164-9319-af63b4baa5b5.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Compare b/w expected and actual Standard deviation value<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Screenshot of positive test case execution</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/99361267/167032868-5673b1bb-34de-4164-9319-af63b4baa5b5.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Compare b/w expected and actual Standard deviation value<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 7: </em> Choice 5 </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://via.placeholder.com/400x120/f2c037/000000?text=Partial"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Label what your choice was and explain the usage/purpose from the math perspective</td></tr>
<tr><td> <em>Response:</em> <p>Z-score<br>determines whether a score falls within a standard normal distribution<br></p><br></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshot of the new function (include your ucid and date)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/99361267/167031015-27fd2297-16fe-43c9-b465-a9d11d9c6bb9.png"/></td></tr>
<tr><td> <em>Caption:</em> (missing)</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshot of positive test case execution</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/99361267/167032851-e36ab071-e9a6-4fa1-8493-cd466c1a3ac0.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Compare b/w expected and actual values. given list returns list. this calculation is<br>dependent on standart deviation<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Screenshot of positive test case execution</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/99361267/167032851-e36ab071-e9a6-4fa1-8493-cd466c1a3ac0.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Compare b/w expected and actual values. given list returns list. this calculation is<br>dependent on standart deviation<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 8: </em> Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://via.placeholder.com/400x120/f2c037/000000?text=Partial"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Mention any difficulties and how you overcame them or what you learned during this mini project.</td></tr>
<tr><td> <em>Response:</em> <p>How to use math module<br>How to use a counter method from collections<br>Once again<br>go through the mathematical definitions<br>difference between positive and negative test cases <br></p><br></td></tr>
<tr><td> <em>Sub-Task 2: </em> Pull Request Link(s) for this project</td></tr>
<tr><td>Not provided</td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-004-S22/mini-project-2_advanced-calculator/grade/sn745" target="_blank">Grading</a></td></tr></table>
