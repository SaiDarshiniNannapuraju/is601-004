<table><tr><td> <em>Assignment: </em> IS601 Milestone1 Deliverable</td></tr>
<tr><td> <em>Student: </em> Saidarshini Nannapuraju(sn745)</td></tr>
<tr><td> <em>Generated: </em> 10/05/2022 01:42:08</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-004-S22/is601-milestone1-deliverable/grade/sn745" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <ol>
<li>Checkout Milestone1 branch</li>
<li>Create a milestone1.md file in your Project folder</li>
<li>Fill in the deliverable items</li>
<li>Ensure your images display correctly in the sample markdown at the bottom</li>
<li>Save the submission items</li>
<li>Copy/paste the markdown from the &quot;Copy markdown to clipboard link&quot;</li>
<li>Paste the code into the milestone1.md file</li>
<li>Git add/commit/push the md file to Milestone1</li>
<li>Double check the images load when viewing the markdown file (points will be lost for invalid/non-loading images)</li>
<li>Make a pull request from Milestone1 to dev and merge it (resolve any conflicts)<ol>
<li>Make sure everything looks ok</li>
</ol>
</li>
<li>Make a pull request from dev to prod (resolve any conflicts) <ol>
<li>Make sure everything looks ok on the deploy service</li>
</ol>
</li>
<li>Submit the direct link from github prod branch to the milestone1.md file (no other links will be accepted and will result in 0)</li>
</ol>
<p>Note: Make sure all provided links work as they&#39;re likely to be visited during testing/validation of this assignment</p>
</td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Feature: User will be able to register a new account </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add one or more screenshots of the application showing the form and validation errors per the feature requirements</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/99361267/167458342-771e2533-8efa-47e8-843a-6c4597630590.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Form fro registering new user<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot of the Users table with data in it</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/99361267/167458862-1f885086-fbe6-4c0b-988c-812f3374485f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>User table data is stored<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/SaiDarshiniNannapuraju/is601-004/pull/10">https://github.com/SaiDarshiniNannapuraju/is601-004/pull/10</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Explain briefly how the process/code works</td></tr>
<tr><td> <em>Response:</em> <p>Users can create their own account by specifying a username, email, and password<br>and confirming the password <br></p><br></td></tr>
<tr><td> <em>Sub-Task 5: </em> Add a link to your deployed app directly to a route related to this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://user-images.githubusercontent.com/99361267/167461607-76681736-a1a6-4b64-869b-138d2a57433f.png">https://user-images.githubusercontent.com/99361267/167461607-76681736-a1a6-4b64-869b-138d2a57433f.png</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Feature: User will be able to login to their account </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add one or more screenshots of the application showing the form and validation errors per the feature requirements</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/99361267/167462558-6fbabd92-e6d7-45dd-af2a-da991c7b19f8.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>When the user provided password and confirm password we are redirecting to error=password-not-matched<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot of successful login</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/99361267/167461870-609b01b3-8ad2-4093-b7d2-7054249abbd2.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>When user provide right user name and password they can login<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/SaiDarshiniNannapuraju/is601-004/pull/10">https://github.com/SaiDarshiniNannapuraju/is601-004/pull/10</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Explain briefly how the process/code works</td></tr>
<tr><td> <em>Response:</em> <p>Firstiy user should register himself if he does not have an account<br>While registering<br>users he needs to provide a username, email, and password and confirm the<br>password<br>if the user already exists  we redirect to ?error=user-or-email-exists<br>if everything is good<br>we show success=account-created and redirect to login page <br></p><br></td></tr>
<tr><td> <em>Sub-Task 5: </em> Add a link to your deployed app directly to a route related to this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://user-images.githubusercontent.com/99361267/167465992-a42fc0a3-a0c4-4cd2-bde0-18e383ac8dd9.png">https://user-images.githubusercontent.com/99361267/167465992-a42fc0a3-a0c4-4cd2-bde0-18e383ac8dd9.png</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Feat: Users will be able to logout </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot showing the successful logout message</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/99361267/167466132-0b9581d5-d52b-4b39-abc2-5e88072ec9bd.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>When the user click on logout we redirect to login page and url<br>as login?success=logged-out<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot showing the logged out user can't access a login-protected page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/99361267/167466359-9ca118be-078a-4f8b-94ec-d0147b41b91c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>using LoginManager in flask we are showing Unauthorized message<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/SaiDarshiniNannapuraju/is601-004/pull/10">https://github.com/SaiDarshiniNannapuraju/is601-004/pull/10</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Explain briefly how the process/code works</td></tr>
<tr><td> <em>Response:</em> <p>After the user is logged in,  A button is provided to logout<br>once<br>users log out that session is expired<br>if the user tries to access /home<br>we show an Unauthorized message<br></p><br></td></tr>
<tr><td> <em>Sub-Task 5: </em> Add a link to your deployed app directly to a route related to this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://user-images.githubusercontent.com/99361267/167466991-2cd9f0c7-5510-4b54-9e93-64461c3e1d3e.png">https://user-images.githubusercontent.com/99361267/167466991-2cd9f0c7-5510-4b54-9e93-64461c3e1d3e.png</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> Feature: Basic Security Rules Implemented / Basic Roles Implemented </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot showing the logged out user can't access a login-protected page (may be the same as similar request)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/99361267/167466359-9ca118be-078a-4f8b-94ec-d0147b41b91c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>using LoginManager in flask we are showing Unauthorized message<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot showing a user without an appropriate role can't access the role-protected page (a test/dummy page is fine)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/99361267/167484692-13f40a5f-e084-43ba-82e5-ceb3d179a55a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>User can&#39;t access the role-protected page without appropriate role<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add a screenshot of the Roles table with data</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/99361267/167485344-7b8e1a66-d493-4d0b-9da2-d6f34360dad9.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Roles table with data<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add a screenshot of the UserRoles table with data</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/99361267/167486085-8c690b22-da53-413d-bb67-49734a895faa.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>UserRoles table with data<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 5: </em> Add the related pull request(s) for these features</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/SaiDarshiniNannapuraju/is601-004/pull/10">https://github.com/SaiDarshiniNannapuraju/is601-004/pull/10</a> </td></tr>
<tr><td> <em>Sub-Task 6: </em> Explain briefly how the process/code works for login-protected pages</td></tr>
<tr><td> <em>Response:</em> <p>Use the Flask-Login library for session management.<br>Use the built-in Flask utility for hashing<br>passwords.<br>Add protected pages to the app for logged-in users only.<br>Use Flask-SQLAlchemy to create<br>a User model.<br>Create sign-up and login forms for the users to create accounts<br>and log in<br></p><br></td></tr>
<tr><td> <em>Sub-Task 7: </em> Explain briefly how the process/code works for role-protected pages</td></tr>
<tr><td> <em>Response:</em> <p>developers who use role-protected pages for access management can mitigate the errors that<br>come from assigning permissions to users individually.\nyou can use the auth0 dashboard to<br>enable role-based access control by creating api permissions<br></p><br></td></tr>
<tr><td> <em>Sub-Task 8: </em> Add a link to your deployed app directly to a route related to this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/SaiDarshiniNannapuraju/is601-004/pull/10">https://github.com/SaiDarshiniNannapuraju/is601-004/pull/10</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 5: </em> Feature: Site should have basic styles/theme applied; everything should be styled </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots to show examples of your site's styles/theme</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/99361267/167487141-71104880-3def-4751-b8fa-b9e9877e9dc3.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>We used basic style that comes with anchor tag and button<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/SaiDarshiniNannapuraju/is601-004/pull/10">https://github.com/SaiDarshiniNannapuraju/is601-004/pull/10</a> </td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain your CSS at a high level</td></tr>
<tr><td> <em>Response:</em> <p>CSS, handle webpage look and feel.<br>We can control the text color, font style<br></p><br></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add a link to your deployed app directly to a route related to this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/SaiDarshiniNannapuraju/is601-004/pull/10">https://github.com/SaiDarshiniNannapuraju/is601-004/pull/10</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 6: </em> Feature: Any output messages/errors should be "user friendly" </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots of some examples of errors/messages</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/99361267/167488318-54ab52d5-9f00-46c0-b4c4-a693bcd728db.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Username exists in DB but wrong password then we show &quot;error=incorrect-password&quot; in url<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a related pull request</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/SaiDarshiniNannapuraju/is601-004/pull/10">https://github.com/SaiDarshiniNannapuraju/is601-004/pull/10</a> </td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain how you made messages user friendly</td></tr>
<tr><td> <em>Response:</em> <p>I used the redirect function from the flask itself<br>Ex:<br>redirect(url_for(&#39;register.show&#39;) + &#39;?error=user-or-email-exists&#39;)<br>url_for represents page<br>and next following message as parameters to url<br></p><br></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add a link to your deployed app directly to a route related to this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/SaiDarshiniNannapuraju/is601-004/pull/10">https://github.com/SaiDarshiniNannapuraju/is601-004/pull/10</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 7: </em> Feature: Users will be able to see their profile </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots of the User Profile page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/99361267/167489083-bf5a1261-c5bc-44f3-9c2c-5d26f7e8271a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>We are showing welcome message currently<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/SaiDarshiniNannapuraju/is601-004/pull/10">https://github.com/SaiDarshiniNannapuraju/is601-004/pull/10</a> </td></tr>
<tr><td> <em>Sub-Task 3: </em> Explain briefly how the process/code works (view only)</td></tr>
<tr><td> <em>Response:</em> <p>Once the user login successfully then he can edit his profile<br></p><br></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add a link to your deployed app directly to a route related to this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/SaiDarshiniNannapuraju/is601-004/pull/10">https://github.com/SaiDarshiniNannapuraju/is601-004/pull/10</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 8: </em> Feature: User will be able to edit their profile </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots of the User Profile page validation messages and success messages</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/99361267/167489363-7e315e5d-a0d2-4e41-bb4b-ab1ffd2aa845.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Currently not yet implemented profile page for the user<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add before and after screenshots of the Users table when a user edits their profile</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/99361267/167489560-7c73a9c1-e3c3-40f0-9218-d6f464a15ac8.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>No edit option provided<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/SaiDarshiniNannapuraju/is601-004/pull/10">https://github.com/SaiDarshiniNannapuraju/is601-004/pull/10</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Explain briefly how the process/code works (edit only)</td></tr>
<tr><td> <em>Response:</em> <p> We have to provide an edit option on the profile page<br>After editing<br>the fields we will update the form fields with the latest modified values<br>after getting conformation <br></p><br></td></tr>
<tr><td> <em>Sub-Task 5: </em> Add a link to your deployed app directly to a route related to this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/SaiDarshiniNannapuraju/is601-004/pull/10">https://github.com/SaiDarshiniNannapuraju/is601-004/pull/10</a> </td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-004-S22/is601-milestone1-deliverable/grade/sn745" target="_blank">Grading</a></td></tr></table>
