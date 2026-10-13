\# Flask and MongoDB Assignment — Pratheesh Babu



\## Project Overview



This project demonstrates a Flask web application integrated with MongoDB Atlas.



\### Features



\- `/api` reads data from `data.json` and returns a JSON response.

\- A web form accepts a name, email address, and message.

\- Submitted form data is stored in MongoDB Atlas.

\- Successful submissions redirect to a page displaying \*\*Data submitted successfully\*\*.

\- Validation and database errors are displayed on the form page without redirecting.



\## Technologies Used



\- Python

\- Flask

\- MongoDB Atlas

\- PyMongo

\- HTML

\- python-dotenv



\## Project Structure



```text

Flask\_and\_MongoDB\_PratheeshBabu/

├── app.py

├── data.json

├── .env.example

├── .gitignore

├── README.md

├── requirements.txt

├── templates/

│   ├── index.html

│   └── success.html

├── static/

└── screenshots/

```



\## Setup Instructions



1\. Install Python.

2\. Create and activate a virtual environment.

3\. Install dependencies using `pip install -r requirements.txt`.

4\. Create a local `.env` file using `.env.example` as a template.

5\. Configure the MongoDB Atlas connection string and database name in `.env`.

6\. Run the application using `python app.py`.

7\. Open `http://127.0.0.1:5000/` in a browser.

8\. Open `http://127.0.0.1:5000/api` to test the JSON API.



\## MongoDB Configuration



The application uses the `flask\_mongodb\_assignment` database and the `form\_submissions` collection.



Configure your own MongoDB Atlas connection string in the local `.env` file. Do not publish database credentials.



\## Testing Evidence



The `screenshots` folder contains evidence of the API response, successful form submission, MongoDB record, and error handling.



\## GitHub Repository



Repository link: Add the GitHub repository URL here after creating the repository.



\## Author



Pratheesh Babu

