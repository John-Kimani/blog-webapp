
# Blog Web App
This application enables user/(s) to view, random quotes, blog posts and are able to leave their comment/(s) on blog posts.

# App screenshot
![Blog-WebApp](/app/static/images/blogwebapp.png)
## Installation

Guide to install Blog APP application:

### Clone this repository
```bash
 git clone https://github.com/John-Kimani/blog-webapp.git
```
* Move into the cloned directory:
```bash
cd blog-webapp
```
* Create and activate your virtual environment:
```bash
mkvirtualenv virtual
```
* Install project dependancies within your active environment: (Read: requirements.txt and use command below)
```bash
(virtual)$ pip3 Install -r requirements.txt
```
* Environment variables:
    *  Create a file called ```.env``` in the root folder
    ```bash
    (virtual)$ touch .env
    ```
    * Add the following lines to the file as seen in ```.env-template```
    ```bash 
    SECRET_KEY=
    DATABASE_URL=
    ```
* Start the flask server
```bash
(Virtual)$ flask run
```
* or

```bash
(Virtual)$ python3 run.py
```
## Features and BDD

- Users are able to create user profile and login to their profiles.


## Technology Used

**Framework:** Flask
**Language** Python

### Developed with
**Structure:** Bootstrap, HTML
**Styles:** CSS

## Author

* Design and developed by: [John Kimani](https://github.com/John-Kimani)