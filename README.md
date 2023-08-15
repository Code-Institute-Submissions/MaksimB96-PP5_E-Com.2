# Honey Haven

(Developer: Maksims Buraks)

![Mockup image](docs/am-i-responsive.png)

[live web-page](https://honeyhaven-236ab8f8ceba.herokuapp.com/)

## Table of contents

- [Honey Haven](#honey-have)
  - [Table of contents](#table-of-contents)
  - [Project Overview](#project-overview)
  - [Business Model](#business-model)
  - [Project Goals](#project-goals)
    - [User Goals](#user-goals)
    - [Site Owner Goals](#site-owner-goals)
  - [User Experience](#user-experience)
    - [Target Audience](#target-audience)
    - [User Requirements and Expectations](#user-requirements-and-expectations)
    - [User Stories](#user-stories)
      - [First-time User](#first-time-user)
      - [Returning User](#returning-user)
      - [Site Owner](#site-owner)
  - [Design](#design)
    - [Design Choices](#design-choices)
    - [Kanban-Board](#kanban-board)
    - [Colour](#colour)
    - [Fonts](#fonts)
    - [Structure](#structure)
    - [Wireframes](#wireframes)
  - [Tech Used](#tech-used)
    - [Languages](#languages)
    - [Tools](#tools)
  - [Features](#features)
    - [Logo and Nav-Bar](#logo-and-nav-bar)
    - [](#)
    - [Index](#index)
    - [Contact Form](#contact-form)
  - [Validation](#validation)
    - [HTML Validation](#html-validation)
    - [CSS Validation](#css-validation)
    - [Python Validation](#python-validation)
    - [JS Validation](#js-validation)
    - [Tests](#tests)
      - [Devices tested on on:](#devices-tested-on-on)
      - [Browser tested on on:](#browser-tested-on-on)
  - [Bugs](#Bugs)
  - [Deployment](#deployment)
  - [Future Features](#future-features)
  - [Credits](#credits)
    - [Media](#media)
    - [Code](#code)
  - [Acknowledgements](#acknowledgements)


## Project Overview

Welcome to Honey Haven, the one stop shop for everything related to natural honey as well as products! This project is essentially a proof of concept that will be worked on, and eventually become a fully fledged e-commerce store. Please note that while products at the moment are limited the end goal is to flesh it out once we determine exact products to be sold!

The website is a B2C and B2B model. It provides services to customers through shopping with a quick and easy pathway to purchase. User profiles display previous orders and the ability to save delivery info. The store also allows customers to subscribe to a news letter which in turn allows them to recieve emails updating them on new potential products and/or offers. There is a contact section that allows users to leave a message which will be displayed to the admin panel (future features will include a display of messages in the admin profile with a reply functionality)

Admins have the ability to edit/update and delete items. Full editing of the bag items for Users are also available.


## Business Model

# Facebook Page

This project utilizes a facebook page to increase the clients reach and influence. It is based in cavan so the target audience would be local but through marketing it would allow to expand it's reach further in Ireland!

![Facebook](docs/honey-haven-fb1.png)
![Facebook](docs/honey-haven-fb2.png)


## Project Goals

### User Goals

    -Finding a site that provides ability to book a one on one session
    -To Create Bookings
    -To Update Bookings
    -To Delete Bookings
    -To Manage Bookings
    -To Create Account

### Site Owner Goals

    -Provide a simple and appealing manner in which to shop
    -Provide an area to get in contact
    -To manage and send news

## User Experience

### Target Audience

    -Honey enthusiasts local to Ireland

### User Requirements and Expectations

    -A simple and natural way to navigate the website
    -Quick acessibility to relevant information
    -Quick acessibility to relevant products
    -Appealing design that responds accordingly
    -User Subscribe functionality
    -Detail view of products
    -Login functionality in order to get in contact
    

### User Stories

#### User


#### Site Owner

5


## Design

### Design Choices

Website design was inspired by a variety of e-com websites, with the focus of the user having a clear goal. Every section is easy to understand, website flow is easy and navigation is intuative. Path to purchase is made as easy as possible


### Kanban-Board

A kanban board was utilised to set specific goals that would aid agile development! For a detailed view of my goals please find it following the link:
<br>
<a href="https://github.com/users/MaksimB96/projects/7">Kanban Overview</a>

![Kanban Board](docs/kanban.png)


### ER Diagram
Please find the Entity relationship diagram utilized to bring the project to fruition!

![ER Diagram](docs/er.png)

### Colour

Colors used were the bootstrap bg dark with accents of grey and black and the main accent of yellow. These colors were chosen as all these tones play well together adding a layer of depth to the site while maintaining a minimal structure.
<br>

![Color Scheme](docs/colors.png)

### Fonts

Fonts used were Abril Fatface with a fall back of cursive for the majority of headings as well as Lato with a fall back of sans-serif which I found complements the playful design of Abril and adds nice contrasts, as well as allowing users to quickly pick up on the vital points of info.

### Structure

The Structure of the website is clear and concise. Bright colors draw in the user, I untilised the rule of thirds on the home page to make the overall flow pleasant, as well as not over crowding areas with text. The aim was simple and clear, and specific towards an audience interested in honey produce. Navigation is intuative, and the path to purchase is simple and not cluttered.

<br>

The website is made up of multiple pages:

    -The Index
    -The Products
    -The Product Detail
    -The Bag
    -Checkout Area
    -Checkout Success
    -User Profile (If authenticated)
    -News Segment (If super User)
    -Edit/Add segemt (If super User)
    -Allauth essentials

### Wireframes

<details><summary>Index</summary><img src="docs/wireframes/index-wf.png"></details>

<details><summary>Product View</summary><img src="docs/wireframes/products-wf.png"></details>

<details><summary>Product Detail</summary><img src="docs/wireframes/product-d-wf.png"></details>

<details><summary>Bag</summary><img src="docs/wireframes/bag-wf.png"></details>

<details><summary>Checkout</summary><img src="docs/wireframes/check-out-wf.png"></details>

<details><summary>Profile</summary><img src="docs/wireframes/profile-wf.png"></details>

<details><summary>Admin Edit/Add</summary><img src="docs/wireframes/admin-edit-wf.png"></details>

<details><summary>Admin News/Contact Form</summary><img src="docs/wireframes/admin-news-wf.png"></details>

<details><summary>Allauth all portals</summary><img src="docs/wireframes/allauth-wf.png"></details>


## Tech Used

### Languages

    -HTML
    -CSS
    -Java Script
    -Pyhton
    -Django
    

### Tools

    -Git
    -Git Hub
    -Git Pod
    -Figma
    -Google Fonts
    -Adobe Color Wheel
    -Font Awesome
    -Favicon.io
    -Circle Crop
    -postgresql
    -psycopg
    -Canva
    -Boot strap 4
    -pixelr
    -Django
    -Crispy Forms
    -panda_io
    -Amazon Web Services

## Features






## Validation

### HTML Validation
W3C mark-up was utilised in order to validate html of the website. All Pages pass with no errors. Warnings are related to various segments not using Headings, but utilise div elements.

<details><summary>Index</summary>
<img src="docs/validations/index-valid.png">
</details>

<details><summary>login</summary>
<img src="docs/validations/login-valid.png">
</details>

<details><summary>logout</summary>
<img src="docs/validations/logout-valid.png">
</details>

<details><summary>Manage</summary>
<img src="docs/validations/manage-valifd-html.png">
</details>

<details><summary>Sign-Up</summary>
<img src="docs/validations/sign-up-valid.png">
</details>

<details><summary>Delete</summary>
<img src="docs/validations/delete-valid-html.png">
</details>



<br>

### CSS Validation
W3C CSS validator was utilised in order to make sure the css code passes standards with no errors.

<details><summary>Full Document</summary>
<img src="docs/validation/css-valid.png">
</details>

<br>

### Python Validation

CI Python linter used here

<details><summary>Forms</summary>
<img src="docs/validation/forms-py.png">
</details>

<details><summary>Model</summary>
<img src="docs/validation/models-py.png">
</details>


<details><summary>View</summary>
<img src="docs/validation/views-py.png">
</details>

### JS Validation
JSHint validator was utilised in order to make sure the javascript code passes standards with no errors or warnings, All functions marked as "unused" are called on click in HTML code segments, images of relevnt code is attached to validations.

<details><summary>Email Js And Script</summary>
<img src="docs/validations/script.png">
<img src="docs/validations/sendEmail..png">
</details>

<br>

### Tests
-login/Crud Functionality functionality:
    <img src="docs/features/booking-created.png">
    <img src="docs/features/admin-confirm.png">
    <img src="docs/features/booking-delete.png">
    <img src="docs/features/sign-in.png">
    <img src="docs/features/sign-out.png">
    <img src="docs/features/admin-view.png">


#### Devices tested on on:
    -Iphone SE, XR, 11, 12, 14, 14 pro, samsung s5
    -Ipad
    -Macbook Pro/Air
    -Lenovo Platform
    -Dell Platform

#### Browser tested on on:
    -Chrome
    -Safari
    -Brave/Brave Mobile


### Bugs

During Development I ran in to a few bugs:

  Media Files not fully rendering even with proper aws deployment:

  -This was fixed by implementing a media context proccessor.

  Sorting and some categories did not work

  -This was fixed by getting rid of the base js in the extended templates

  Codeanywhere workspaces deletion.

  -The cause of this was unknown, however thanks to Sean we migrated back to gitpod which was a more reliable IDE

  Contact form server error.

  -This was simply due to the db not being fully integrated

3. Toast not

## Deployment

Honey Haven followed a multi-step deployment. The website was deployed as follows:

### GitHub

The process for github was as follows:
  -


## Future Features

There are a few more feartures that I would like to implement in the future. These Include:
1.User Unsubscribe functionality 
2.Rating System
3.Flesh out the products 
4.A Feedback Section/ Possibly rating system
5.Additional support through webkits for mozilla and other browsers


## Credits

### Media

Logo media created by me using  <a href="https://www.canva.com/">Canva</a>, this includes Icons and backgound images.
<br>
Any Icons used found on <a href="https://fontawesome.com/">Font Awesome</a>
<br>

# Images



    
### Code 

1. Product/bag/checkout/search logic inspired by : <a href="https://www.youtube.com/watch?v=3_3q_dE4_qs&t=649s">Code Institute Boutique Ado</a>
2. Preloader idea : <a href="https://www.youtube.com/watch?v=Yf5d_Zx3AaI">Youtube</a>
3. ScrollReveal() function : <a href="https://www.youtube.com/watch?v=ePgnR4gHIi4">Youtube</a>
4. Carousel ideas : <a href="Carousel">Codepen</a>
5. Understanding Widgets : <a href ="https://simpleisbetterthancomplex.com/tutorial/2019/01/03/how-to-use-date-picker-with-django.html">Here</a>
6. Heavy inspiration from CI Hello Django and Blog Walkthrough
7. Bootstrap Documentation
8. Django Documentation
9. EmailJs instructions may be found on <a href="https://www.emailjs.com/">EmailJS</a>



## Acknowledgements

-I would like to thank my wonderful girfriend for the inspiration and idea conception
<br>
-CI for provide me the knowledge to under-take this task
<br>
-Tutor Support for provideing better knowledge to implement the code and salvaging my project, especially Sean and Ed
<br>
-CI Boutique Ado for a solid foundation and logic behind e-commerce applications
<br>
-The wonderful community over on Slack!
<