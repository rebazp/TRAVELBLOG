# Rebaz Travel Blog

Join Rebaz on his travels and discuss where to go next! This Django based blog allows users to create their own account so that they
can leave blog posts, comments and likes. This simple and easy to use blog is for the creator and users to share travel tips and memories.

![Home Screen](accounts/static/images/responsive.jpg)

[View Rebaz Travel Blog live website here](https://rebazptravelblog-3e0a8b8b8d3b.herokuapp.com/)
---

## Table of Contents
### [User Experience](#user-experience-ux)
* [Project Goals](#project-goals)
* [Agile Methodology](#agile-methodology)
* [Target Audience](#target-audience)
* [First time user](#first-time-user)
* [Registered user](#registered-user)
* [Admin user](#admin-user)
### [Design](#design-1)
* [Color Scheme](#color-scheme)
* [Images](#cabin-images)
* [Typography](#typography)
* [Wireframes](#wireframes)
* [Data Model](#data-models)
* [User Journey](#user-journey)
* [Database Scheme](#database-scheme)
### [Security Features](#security-features-1)
### [Features](#features-1)
* [Existing Features](#existing-features)
* [Features Left to Implement](#features-left-to-implement)
### [Technologies Used](#technologies-used-1)
* [Languages Used](#languages-used)
* [Databases Used](#databases-used)
* [Frameworks Used](#frameworks-used)
* [Programs Used](#programs-used)
### [Deployment and Local developement](#deployment-and-local-developement-1)
* [Local Developement](#local-developement)
* [ElephantSQL Database](#elephantsql-database)
* [Cloudinary](#cloudinary)
* [Heroku Deployment](#heroku-deployment)
### [Testing](#testing-1)
### [References](#references-1)
* [Docs](#docs)
* [Content](#content)
* [Acknowledgments](#acknowledgments)
---

## User Experience (UX)

Join in on simple to use travel blog and share travel memories and tips. No advance UI or features, instead easy to read and use blog with just the necessary functions. Interact with your own blog posts, comments and like/unlike posts. 

### Project Goals

The goal with this project is to share traveltips and memories through text and pictures.

### Agile Methodology

Agile Methodology was used to help prioritize and organize tasks, writting the user stories and using project boards on github. Template was created to help write user stories and epics.

* Epics were written containing possible user stories and based on that the blog was made.
* User stories were created by looking at epics and through iterations the project was advancing.
* Project board is set to public.
* Project board was used to track progression of the task through the todo, in progress and done columns.
* Labels were added to sort the issues based on the importance.

<details>
<summary> User Stories Template
</summary>

![User Stories Template](accounts/static/images/issuetemplate.jpg)
</details>

<details>
<summary> User Stories, Issues
</summary>

![User Stories, Issues](accounts/static/images/issues.jpg)
</details>

<details>
<summary> Project Board
</summary>

![Project Board](accounts/static/images/projectboard.jpg)
</details>

### User Stories

#### Epics
1. User interaction with posts
2. User engagement with content
3. Account management
4. Content creation and management

#### User Stories
1. View paginated list of posts
* Given more than one post in the database, these multiple posts are listed
* When a user opens the main page a list of posts is seen
* Then the user sees all post titles with pagination to choose what to read
2. Open a post
* When a blog post title is clicked on a detailed view of the post is seen
3. View comments
* Given one or more user comments the admin can view them
* Then a site user can click on the comment thread to read the conversation
4. Account registration
* Given an email a user can register an account
* Then the user can log in
* When the user is logged in they can comment
5. Comment on post
* When a user comment is approved
* Then a user can reply
* Given more than one comment then there is a conversation thread
6. Modify or delete comment on a post
* Given a logged in user, they can modify their comment
* Given a logged in user, they can delete their comment
7. Manage posts
* Given a logged in user, they can create a blog post
* Given a logged in user, they can read a blog post
* Given a logged in user, they can update a blog post
* Given a logged in user, they can delete a blog post
8. Create drafts
* Given a logged in user, they can save a draft blog post
* Then they can finish the content at a later time
9. Likes
* Given one or more user likes the user / admin can view them

Detailed look can be found in the [project board](https://github.com/users/rebazp/projects/6)

### Target Audience

* People seeking travel tips
* People seeking to share travel tips

### First time user

* Simple and intuitive blog with easy navigation.
* Easy Registration process.
* Simple to use on any device.

### Registered User

* Seamless login process with a secure and personalized user account.
* Browsing through categories and see related posts and comments. 
* Give comments likes and dislikes.
* Create new categories.

### Admin user

* Secure and separate login portal for admin users with appropriate access control.
* Access to an admin dashboard for managing users, posts, comments and likes/dislikes.
* Ability to add, edit, or delete user, posts, comments likes/dislikes.

## Design

The travel blog uses a easy to read and navigate layout with only the necessary functions. The dropdown navbar with categories is only accessible in on the homepage to keep the layout clean and easy to use. 

### Color Scheme

* White background with blue text.
* Blue and red like/dislike buttons.

### Images

All images used in blog posts are taken from google search.

### Typography

The 'Lora' font is specified as the primary font, and the 'Domine' font is specified as a fallback font.

### Wireframes

<details>
<summary> Home page
</summary>

![Home Page](accounts/static/images/wireframehomepagelogout.jpg)
</details>

<details>
<summary> Home page when logged in
</summary>

![Home page when logged in](accounts/static/images/wireframehomepagelogin.jpg)
</details>

<details>
<summary> Login page
</summary>

![Login page](accounts/static/images/wireframeloginpage.jpg)
</details>

<details>
<summary> Register page
</summary>

![Register page](accounts/static/images/wireframeregisterpage.jpg)
</details>

<details>
<summary> Add post page
</summary>

![Add post page](accounts/static/images/wireframeaddpost.jpg)
</details>

<details>
<summary> Add comment page
</summary>

![Add comment page](accounts/static/images/wireframeaddcomment.jpg)
</details>

<details>
<summary> Add category page
</summary>

![Add category page](accounts/static/images/wireframeaddcategory.jpg)
</details>