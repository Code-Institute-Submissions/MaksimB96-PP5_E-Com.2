# Honey Haven

(Developer: Maksims Buraks)

![Mockup image](docs/am-i-responsive.png)

[live web-page](https://honeyhaven-236ab8f8ceba.herokuapp.com/)

## Table of contents

- [Honey Haven](#honey-haven)
  - [Table of contents](#table-of-contents)
  - [Project Overview](#project-overview)
  - [Business Model](#business-model)
  - [Project Goals](#project-goals)
    - [User Stories](#user-stories)
    - [Site Owner Stories](#site-owner-stories)
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

SEO scores returned high through out as the keywords helped optimize them!


## Business Model

# Facebook Page

This project utilizes a facebook page to increase the clients reach and influence. It is based in cavan so the target audience would be local but through marketing it would allow to expand it's reach further in Ireland!

![Facebook](docs/honey-haven-fb1.png)
![Facebook](docs/honey-haven-fb2.png)


## Project Goals

### User Stories

- To View list of Products
- To View Details of Products
- To View/Update/Delete in bag view

- To be able to register
- To be able to view profile and update delivery info/view previous orders
- To be able to quickly navigate/search/sort products
- To be able to quickly reach checkout without any issues
- To have secure payment
- To be able to see order confirmation via view and email

- To be able to get in contact
- To be able to subscribe to a newsletter service to keep up to date on offers

### Site Owner Stories

- Admin management Panel, to view all models data

- Add/Edit Items outside of admin panel

- Delete Items outside of admin panel

- Send News updates to list of subscribers

### Target Audience

- Honey enthusiasts local to Ireland

### User Requirements and Expectations

- A simple and natural way to navigate the website
- Quick acessibility to relevant information
- Quick acessibility to relevant products
- Appealing design that responds accordingly
- User Subscribe functionality
- Detail view of products
- Login functionality in order to get in contact
    

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
Please find the Entity relationship diagram utilized to bring the project to fruition! The bulk of the logic happens between the user and products which ultimatley resuts in the order being placed. The contact form is a stand alone form that gets submitted to the admin panel which later a staff member will get in contact with. Subscription forms store info in the db which is then used by the admin via the admin news segment to send news to a list of emails.
<br>
Boutique Ado greatly helped establish the website foundations, along with my 3 models being(Subscribers, NewsLtter and Contact Form)


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

- The Index
- The Products
- The Product Detail
- The Bag
- Checkout Area
- Checkout Success
- User Profile (If authenticated)
- News Segment (If super User)
- Edit/Add segemt (If super User)
- Allauth essentials

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

- HTML
- CSS
- Java Script
- Pyhton
- Django
    

### Tools

- Git
- Git Hub
- Git Pod
- Figma
- Google Fonts
- Adobe Color Wheel
- Font Awesome
- Favicon.io
- Circle Crop
- postgresql
- psycopg
- Canva
- Boot strap 4
- pixelr
- Django
- Crispy Forms
- panda_io
- Amazon Web Services


## Validation

### HTML Validation
W3C mark-up was utilised in order to validate html of the website. All Pages pass with no errors. It is worth noting that some pages with data_detail were thrown as errors which was not fixable

<details><summary>HTML</summary>
<img src="docs/validation/html/index-html.png">
</details>

<br>

### CSS Validation
W3C CSS validator was utilised in order to make sure the css code passes standards with no errors.

<details><summary>Full Document</summary>
<img src="docs/validation/css/css-valid.png">
</details>

<br>

### Python Validation

CI Python linter used here to validate my views

<details><summary>Home</summary>
<img src="docs/validation/python/home-view.png">
</details>

<details><summary>Products</summary>
<img src="docs/validation/python/products-view.png">
</details>

<details><summary>Bag</summary>
<img src="docs/validation/python/bag-view.png">
</details>

<details><summary>Checkout</summary>
<img src="docs/validation/python/checkout-view.png">
</details>

<details><summary>Contacts</summary>
<img src="docs/validation/python/contacts-view.png">
</details>

<details><summary>Profiles</summary>
<img src="docs/validation/python/profiles-view.png">
</details>

<details><summary>Subscription</summary>
<img src="docs/validation/python/subscription-view.png">
</details>


### JS Validation
JSHint validator was utilised in order to make sure the javascript code passes standards with no errors or warnings, all functions return without errors!

<br>

### Performance

Below is the performance of all pages (note that performace was consistant across all pages with a high SEO):

<details><summary>Performance</summary>
<img src="docs/performance.png">

</details>

### Tests


#### Devices tested on on

  - Iphone SE, XR, 11, 12, 14, 14 pro, samsung s5
  - Ipad
  - Macbook Pro/Air
  - Lenovo Platform
  - Dell Platform

#### Browser tested on on

  - Chrome
  - Safari
  - Brave/Brave Mobile


### Manual Tests

Manual testing 



### Bugs

During Development I ran in to a few bugs.

  Media Files not fully rendering even with proper aws deployment:

    -This was fixed by implementing a media context proccessor.

  Sorting and some categories did not work:

    -This was fixed by getting rid of the base js in the extended templates

  Codeanywhere workspaces deletion:

    -The cause of this was unknown, however thanks to Sean we migrated back to gitpod which was a more reliable IDE

  Contact form server error:

    -This was simply due to the db not being fully integrated

  Internal server error on deployed site:

    -This was a typo in the products view for loop which I did not commit, site works fine now

3. Toast not

## Deployment

Honey Haven followed a multi-step deployment. The website was deployed as follows:

### GitHub

The process for github was as follows:

  - First, Navigate to [GitHub](https://github.com/).
  - Now go to your repositories and find the project you wish to deploy in my case honey haven 
  - In the repository click on 'Settings' located on the right hand side on the top menu.
  - Scroll down to 'Pages'.
  - Once at 'Source' click on the dropdown and select 'main' branch, and then save it.
  - The page will reload and you'll see the link of your published page displayed under 'GitHub' pages.
    
### Gitpod
  - Navigate to [Gitpod](https://gitpod.io/) workspaces
  - In the browser’s address bar, prefix the entire URL with gitpod.io/# and press Enter.
  - Googles gitpod browser extension allows it to be a single click function.
  - Side Note:
    - Initially the project was developed through CodeAnywhere, however due to it's buggy nature the workspace was deleted, 
    thanks to Sean(Tutor Support) we migrated to Gitpod and after a bit of work got the project back, the DB had to be re-established however.

<hr>
 
### elephantSQL

Secondly a DB was to be established, I utilized elephantSQL.

  * Go to [ElephantSQL.com](https://www.elephantsql.com/)
  * The Tiny Turtle option was used as the free teir to upload and host the DB

  - To sign in I simply logged in via the github portal
  - Create a new app.
  - Name the app. Preferably something similar to the project
  - Select a plan: <strong>Tiny Turtle Plan</strong>
  - Select Region: In my case I selected EU-West-1 (IRELAND).
  - Then click review.
  - Return to the ElephantSQL dashboard and click on the database instance name for this project.
  - Verify the DB was connected by running instances.

<hr>

### AWS

Thirdly AWS was used to host my static and media files, while more complicated, I find less issues when items are hosted!

  I created an account on [Amazon Web Services](https://aws.amazon.com/)
  - Follow a multi-step log in procedure, this includes email verification and utilization of a credit card (which will be charged if usage exceeds free teir)

  <u>Create a bucket</u>
  - Once my account was established, find S3 using the search bar, select and navigate to S3 to create a new bucket which will be used to store your static and media files
  - Create the bucket
  - Eu Ireland was selected as the region.
  - In settings select *ACLs enabled* and a bucket ownership dropdown will appear, select *Bucket owner preferred*
  - On the Block Public Access settings for this bucket section, uncheck *Block all public access*, check the *I acknowledge that the current settings might result in this bucket and the objects within becoming public* checkbox, this renders the bucket public access.
  - In bucket settings select the *properties* tab. Scroll down to find the *static web hosting* section, select *enable static web hosting*
  - using the generated ARN, navigate to the bucket policy section, click *edit* and select *policy generator*. From the *Select Type Policy* dropdown options, select S3 bucket policy. We want to allow all principal by adding the `*` to the input and the from the -Actions* dropdown, select *GetObject*.
  - Paste the ARN into the ARN input field and click *add statement*, then click *generate policy*, copy this Policy from the new popup and paste it into the bucket policy editor and add `/*` at the end of the resource value to allow access to all resources in this policy.
  - Utilize the updated **cross-origin resource sharing** in the below code snippet:
```json

  [
    {
        "AllowedHeaders": [
            "Authorization"
        ],
        "AllowedMethods": [
            "GET"
        ],
        "AllowedOrigins": [
            "*"
        ],
        "ExposeHeaders": []
    }
  ]

```

- Find IAM using the search bar, select and navigate to IAM to create a group, create an access policy to give group access to the S3 bucket and assign the created user to the group so it can use the policy to access the files.
- A group was then created in *User Groups*
- Add a name for your group, one that is relevent to your project, in my case honey haven
- Open the *JSON* tab on the new page and click the *import managed policy*
- Search for S3 and select the pre-built *AmazonS3FullAccess* policy and click *import*
- Edit the policy by pasting the S3 ARN on *resource*, tutor support helped understand this proccess as it was drastically different from the video guide:

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "s3:*",
            "Resource": [
                "arn:aws:s3:::bucket-name",
                "arn:aws:s3:::bucket-name/*",
            ]
        },
        "Statement": [
        {
            "Effect": "Allow",
            "Action": "s3:*",
            "Resource": [
                "arn:aws:s3:::bucket-name",
                "arn:aws:s3:::bucket-name/*",
            ]
        }
    ]
}
```

- Click review
- Assign an appropriate name
- Next attach your policy previously created to the group
- Select the Policy you created and click *add permissions*
- We have to create a user for the group. Click *Users* from the left sidebar and then click the *add users* button and add a name for the user, in my case honeyhaven-staticfiles-user
- Next tick *programmatic access*
- Add user to the group
- Then download the .csv file which will contain this user's access key and secret access key which we'll use to authenticate them from our Django app. It is important to keep these safe as to do the process again will require a new user.



### Connect AWS to django

First, you are required to install boto and django-storages to read these. After these have been installed and your settings reflect this, the following parameters were added to settings:

```python
    if 'USE_AWS' in os.environ:
        AWS_S3_OBJECT_PARAMETERS = {
            'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
            'CacheControl': 'max-age=9460800',
        }

        AWS_STORAGE_BUCKET_NAME = 'your bucket name goes here'
        AWS_S3_REGION_NAME = 'your selected region goes here'
        AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
        AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
        AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
```

The CSV file that was created earlier containing the respective keys were then added to heroku config vars to set it up. Then, additional settings were implemeted in order to allow aws to utilize the static and media files as well as over riding variables:

```python
    STATICFILES_STORAGE = 'custom_storages.StaticStorage'
    STATICFILES_LOCATION = 'static'
    DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
    MEDIAFILES_LOCATION = 'media'

    STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}/'
    MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}/'
```

Once this was completed and the static files pushed, the static folder was established in AWS. Afterwhich, my media files were uploaded to the newly created media folder in AWS! 

It is worth noting that an extra line of code was added to my context processor to allow all media files to load accordingly:

```python

   'django.template.context_processors.media',

```

<hr>

### Heroku

lastly, Heroku was set up to host the web app.
    
- Create a new app, and name it, in my case honeyhaven. 
- I then selected the closest region being EU.
- Once the app was created, open the Settings tab. 
- Click reveal config vars.
- Add the config var <strong><i>DATABASE_URL</i></strong>, utilising the url provided by elephantSQL.
- Add the config var <strong><i>AWS_ACCESS_KEY_ID</i></strong>, add the value previously obtained from aws. 
- Add the config var <strong><i>AWS_SECRET_ACCESS_KEY</i></strong>, add the value previously obtained from aws. 
- Add the config var <strong><i>USE_AWS</i></strong>, and for the value set it to true.
- Add the config var <strong><i>STRIPE_PUBLIC_KEY</i></strong>, add the value previously obtained from the stripe dev dashboard.
- Add the config var <strong><i>STRIPE_SECRET_KEY</i></strong>, add the value previously obtained from the stripe dev dashboard.
- Add the config var <strong><i>STRIPE_WH_SECRET</i></strong>, add the value previously obtained from the stripe dev dashboard > webhooks.
- Add the config var <strong><i>SECRET_KEY</i></strong>, add a random key generated for the project.

- Adjust settings to allow for auto deploy and then deploy!

<hr>

### Github cloning/forking

It is worth mentioning how to clone/fork a project

#### Cloning

1. Go to your repo
2. Locate the Code button above the list of files and click it
3. Select if you prefer to clone using HTTPS, SSH, or GitHub CLI and click the copy button to copy the URL to your clipboard
4. Open Git Bash or Terminal
5. Change the current working directory to the one where you want the cloned directory
6. In your IDE Terminal, type the following command to clone a repo:
   - `git clone https://github.com/Balkaneros91/Cubaneros-PP4.git`
7. Press Enter to create your local clone.

### Forking

1. Go to your repo
2. At the top of the Repository, above the *Settings* button on the menu, locate the *Fork* button.
3. User should now have access to the forked repo

## Future Features

There are a few more feartures that I would like to implement in the future. These Include:

1. Admin view message panel in manage section
2. Rating System/comment section
3. Flesh out the products 
4. A Feedback Section
5. Additional support through webkits for mozilla and other browsers


## Credits

### Media

Logo media created by me using  <a href="https://www.canva.com/">Canva</a>, this includes Icons and backgound images.
<br>
Any Icons used found on <a href="https://fontawesome.com/">Font Awesome</a>
<br>


# Images

1. Landing page - Kat Smith
2. HoneySpoon - Mae My
3. Spoon and honey - Daily Slowdown
4. Small Jar - Dario Menendez
5. Large Jar - Kier
6. Bee suit - gryffn
7. Lip Balm - Antoni Shkraba
8. Candle - Jill Burrow
9. Beeswax paper - Karina Zhukovskaya
10. Bee Flower - Erik Kartis

    
### Code 

1. Product/bag/checkout/search/wh handling logic inspired by : <a href="https://www.youtube.com/watch?v=3_3q_dE4_qs&t=649s">Code Institute Boutique Ado</a>
2. subscription form with my modifications by : <a href="https://www.youtube.com/watch?v=hWtlskOaFNI&t=3315s">KenBroTec</a>
3. Interactive search bar : <a href="https://bbbootstrap.com/snippets/expandable-search-bar-12368750">bbbootstrap</a>
4. Bootstrap Documentation
5. Django Documentation
6. Stripe Docs
7. Github docs


## Acknowledgements

-  would like to thank my wonderful girfriend for the inspiration and idea conception, and for the slight scare at the hospital
- CI for provide me the knowledge to under-take this task
- Tutor Support for provideing better knowledge to implement the code and salvaging my project, especially Sean and Ed
- CI Boutique Ado for a solid foundation and logic behind e-commerce applications
- The wonderful community over on Slack!
- The amazing studetnt support staff that helped me during my tough times