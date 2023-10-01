
# Devify

Devify is a dynamic platform where developers can showcase their projects, demonstrate their skills, review others' work, and engage with a thriving developer community. 

![](https://github.com/DeveshYadav13/Devify/blob/master/devplay.gif)

## Demo

To get a glimpse of Devify's features, check out the demo video: [Demo Video](https://www.youtube.com/watch?v=Wpz5RrVUReM)

## Features

- **CRUD Functionality:**
  - Implemented CRUD (Create, Read, Update, Delete) operations, enabling users to manage their projects and data efficiently using Python and Django models.

- **User Authentication:**
  - Utilized Django for user authentication, providing secure login and password reset features.
  - Implemented access control through Django decorators to restrict unauthorized access.

- **Advanced Search and Pagination:**
  - Added a powerful search functionality using Django Filter, allowing users to easily discover projects matching their interests.
  - Enhanced user experience with pagination using Django Paginator, improving the navigation of project listings.

- **REST API Integration:**
  - Developed a RESTful API using Django Rest Framework (DRF) to serve project data.
  - Serialized the data using DRF serializers, ensuring efficient data exchange.
  - Incorporated user authentication via JSON Web Tokens (JWT) for secure API access.

- **Database Integration:**
  - Connected the Django application seamlessly with a PostgreSQL database.
  - Deployed the application on Heroku with Heroku Postgres, ensuring data persistence and reliability.

## Getting Started

To run Devify locally or contribute to its development, follow these steps:

1. Clone this repository to your local machine.

2. Set up a virtual environment and install the required Python packages.

   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt

3. Run the development server.

    ```bash
   python manage.py runserver

4. Access Devify in your web browser at http://localhost:8000 and start exploring.


## Contributing

I welcome contributions to enhance Devify. Feel free to open issues, suggest improvements, or submit pull requests to make this platform even better.

## Credits

Created with ❤️ by [Devesh Yadav](https://github.com/DeveshYadav13).
