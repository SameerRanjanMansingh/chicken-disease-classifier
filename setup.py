import setuptools

with open("README.md","r", encoding="utf-8") as f:
    long_description = f.read()


__version__  = "0.0.0"

REPO_NAME = "chicken-disease-classifier"
AUTHOR_USER_NAME = "SameerRanjanMansingh"
<<<<<<< HEAD
SRC_REPO = "cnnClassifier"
=======
SRC_REPO = "chicken-disease-classifier"
>>>>>>> 86115ac4a0b177cda42c7c60a03d18b9e678a904
AUTHOR_EMAIL = "sameerranjan0367@gmail.com"


setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for CNN app",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
<<<<<<< HEAD
    package_dir={"": "src"},
=======
    package_dir={"", "src"},
>>>>>>> 86115ac4a0b177cda42c7c60a03d18b9e678a904
    packages=setuptools.find_packages(where="src")
)