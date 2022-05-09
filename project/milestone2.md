<table><tr><td> <em>Assignment: </em> IS601 Milestone 2 Shop Project</td></tr>
<tr><td> <em>Student: </em> Saidarshini Nannapuraju(sn745)</td></tr>
<tr><td> <em>Generated: </em> 10/05/2022 00:32:00</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-004-S22/is601-milestone-2-shop-project/grade/sn745" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <ol>
<li>Checkout Milestone2 branch </li>
<li>Create a new markdown file called milestone2.md</li>
<li>git add/commit/push immediate</li>
<li>Fill in the below deliverables</li>
<li>At the end copy the markdown and paste it into milestone2.md</li>
<li>Add/commit/push the changes to Milestone2</li>
<li>PR Milestone2 to dev and verify</li>
<li>PR dev to prod and verify</li>
<li>Checkout dev locally and pull changes to get ready for Milestone 3</li>
<li>Submit the direct link to this new milestone2.md file from your GitHub prod branch to Canvas</li>
</ol>
<p>Note: Ensure all images appear properly on github and everywhere else.
Images are only accepted from Google Cloud, not localhost.
All website links must be from Google Cloud. </p>
</td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Users with admin or shop owner will be able to add products </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot of admin create item page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/99361267/167309406-636e6e42-a257-492e-9143-51b340580abe.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Admin can add items with category, name description, stock and price<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot of populated Products table clearly showing the columns</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/99361267/167309699-7b25c791-84fa-43e2-a333-beef87b2bc0c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>This table contains columns as category, slug, name, description, price, available, stock, created_at,<br>updated_at, image<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly describe the code flow for creating a Product</td></tr>
<tr><td> <em>Response:</em> <p>Only admin can add products <br>Edit Product info<br>At first, the admin should log<br>in and select products and fill in the details, and add them to<br>the list<br>Those are stored in shop_products DB and shown to users<br><br></p><br></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/SaiDarshiniNannapuraju/is601-004/pull/14">https://github.com/SaiDarshiniNannapuraju/is601-004/pull/14</a> </td></tr>
<tr><td> <em>Sub-Task 5: </em> Add a direct link to the related file from Google Cloud</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/SaiDarshiniNannapuraju/is601-004/pull/14">https://github.com/SaiDarshiniNannapuraju/is601-004/pull/14</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Any user can see visible products on the Shop Page </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot of the Shop page showing 10 items without filters/sorting applied</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/99361267/167310725-635c4806-b0d5-4e39-8a10-a9fc3e813606.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing home page with listing all the products available<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot of the Shop page showing both filters and a different sorting applied (should be more than 1 sample product)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/99361267/167310766-f4598014-97d4-4c81-b599-2d2d68bd4df8.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>In the above screenshot showing results after filtering with books <br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add a screenshot of the filter/sort logic from the code (ensure ucid and date is shown)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/99361267/167310849-98228057-e2ea-4f88-921a-6fc701dc9828.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Perform query based on category filter and query to database and send results<br>to template and render list of products<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Briefly explain how the results are shown and how the filters are applied</td></tr>
<tr><td> <em>Response:</em> <p>When the user clicks on any of the categories. then backend request is<br>raised and based on the category of user-specified.<br>A database query is performed using<br>the filter function.<br>Fetch results with user performed queries and results are shown in<br>the page<br></p><br></td></tr>
<tr><td> <em>Sub-Task 5: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/SaiDarshiniNannapuraju/is601-004/pull/14">https://github.com/SaiDarshiniNannapuraju/is601-004/pull/14</a> </td></tr>
<tr><td> <em>Sub-Task 6: </em> Add a direct link to the related file from Google Cloud</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/SaiDarshiniNannapuraju/is601-004/pull/14">https://github.com/SaiDarshiniNannapuraju/is601-004/pull/14</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Show Admin/Shop Owner Product List (this is not the Shop page and should show visibility status) </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot of the Admin List page/results</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/99361267/167311088-4c757de6-ec71-4516-8efc-3c638336e6e3.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>In the admin page we are showing all the products present and providing<br>option to add new products and edit existing products<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Briefly explain how the results are shown</td></tr>
<tr><td> <em>Response:</em> <p>When the request is hit with /admin url pattern we check for admin<br>authentication with user name and password<br>After authentication is successful we show all the<br>products list with edit access and adding products</p><br> <br></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/SaiDarshiniNannapuraju/is601-004/pull/14">https://github.com/SaiDarshiniNannapuraju/is601-004/pull/14</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Add a direct link to the related file from Google Cloud</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/SaiDarshiniNannapuraju/is601-004/pull/14">https://github.com/SaiDarshiniNannapuraju/is601-004/pull/14</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> Admin/Shop Owner Edit button </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a sceenshot showing the edit button visible to the Admin on the Shop page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/99361267/167311297-49ff1729-4cdc-46c5-a4bb-287d7f4c291c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>After clicking product in admin page, Edit page is opened  as above<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a sceenshot showing the edit button visible to the Admin on the Product Details Page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/99361267/167311297-49ff1729-4cdc-46c5-a4bb-287d7f4c291c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Currently , We have supported edit access to admin only in admin page<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add a sceenshot showing the edit button visible to the Admin on the Admin Product List Page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/99361267/167311499-55409655-65e2-410c-ac33-900d4d4aa7fc.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Once we hover on product name and click it will redirect to edit<br>page of corresponding product<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add a before and after screenshot of Editing a Product via the Admin Edit Product Page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/99361267/167311644-b3b3d228-04dd-44cb-8f07-a508ac9eaef7.png,   https://user-images.githubusercontent.com/99361267/167311678-4d3d0f95-0811-4142-a5c8-ac0248f3b858.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Here this product has 0 in stock and unavailable. Later after editing as<br>adding 10 more stock we see that is aging available<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 5: </em> Briefly explain the code process/flow</td></tr>
<tr><td> <em>Response:</em> <p>If the admin wanted to change any of the changes he show login<br>with admin login<br>once it is successful he can edit the details<br>for example if<br>the product prize or stock needs to modify he will click that product<br>do necessary actions and  save them<br>then products table will be updated <br><br><br></p><br></td></tr>
<tr><td> <em>Sub-Task 6: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/SaiDarshiniNannapuraju/is601-004/pull/14">https://github.com/SaiDarshiniNannapuraju/is601-004/pull/14</a> </td></tr>
<tr><td> <em>Sub-Task 7: </em> Add a direct link to the related file from Google Cloud</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/SaiDarshiniNannapuraju/is601-004/pull/14">https://github.com/SaiDarshiniNannapuraju/is601-004/pull/14</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 5: </em> Product Details Page </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot showing the button (clickable item) that directs the user to the Product Details Page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/99361267/167472156-85412422-b540-4af3-bd8f-adad312e89a7.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Link is provided below product image<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot showing the result of the Product Details Page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/99361267/167471828-ea1d5c38-fcc2-40ae-86f6-f966a421e28c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Provided a link below product image by clicking it will direct us to<br>product details page<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain the code process/flow</td></tr>
<tr><td> <em>Response:</em> <p>Once the user clicks on the view product details<br>based on the uniq URLgenerated<br>will fetch complete details and show using the &quot;shop/product/detail.html&quot; template<br></p><br></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/SaiDarshiniNannapuraju/is601-004/pull/14">https://github.com/SaiDarshiniNannapuraju/is601-004/pull/14</a> </td></tr>
<tr><td> <em>Sub-Task 5: </em> Add a direct link to the related file from Google Cloud (can be any specific item)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/SaiDarshiniNannapuraju/is601-004/pull/14">https://github.com/SaiDarshiniNannapuraju/is601-004/pull/14</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 6: </em> Add to Cart </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot of the success message of adding to cart</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/99361267/167472663-58d0d1d5-2916-4d9a-91aa-3a4c9b8fa731.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Once user clicks on the add to cart to see the items in<br>cart we show products added to cart<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot of the error message of adding to cart (i.e., when not logged in)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/99361267/167472663-58d0d1d5-2916-4d9a-91aa-3a4c9b8fa731.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>While developing got error could not maintain them<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add a screenshot of the Cart table with data in it</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/99361267/167473232-3eeabece-1493-4994-9acf-b55a88e70515.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Table format of adding cart items<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Tell how your cart works (1 cart per user; multiple carts per user)</td></tr>
<tr><td> <em>Response:</em> <p>We are storing all the products added and showing them to users when<br>required <br></p><br></td></tr>
<tr><td> <em>Sub-Task 5: </em> Explain the process of add to cart</td></tr>
<tr><td> <em>Response:</em> <p>Once the user visits the product details page <br>Provided &quot;Add to cart&quot; button<br>once clicked we add them to cart<br>show to the user when required <br></p><br></td></tr>
<tr><td> <em>Sub-Task 6: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/SaiDarshiniNannapuraju/is601-004/pull/14">https://github.com/SaiDarshiniNannapuraju/is601-004/pull/14</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 7: </em> User will be able to see their Cart </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot of the Cart View (show subtotal, total, and the link to Product Details Page)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/99361267/167473856-548e89da-325e-4a95-abb2-16a1d155f0ad.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Listing all cart products added<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Explain how the cart is being shown from a code perspective along with the subtotal and total calculations</td></tr>
<tr><td> <em>Response:</em> <p>We calculate the total by the cost of the product multiplied with quantity<br>Add<br>all of them and show sub total<br></p><br></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/SaiDarshiniNannapuraju/is601-004/pull/14">https://github.com/SaiDarshiniNannapuraju/is601-004/pull/14</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Add a direct link to the related file from Google Cloud</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/SaiDarshiniNannapuraju/is601-004/pull/14">https://github.com/SaiDarshiniNannapuraju/is601-004/pull/14</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 8: </em> User can update cart quantity </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Show a before and after screenshot of Cart Quantity update</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/99361267/167474205-7169dfa1-2c4d-4c49-af87-cdd0a14bc402.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>after changing quantity user need to update it<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Show a before and after screenshot of setting Cart Quantity to 0</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/99361267/167474674-73e6dc7b-71f6-4c27-9957-45b2c0126c6d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>We can remove product from cart by clicking remove instead of product with<br>quanttiy 0<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Show how a negative quantity is handled</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/99361267/167474468-d28e4a16-0b66-4165-a1d7-c96fcdfcd963.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>We did not give plus button we provided drop down with quantity start-with<br>1 by default<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Explain the update process including how a value of 0 and negatives are handled</td></tr>
<tr><td> <em>Response:</em> <p>We did not give an option for the user to select 0 of<br>a negative value for the quantity<br>instead, we provided a remove button and the<br>quantity dropdown starts with 1 <br></p><br></td></tr>
<tr><td> <em>Sub-Task 5: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/SaiDarshiniNannapuraju/is601-004/pull/14">https://github.com/SaiDarshiniNannapuraju/is601-004/pull/14</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 9: </em> Cart Item Removal </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a before and after screenshot of deleting a single item from the Cart</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/99361267/167473856-548e89da-325e-4a95-abb2-16a1d155f0ad.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Cart with two item<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/99361267/167474674-73e6dc7b-71f6-4c27-9957-45b2c0126c6d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Cart with one item after deleting an item<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a before and after screenshot of clearing the cart</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/99361267/167475134-09043723-c54a-4b5b-b123-3c0bed541e20.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Cart with no products<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain how each delete process works</td></tr>
<tr><td> <em>Response:</em> <p>When the user deletes an item from the cart we remove it from<br>his cart</p><br><br></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add related pull request link(s)</td></tr>
<tr><td> <em>Response:</em> <p><a href="https://github.com/SaiDarshiniNannapuraju/is601-004/pull/14">https://github.com/SaiDarshiniNannapuraju/is601-004/pull/14</a><br></p><br></td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-004-S22/is601-milestone-2-shop-project/grade/sn745" target="_blank">Grading</a></td></tr></table>
