# Inventory_Management

Inventory Management Web Application
The goal is to create a web application using the Flask framework to manage the
inventory of a list of products in respective warehouses. Imaging this application will be
used in a shop or a warehouse that needs to keep track of various products and various
locations.
The application should cover the following functionalities:
Database Tables:
● Product (product_id)
● Location (location_id)
● ProductMovement (movement_id, timestamp, from_location, to_location, product_id,
qty)
Note:
1. Primary keys can be text / varchar
2. Any one, or both of from_location and to_location can be filled. If you want to move
things into a location, from_location will be blank, if you want to move things out, then
to_location will be blank.
Views:
● Add/Edit/View Product
● Add/Edit/View Location
● Add/Edit/View ProductMovement
Report:
● Balance quantity in each location Use Cases:
● Create 3/4 Products
● Create 3/4 Locations
● Make ProductMovements

● Move Product A to Location X
● Move Product B to Location X
● Move Product A from Location X to Location Y
● (make 20 such movements)
● Get product balance in each Location in a grid view, with 3 columns:
Product, Warehouse, Qty
