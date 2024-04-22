Project Objective: Develop a web-based billing system that enables an administrator to add items to a product list and then select from those items to generate bills for customers.

Requirements:
Admin Item Management: The system must allow an administrator to add, edit, and delete items in the product list. Each item should include relevant details such as name, price, and description.

Bill Generation: The system must allow the administrator to select multiple items from the product list to create a bill. The bill should automatically calculate the total cost based on the selected items.

Technology: The project can be developed using any web technologies for both front-end and back-end development. The choice of technology should be based on ease of implementation, performance, and scalability.

Timeframe: The initial version of the system must be completed within one hour. This version should include the basic functionality for item management and bill generation.

User Interface: The system should have a user-friendly interface for easy navigation and use by the administrator. It should be responsive and accessible from various devices including desktops, laptops, and tablets.

Security: Implement basic security measures to protect the system and data, including secure login for the administrator.
Outcome: The project aims to create a functional and efficient billing system that simplifies the process of managing products and generating bills, thereby improving operational efficiency for businesses or individual users.


# To start this application

- Clone the repo

```
git clone https://github.com/Dhruv97Sharma/product-billing-system.git
```

- Run command for django app starting

```
python manage.py runserver
```

- Go to the urls http://localhost:8000/products/ and use the application to calculate product prices

- Access the admin from here - http://localhost:8000/admin/ after creating a superuser to test this