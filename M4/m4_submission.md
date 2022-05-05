<table><tr><td> <em>Assignment: </em> M4-Simple-Calc</td></tr>
<tr><td> <em>Student: </em> Saidarshini Nannapuraju(sn745)</td></tr>
<tr><td> <em>Generated: </em> 06/05/2022 01:43:58</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-004-S22/m4-simple-calc/grade/sn745" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <p>Make sure you&#39;re working in an up to date branch</p>
<ul>
<li><code>git checkout dev</code></li>
<li><code>git pull origin dev</code></li>
<li><code>git checkout -b M4-Simple-Calc</code></li>
</ul>
<p>This will likely be started in class.</p>
<p>Steps:</p>
<ol>
<li>Create a new Folder called M4</li>
<li>Create a new file called MyCalc.py inside this folder</li>
<li>Create a MyCalc Class</li>
<li>Define basic addition / subtraction / multiplication / division functions<ol>
<li>These functions should update an internal variable as a running total/value called <code>ans</code></li>
<li>All functions must properly handle the math given standard math scenarios (i.e., show proper messages when trying to divide by zero)</li>
<li>Since you&#39;ll likely be taking screenshots of the code, make sure you add a comment with your ucid and the date</li>
</ol>
</li>
<li>Define a &quot;main&quot; logic to run when the program runs</li>
<li>This logic should ask for user input<ol>
<li>The input can be any valid number, any valid math operator, and any valid number (i.e., 2 * 2)<ol>
<li>This will do an immediate calculation, print it, and store the answer in the <code>ans</code> variable</li>
</ol>
</li>
<li>Alternatively, the input can be <code>ans</code>, any valid math operator, any valid number (i.e., <code>ans</code> * 2)<ol>
<li>This will use the previous answer (or 0 if not set) as part of the calculation, print it, and will store the new answer in the <code>ans</code> variable</li>
</ol>
</li>
</ol>
</li>
<li>Create a test case for each scenario that utilize functions to have expected input and compare against expected output, all cases should pass<ol>
<li>Test number-add-number</li>
<li>Test ans-add-number</li>
<li>Test number-sub-number</li>
<li>Test ans-sum-number</li>
<li>Test number-mult-number</li>
<li>Test ans-mult-number</li>
<li>Test number-div-number</li>
<li>Test ans-div-number</li>
</ol>
</li>
<li>Create a new file called m4_submission.md inside the M4 folder</li>
<li>Fill out the below deliverables</li>
<li>Generate the markdown and paste it into the m4_submission.md</li>
<li><code>git add .</code></li>
<li><code>git commit -m &quot;adding m4 hw&quot;</code></li>
<li><code>git push origin M4-Simple-Calc</code></li>
<li>Create a pull request M4-Simple-Calc to dev</li>
<li>Create a pull request dev to prod (after the previous one is merged)</li>
<li>Navigate to the prod branch on github, go to the M4 folder, click the m4_submission.md</li>
<li>Submit this link to Canvas</li>
</ol>
</td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Code Snippets (Make sure each screenshot has a comment showing your ucid and the date it was written) </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot of valid Addition Function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/99361267/167002150-a5d2dea3-cbc7-4677-ba2d-977a7dfc1fd8.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>sn745 - this function addition will take two arguments a,b add them and<br>store in self.ans variable<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshot of valid Subtraction Function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/99361267/167004020-54f8c87e-1d2e-40e1-a322-0125696e2474.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>sn745 - this function subtraction will take two arguments a,b perform a-b and<br>them store in self.ans variable<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshot of valid Multiplication Function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/99361267/167004305-d995e7c1-8375-44e3-ab0c-621167808e7d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>sn745 - this function multiplication  will take two arguments a,b perform a*b<br>and them store in self.ans variable<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Screenshot of valid division Function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/99361267/167004502-23065d43-65d0-4d88-afb2-89ba2dd0602d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>sn745 - this function division  will take two arguments a,b perform a/b<br>and them store in self.ans variable. if b==0 it raises ZeroDivisionError exception.<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Test Case Validations </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot of passing number-add-number Test Case (should test multiple values via fixture)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/99361267/167004822-fd064905-66d5-41b5-a4a4-d3be970a7e95.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>sn745 - Before running test case we created instance of MyCalc. We wrote<br>a function number_add_number which calls  method run with arguments 2, &quot;+&quot;, 2.<br>Here we used operator &quot;+&quot; so it calls addition method. Next we compared<br>actual and expected values with self.assertEqual<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshot of passing ans-add-number Test Case (should test multiple values via fixture, ans should be a cached value from a previous case)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/99361267/167005991-d56fd3b8-c02c-454d-82c5-94e1456162ff.png"/></td></tr>
<tr><td> <em>Caption:</em> <p> sn745 - Before running test case we created instance of MyCalc. We<br>wrote a function  ans_add_number which calls  method  run with arguments<br> Number,  &quot;+&quot;,  Number. We passed previous ans as first argument<br>Here we used operator  “+”  so it calls addition  method.<br>Next we compared actual and expected values with self.assertEqual<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshot of passing number-sub-number Test Case (should test multiple values via fixture)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/99361267/167006477-ab30cea7-9c7e-4e41-b08d-c705773eaed3.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>sn745 - Before starting the test case, we created an instance of MyCalc.<br>The function number_sub_number calls a procedure with arguments 10, &quot;-&quot;, and 4. We<br>used the operator &quot;-&quot; here, which is called the subtraction method. Then we<br>compared actual and expected values with self.assertEqual<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Screenshot of passing ans-sub-number Test Case (should test multiple values via fixture, ans should be a cached value from a previous case)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/99361267/167008607-18abe8ff-eb2e-428b-979c-3ed128eba03c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>sn745 - Before starting the test case, we created an instance of MyCalc.<br>The function ans_sub_number calls a procedure with arguments, self,ans &quot;-&quot;, and 2. We<br>used the operator &quot;-&quot; here, which is called the subtraction method. Then we<br>compared actual and expected values with self.assertEqual<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 5: </em> Screenshot of passing number-mult-number Test Case (should test multiple values via fixture)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/99361267/167008953-f87aa6ae-1efb-4198-87cb-e7eeddbadf7b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>sn745 - Before starting the test case, we created an instance of MyCalc.<br>The function number_mult_number  calls a procedure with arguments,  2 &quot;<em>&quot;, and<br>12. We used the operator &quot;</em>&quot; here, which is called the multiplication method.<br>Then we compared actual and expected values with self.assertEqual<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 6: </em> Screenshot of passing ans-multi-number Test Case (should test multiple values via fixture, ans should be a cached value from a previous case)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/99361267/167008883-cd9e7132-d80d-41ca-875d-076050ded4e3.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>sn745 - Before starting the test case, we created an instance of MyCalc.<br>The function ans_mult_number  calls a procedure with arguments, self,ans &quot;<em>&quot;, and 2.<br>We used the operator &quot;</em>&quot; here, which is called the multiplication method. Then<br>we compared actual and expected values with self.assertEqual<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 7: </em> Screenshot of passing number-div-number Test Case (should test multiple values via fixture, ans should be a cached value from a previous case)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/99361267/167009440-2b857f93-4d67-4def-aae3-ee4abe7185f9.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>sn745 - Before starting the test case, we created an instance of MyCalc.<br>The function number_div_number  calls a procedure with arguments,  20 &quot;/&quot;, and<br>2. We used the operator &quot;/&quot; here, which is called the division method.<br>Then we compared actual and expected values with self.assertEqual<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 8: </em> Screenshot of passing ans-div-number Test Case (should test multiple values via fixture, ans should be a cached value from a previous case)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/99361267/167009494-52a63d08-2cab-4b17-9c29-71714faba114.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>sn745 - Before starting the test case, we created an instance of MyCalc.<br>The function ans_div_number  calls a procedure with arguments,  self.ans &quot;/&quot;, and<br>5. We used the operator &quot;/&quot; here, which is called the division method.<br>Then we compared actual and expected values with self.assertEqual<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Briefly talk about anything you learn during this assignment/module</td></tr>
<tr><td> <em>Response:</em> <p>How classes are declared in python<br>Define Constructure in Class<br>Handle exceptions<br>create class instances<br></p><br></td></tr>
<tr><td> <em>Sub-Task 2: </em> Discuss how test cases work and anything new you learned about them while doing this assignment</td></tr>
<tr><td> <em>Response:</em> <p>How can we write test cases to test out logic code using the<br>unit test module<br>Got to know about assertEqual<br>run test cases</p><br><br></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add the pull request of M4-Simple-Calc to Dev link</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/SaiDarshiniNannapuraju/is601-004/pull/4">https://github.com/SaiDarshiniNannapuraju/is601-004/pull/4</a> </td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-004-S22/m4-simple-calc/grade/sn745" target="_blank">Grading</a></td></tr></table>
