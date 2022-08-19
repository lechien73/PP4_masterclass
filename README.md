![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

# Building a Better Blog

This is the *I Blog Therefore I Am* walkthrough project updated with the following major features:

* Uses WhiteNoise instead of Cloudinary static storage (Cloudinary is still used for images)
* Reverts to function-based views instead of class-based
* Adds full CRUD functionality to comments. Logged-in users can edit or delete their comments
* Adds a simple "About" app to show how more than one Django app can be used in a project
* The apps are tested with Django's unit tests

The following minor updates have been added too:

* Removes the dependency on an externally-hosted placeholder image
* Adds dynamic "active" links to the navbar using template variables
* Added the functionality to use SQLite for tests
