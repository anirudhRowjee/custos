# Devspot WEBATHON

## Judgement Criteria

1. Uniqueness(Ingenuity) - x Points
2. Practical usecase(Impact) - x Points
3. User Experience(Working MVP) - x Points
4. Code quality & scalability - x Points
5. User Interface - x Points
6. Presentation - x Points

## Idea

A tool to tell you when you can use the things that you get from outside.

For example, if you order something from Amazon, and get it to your house, and you need to wait 24 hours before touching it, it's a pain to manually remember (especially for a large number of items) when it's safe to touch different things, and by extension, when it's safe to user them. If you use our solution, you will not need to rememeber anything, as the app will take care of that for you, all while allowing you to see which items are past the time limit (making them safe to use).

You can also share your lists with other people and allow then to benefit from the timing.

## Main Features

1. Keep track of things that you get from outside
2. Set timers to see when the things are safe to use
3. Add family members/ roommates to view the timers, add new things
4. Change status of products which are yet to arrive with the arrival date to keep track of everything (?)

## Sitemap

1. "/" Homepage (onboarding)
2. "/signin" Login / Register
3. "/lists" (default once logged in) all lists
4. "/me" settings page
5. "/shared" lists shared with me

## Architecture

1. Django
2. Third-Party Auth Packages for Django (django-socialauth, etc)
3. React in Django Templates
4. Bootstrap

## Colorscheme

css
/* CSS HEX */
--white: #ffffffff;
--star-command-blue: #2274a5ff;
--blush: #ea638cff;
--orange: #f77f00ff;
--eerie-black: #141414ff;

/* CSS HSL */
--white: hsla(0, 0%, 100%, 1);
--star-command-blue: hsla(202, 66%, 39%, 1);
--blush: hsla(342, 76%, 65%, 1);
--orange: hsla(31, 100%, 48%, 1);
--eerie-black: hsla(0, 0%, 8%, 1);

/* SCSS HEX */
$white: #ffffffff;
$star-command-blue: #2274a5ff;
$blush: #ea638cff;
$orange: #f77f00ff;
$eerie-black: #141414ff;

/* SCSS HSL */
$white: hsla(0, 0%, 100%, 1);
$star-command-blue: hsla(202, 66%, 39%, 1);
$blush: hsla(342, 76%, 65%, 1);
$orange: hsla(31, 100%, 48%, 1);
$eerie-black: hsla(0, 0%, 8%, 1);

/* SCSS RGB */
$white: rgba(255, 255, 255, 1);
$star-command-blue: rgba(34, 116, 165, 1);
$blush: rgba(234, 99, 140, 1);
$orange: rgba(247, 127, 0, 1);
$eerie-black: rgba(20, 20, 20, 1);

/* SCSS Gradient */
$gradient-top: linear-gradient(0deg, #ffffffff, #2274a5ff, #ea638cff, #f77f00ff, #141414ff);
$gradient-right: linear-gradient(90deg, #ffffffff, #2274a5ff, #ea638cff, #f77f00ff, #141414ff);
$gradient-bottom: linear-gradient(180deg, #ffffffff, #2274a5ff, #ea638cff, #f77f00ff, #141414ff);
$gradient-left: linear-gradient(270deg, #ffffffff, #2274a5ff, #ea638cff, #f77f00ff, #141414ff);
$gradient-top-right: linear-gradient(45deg, #ffffffff, #2274a5ff, #ea638cff, #f77f00ff, #141414ff);
$gradient-bottom-right: linear-gradient(135deg, #ffffffff, #2274a5ff, #ea638cff, #f77f00ff, #141414ff);
$gradient-top-left: linear-gradient(225deg, #ffffffff, #2274a5ff, #ea638cff, #f77f00ff, #141414ff);
$gradient-bottom-left: linear-gradient(315deg, #ffffffff, #2274a5ff, #ea638cff, #f77f00ff, #141414ff);
$gradient-radial: radial-gradient(#ffffffff, #2274a5ff, #ea638cff, #f77f00ff, #141414ff);


## Models

1. User (extends Django base User Model)
    - username
    - password
    - email
    - default_timer

2. List
    - User (fkey)
    - Name
    - Created Timestamp

3. Item
    - User (fkey)
    - List (fkey)
    - Name
    - added_timestamp
    - expected_elapsed_timestamp
    - Expired (boolean flag, done or not)

4. PrivilegeTable (Decides who can see what)
    - List (fkey)
    - User (fkey)
    - role (One of 3 - Editor, Consumer and Owner)

// by default, every user is the owner of the lists they create

## Resources
