# Shelf Identification Project

## Overview

The "Shelf Identification" project is a Django-based application that provides two APIs:

1. **Default Page**: http://localhost:8000/
   - This is the default landing page for the project.

2. **Analyze API**: http://localhost:8000/analyze
   - This API is used to get the shape of products on a shelf.

## Getting Started

Follow these steps to build and run the "Shelf Identification" project using Docker.

### Prerequisites

Before you begin, make sure you have Docker installed on your system.Make sure you should activate your docker in background

### Build the Docker Image

1. Open a terminal or command prompt.

2. Extract the project folder and navigate to the directory containing your project files and the Dockerfile. 

3. Build the Docker image using the following command:

   ```
   docker build -t assignment:latest .
   ```

   Replace `assignment` with the desired image name and `latest` with the desired tag.

### Run the Docker Container

1. After successfully building the Docker image, you can run a Docker container from it using the following command:

   ```
   docker run -p 8000:8000 assignment:latest
   ```

   Replace `assignment:latest` with the image name and tag you used during the build.

2. The Django development server will start inside the Docker container, and the application will be accessible at http://localhost:8000/ in your web browser.

### Access the APIs

- Default Page: http://localhost:8000/
   - This is the default landing page for the project.

- Analyze API: http://localhost:8000/analyze
   - Use this API to get the shape of products on a shelf.

Sure, I've added a section called "Example Shelf" to your README file. Here's the updated README:

---

# Shelf Identification Project

## Overview

The "Shelf Identification" project is a Django-based application that provides two APIs:

1. **Default Page**: http://localhost:8000/
   - This is the default landing page for the project.

2. **Analyze API**: http://localhost:8000/analyze
   - This API is used to get the shape of products on a shelf.

## Example Shelf

### Using Example Data

You can use example shelf data provided in the project folder to test the "Analyze" API.

1. In the project folder, you will find a file named `shelf_examples`. This file contains example data representing the products on a shelf.

2. To use this example data, make a POST request to the "Analyze" API (http://localhost:8000/analyze) with the example data, we can gwt desire output.
   Example use:
   ```
   {
    "grid": [
        ["G", "M", "N", "B"],
		  ["G", "M", "N", "B"],
		  ["G", "M", "N", "B"],
		  ["G", "M", "N", "B"]
    ]
   }
   ```
3. paste the above in the content space in the api and click post

4. The API will process the Test example data and return the shape information of the products on the shelf.

5. NOTE: Paste each test example one by one. 

5. you can use POSTMAN app to check this API key like use post method and paste grid in the body select as json.you can get output

### Stopping the Container

To stop the Docker container, you can press `Ctrl + C` in the terminal where it is running. To remove the container when you are done, use the `docker rm` command:

```
docker ps -a  # Find the container ID
docker rm <container-id>
```

### Manual Running of project

Without docker, you can run project. you much have python 3.10 or above in your pc/laptop

1. Extract the folder and navigate to the folder which contain, manage.py

2. create virtualenv within the directory using command prompt
   
   ```
   python -m venv venv
   ```
3. activate virtualenv and install requirements.txt to install required imports
   ```
   source venv/bin/activate
   ```

   ```
   pip install -r requirements.txt
   ```
4. run the project using the django command
   ```
   python manage.py runserver
   ```

5. navigate to localhost then you can see the result.

## Conclusion

You have successfully built and run the "Shelf Identification" project using Docker. You can now access the default page and use the "Analyze" API to retrieve product shape information.

---
