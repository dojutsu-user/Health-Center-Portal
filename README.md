# Health Center Portal

![Travis (.org) branch](https://img.shields.io/travis/dojutsu-user/Health-Center-Portal/master)
[![codecov](https://codecov.io/gh/dojutsu-user/Hostel-Booking-Portal/branch/master/graph/badge.svg)](https://codecov.io/gh/dojutsu-user/Hostel-Booking-Portal)


This is a health center portal for managing a health center for a college.

## Table Of Contents

- [Features](#features)
- [Setup](#setup)
  * [Starting The Local Server](#sub-heading)
  * [Loading The Demo Data]()
  * [Running The Tests]()
- [Project Specific Settings]()
  * [Change Max Upload Limit Of Display Picture For Doctors]()
  * [Add/Remove Allowed Domains For Login/SignUp]()
  * [Change Logo Of The Website]()
- [Guides]()
  * [How To Setup Permissions For Staff]()'
  * [How To Add A Doctor]()
  * [How To Add A Visit History]()
- [Screenshots]()

## Features

- Patient History Maintenance.
- Medicines' Stock Maintenance.
- Appointment Bookings/Cancellations.
- Patient's Profile Visible To Each Doctor.
- Doctor's Profile.
- Announcements.
- Different Dashboards For Patients/Staff/Doctors.
- Minimal And Responsive UI.

## Setup

### Starting The Local Server

1. Make sure that you have `Docker` and `docker-compose` installed. If not, you can install it by following their documentations: [docs.docker.com](https://docs.docker.com/).

2. Clone this repository:
	```
    git clone https://github.com/dojutsu-user/Health-Center-Portal.git
    ```
3. Change working directory to project root directory:
	```
    cd Health-Center-Portal/
    ```
4. Run the following command:
	```
    docker-compose -f dockerfiles/docker-compose.dev.yml up --build
    ```
5. Local server will start at [http://0.0.0.0:8000/](http://0.0.0.0:8000/).

### Loading The Demo Data

1. If you want to load the dummy data, you can do so by running the following command:
	```
    docker-compose -f dockerfiles/docker-compose.dev.yml run web ./scripts/load_all_fixtures.sh
    ```
### Running The Tests

1. For running tests with Python 3.7:
	```
    docker-compose -f dockerfiles/docker-compose.dev.yml run --no-deps --rm --entrypoint dockerfiles/docker-entrypoint.test.sh -e PYTHON_VERSION=3.7 web
    ```
2. For running tests with Python 3.8:
	```
    docker-compose -f dockerfiles/docker-compose.dev.yml run --no-deps --rm --entrypoint dockerfiles/docker-entrypoint.test.sh -e PYTHON_VERSION=3.8 web
    ```

## Project Specific Settings

### Change Max Upload Limit Of Display Picture For Doctors

1. If you want to change the max upload size of display picture for doctors, then you can do so by changing value of the variable `MAX_ALLOWED_IMAGE_SIZE_IN_MB` in `settings.py`. Note that the value is in `MB`.

### Add/Remove Allowed Domains For Login/SignUp.

1. If you want to restrict the domains with which users can signin or signup, you can do so by adding your own domain in `ALLOWED_EMAIL_DOMAINS_FOR_SIGNUP` in `settings.py`. By default, `@iiitl.ac.in` is added.

### Change Logo Of The Website

1. Change the logo of the website by replacing `logo.png` located at `static/theme/images/logo.png`. Size of the new logo should be same as the previous logo which is `636 x 144 pixels`.

## Guides

### How To Setup Permissions For Staff

1. Make sure the local server is up and running.
2.	Go to [0.0.0.0:8000/admin/](http://0.0.0.0:8000/admin/) and login with superuser credentials.
3.	Go to `Groups`. If you load the dummy data, then there should be a group called `Staff Members`. If not, click on `Add Group` (top right) and enter the name of the group as `Staff Members` and choose the following permissions:
    - announcements | announcement | Can add announcement
    - announcements | announcement | Can change announcement
    - announcements | announcement | Can delete announcement
    - announcements | announcement | Can view announcement
    - auth | user | Can change user
    - medicines | medicine | Can add medicine
    - medicines | medicine | Can change medicine
    - medicines | medicine | Can delete medicine
    - medicines | medicine | Can view medicine
    - student | medicine given history | Can add medicine given history
    - student | medicine given history | Can change medicine given history
    - student | medicine given history | Can delete medicine given history
    - student | medicine given history | Can view medicine given history
    - student | visit history | Can add visit history
    - student | visit history | Can change visit history
    - student | visit history | Can delete visit history
    - student | visit history | Can view visit history
4. Click on `Save`.
5. Then you can go to `Users` and can assign any user to the group just created and that user will have separate dashboard to do its required tasks.

### How To Add A Doctor

1. Add a new user by going here: [0.0.0.0:8000/admin/auth/user/add/](http://0.0.0.0:8000/admin/auth/user/add/)
2. Then go to [0.0.0.0:8000/admin/doctor/doctor/add/](http://0.0.0.0:8000/admin/doctor/doctor/add/) and select the user just created and fill the other fields and click on `Save`.
3. The doctor can login with the username and password used in step 1 and can then login in its dashboard and can edit its details manually.

### How To Add A Visit History

1. Go to [0.0.0.0:8000/admin/student/visithistory/add/](http://0.0.0.0:8000/admin/student/visithistory/add/) and select the and doctor from the list and fill out the other details and click on `Save`.
2. This will be visible to the patient as well as the doctors.

## Screenshots

<details><summary>Homepage</summary>
<p>

![Homepage](https://i.postimg.cc/HnB29jVM/homepage.png)

</p>
</details>

<details><summary>Available Doctors</summary>
<p>

![Available Doctors](https://i.postimg.cc/0QGZrVvc/list-of-available-doctors.png)

</p>
</details>

<details><summary>About Page</summary>
<p>

![About Page](https://i.postimg.cc/WpnXvYX4/about-page.png)

</p>
</details>

<details><summary>Login Page</summary>
<p>

![Login Page](https://i.postimg.cc/cHGXsVpv/login-page.png)

</p>
</details>

<details><summary>Student's Dashboard</summary>
<p>

![Student Dashboard](https://i.postimg.cc/QdPfzBSk/student-dashboard.png)

</p>
</details>

<details><summary>Doctor's Dashboard</summary>
<p>

![Doctor's Dashboard](https://i.postimg.cc/7L2KrxWv/doctor-dashboard.png)

</p>
</details>

<details><summary>Staff Dashboard</summary>
<p>

![Staff Dashboard](https://i.postimg.cc/cL6DT77L/staff-dashboard.png)

</p>
</details>
