# Travel Blog | Testing

Return to [README](README.md)
- - -
Comprehensive testing has been performed to ensure the website's seamless and optimal functionality.

## Table of Contents
### [Responsiveness Testing](#responsiveness-testing-1)
### [Browser Compatibility Testing](#browser-compatibility-testing-1)
### [Device Testing](#device-testing-1)
### [Code Validation](#code-validation-1)
* [HTML Validation](#html-validation)
* [CSS Validation](#css-validation)
* [JavaScript Validation](#javascript-validation)
* [Python](#python)
### [Lighthouse Report](#lighthouse-report-1)
### [Bugs](#bugs-1)
* [Resolved Bugs](#resolved-bugs)
* [Unresolved Bugs](#unresolved-bug)
### [Features Testing](#features-testing-1)
---

## Responsiveness Testing

The deployed website underwent rigorous testing on multiple devices and screen sizes to ensure its responsiveness and adaptability. Developer Tools were utilized to simulate various screen sizes, enabling thorough examination of how the website behaves across different devices. Bootstrap classes and media queries were implemented to achieve the desired design, ensuring that the website maintains its visual and functional integrity on all platforms, enhancing the user experience.

![Am I Responsive](accounts/static/images/responsive.jpg)

## Browser Compatibility Testing

The project was tested on multiple web browsers to check for compatibility issues and ensure it functions as expected across all of them. This testing process guarantees a smooth and consistent user experience, regardless of the browser used.

<details>
<summary> Chrome
</summary>

![Chrome](accounts/static/images/chrome.jpg)
</details>

<details>
<summary> Microsoft Edge
</summary>

![Microsoft Edge](accounts/static/images/edge.jpg)
</details>

<details>
<summary> Opera
</summary>

![Opera](accounts/static/images/opera.jpg)
</details>

<details>
<summary> Firefox
</summary>

![Firefox](accounts/static/images/firefox.jpg)
</details>

<details>
<summary> Samsung Internet (Mobile)
</summary>

![Samsung Internet Mobile](accounts/static/images/mobile.jpg)
</details>

## Device Testing

Device testing was conducted on a variety of phone models, including Samsung Galaxy, iPhone and Sony. The assistance of family members and friends was sought to perform the testing. This comprehensive approach ensured that the website was thoroughly evaluated on different devices and platforms, contributing to a more robust and user-friendly final product.

## Code Validation

### HTML Validation

<details>
<summary> Home Page
</summary>

![Home Page](accounts/static/images/htmlcheckhome.jpg)
</details>

<details>
<summary> Register Page
</summary>

![Register Page](accounts/static/images/htmlcheckregister.jpg)
</details>

<details>
<summary> Login Page
</summary>

![Login Page](accounts/static/images/htmlchecklogin.jpg)
</details>

<details>
<summary> Logout Page
</summary>

![Logout Page](accounts/static/images/htmlchecklogout.jpg)
</details>

<details>
<summary> Category Page
</summary>

![Category Page](accounts/static/images/htmlcheckcategory.jpg)
</details>

<details>
<summary> Add Post Page
</summary>

![Add Post Page](accounts/static/images/htmlcheckaddpost.jpg)
</details>

<details>
<summary> Add Category Page
</summary>

![Add Category Page](accounts/static/images/htmlcheckaddcategory.jpg)
</details>

<details>
<summary> View Post Page
</summary>

![View Post Page](accounts/static/images/htmlcheckarticledetail.jpg)
</details>

<details>
<summary> Edit Post Page
</summary>

![Edit Post Page](accounts/static/images/htmlcheckeditpost.jpg)
</details>

<details>
<summary> Delete Post Page
</summary>

![Delete Post Page](accounts/static/images/htmlcheckdeletepost.jpg)
</details>

<details>
<summary> Add Comment Page
</summary>

![Add Comment Page](accounts/static/images/htmlcheckaddcomment.jpg)
</details>

<details>
<summary> Category Doesn't Exist Page
</summary>

![Category Doesn't Exist Page](accounts/static/images/htmlchecknocategory.jpg)
</details>

### CSS Validation

<details>
<summary> Custom CSS (style.css)
</summary>

![Custom CSS (style.css)]()
</details>

### JavaScript Validation

<details>
<summary> Custom JS (script.js)
</summary>

![Custom JS (script.js)]()
</details>

### Python

#### travel app

<details>
<summary> admin.py
</summary>

![admin.py](accounts/static/images/travelappadmin.jpg)
</details>

<details>
<summary> forms.py
</summary>

![forms.py](accounts/static/images/travelappforms.jpg)
</details>

<details>
<summary> models.py
</summary>

![models.py](accounts/static/images/travelappmodels.jpg)
</details>

<details>
<summary> views.py
</summary>

![views.py](accounts/static/images/travelappviews.jpg)
</details>

<details>
<summary> urls.py
</summary>

![urls.py](accounts/static/images/travelappurls.jpg)
</details>

#### travelblog project

<details>
<summary> settings.py
</summary>

![settings.py](accounts/static/images/travelblogsettings.jpg)
</details>

<details>
<summary> urls.py
</summary>

![urls.py](accounts/static/images/travelblogurls.jpg)
</details>

## Lighthouse Report

<details>
<summary> Home Page
</summary>

![Home Page](documentation/lighthouse_report/home-lighthouse.PNG)
</details>

<details>
<summary> Home Page Logged in
</summary>

![Home Page Logged in](documentation/lighthouse_report/home-logged-lighthouse.PNG)
</details>

<details>
<summary> Contact Page
</summary>

![Contact Page](documentation/lighthouse_report/contact-lighthouse.PNG)
</details>

<details>
<summary> Sign Up Page
</summary>

![Sign Up Page](documentation/lighthouse_report/sign-up-lighthouse.PNG)
</details>

<details>
<summary> Login Page
</summary>

![Login Page](documentation/lighthouse_report/login-lighthouse.PNG)
</details>

<details>
<summary> Logout Page
</summary>

![Logout Page](documentation/lighthouse_report/logout-lighthouse.PNG)
</details>

<details>
<summary> Browse Cabins Page
</summary>

![Browse Cabins Page](documentation/lighthouse_report/browse-cabins-lighthouse.PNG)
</details>

<details>
<summary> Make a Booking Page
</summary>

![Make a Booking Page](documentation/lighthouse_report/make-a-booking-lighthouse.PNG)
</details>

<details>
<summary> Booking Success Page
</summary>

![Booking Success Page](documentation/lighthouse_report/booking-succesful-lighthouse.PNG)
</details>

<details>
<summary> Booking Overview Page
</summary>

![Booking Overview Page](documentation/lighthouse_report/booking-overview-lighthouse.PNG)
</details>

<details>
<summary> Edit Booking Page
</summary>

![Edit Booking Page](documentation/lighthouse_report/edit-booking-lighthouse.PNG)
</details>

<details>
<summary> Delete Booking Page
</summary>

![Delete Booking Page](documentation/lighthouse_report/delete-booking-lighthouse.PNG)
</details>

## Bugs

### Resolved Bugs

#### Categories not working properly.

* When I made a blogpost in a category and pressed on the category to see the posts in that category I got the error message "this category doesn't exist". This was because when creating categories I spelled them with capital letters while the code was looking for the url with lower case letters. I solved this by changing the name of the categories to lower letters.

#### User name not showing in blog posts.

* When creating a new blog post as a normal user their name didn't appear on the homepage after the category name. This was because when creating a normal user I only specified their first name and not last name. I changed the code to: post.author.get_full_name to solve this issue.

### Unresolved Bug

* There are no unresolved bugs.

## Features Testing

![feature.testing](accounts/static/images/featuretesting.jpg)

Return to [README](README.md)