![Python package](https://github.com/jacknely/DocumentPortal/workflows/Python%20package/badge.svg)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
![Docker Image CI](https://github.com/jacknely/DocumentPortal/workflows/Docker%20Image%20CI/badge.svg)
![Python application](https://github.com/jacknely/DocumentPortal/workflows/Python%20application/badge.svg)
# DocumentPortal

## Requirements
- Python 3
- Docker
- Flask==1.1.1
- Flask-SQLAlchemy==2.4.1

Install from requirements.txt


## Usage
In the root directory execute the below code:
```
docker-compose up
```
Navigate to localhost in browser with container running

### Upload files
Submit form on index.html with file.

### View Files
With container running, navigate to the below address:
```
localhost:5000/files
```
