# Testing

- Manual testing was carried out throughout the development of the website and bugs fixed as they arose. 

## Manual testing
- Manual testing was carried out on the local and deployed sites.
                                                                         
|Location       | Feature                 | Expected Outcome                                                | Pass/Fail|
|--------------|-------------------------|-----------------------------------------------------------------|---------|
|Navbar         | Home link               | On click goes to home webpage                                   | Pass     |
|Navbar         | Games link              | On click goes to Games webpage                                  | Pass     |
|Navbar         | Support link            | On click goes to Support webpage                                | Pass     |  
|Navbar         | Register link           | On click goes to the register account page                      | Pass     |  
|Navbar         | Sign In link            | On click goes to Sign in webpage                                | Pass     |
|Navbar         | Account link            | On click goes to Account webpage                                | Pass     |
|Navbar         | Logout link             | On click goes to Sign out webpage                               | Pass     |
|Navbar         | Viewable on all pages   | The navbar to be visible on all webpages                        | Pass     |
|--------------|-------------------------|-----------------------------------------------------------------|---------|
|Support Page   | Live Chat Button        | On click goes to Playstations Live Chat                         | Pass     |    
|Support Page   | Name Input              | Allows User to input their name                                 | Pass     |
|Support Page   | Email Input             | Allows User to input their email                                | Pass     |
|Support Page   | Issue Type Dropdown     | Allows User to select 1 of 3 types of issue                     | Pass     |  
|Support Page   | Message Input           | Allows User to a longer description of their Issue              | Pass     |  
|Support Page   | Submit                  | Allows User to submit their support request                     | Pass     |
|--------------|-------------------------|-----------------------------------------------------------------|---------| 
|Register Page  | Username Input          | Allows User to input their Username                             | Pass     | 
|Register Page  | Email Input             | Allows User to input their Email                                | Pass     | 
|Register Page  | Password Input          | Allows User to input their Password                             | Pass     |
|Register Page  | Password Input 2        | Allows User to input their Password again to confirm            | Pass     |
|Register Page  | Sign Up Button          | Allows User to register their account/ sign up                  | Pass     |
|--------------|-------------------------|-----------------------------------------------------------------|---------|
|Sign In Page   | Username Input          | Allows User to input their Username                             | Pass     |
|Sign In Page   | Password Input          | Allows User to input their Password                             | Pass     |
|Sign In Page   | Remember Me Checkbox    | Allows User to select their info to be remembered               | Pass     |
|Sign In Page   | Sign In Button          | Allows User to Sign into their account if all details = correct | Pass     |
|--------------|-------------------------|-----------------------------------------------------------------|---------|
|Account Page   | Shows Games Purchased   | Allows User to see their purchased games                        | Pass     |
|--------------|-------------------------|-----------------------------------------------------------------|---------|
|Logout Page    | Sign Out Button         | Allows User to sign out of their account                        | Pass     |
|--------------|-------------------------|-----------------------------------------------------------------|---------|
|Home, Games    | Game Cards              | Allows User to select a game to then go to that webpage         | Pass     |
|--------------|-------------------------|-----------------------------------------------------------------|---------|
|Game Info      | Purchase                | Allows User to select purchase that game, if theyre signed in   | Pass     |
|Game Info      | Game Info DropDown      | Allows User to select hide the game info section                | Pass     |
|Game Info      | Technical Info DropDown | Allows User to select hide the Technical Info section           | Pass     |
|Game Info      | Trophies Info DropDown  | Allows User to select hide the Trophies info section            | Pass     |
|Game Info      | Awards Info DropDown    | Allows User to select hide the game's Awards info section       | Pass     |
|Game Info      | Comment Section         | Allows User, if they own the game, to leave a comment           | Pass     |
|Game Info      | Comment Title Input     | When making a comment, Players input becomes the title          | Pass     |
|Game Info      | Playstation Level Input | When making a comment, Players select their PS level            | Pass     |
|Game Info      | Game Rating Input       | When making a comment, Players select their Rating for that game| Pass     |
|Game Info      | Platinum Trophy Dropdown| When making a comment, Players select if theyve got Platinum    | Pass     |
|Game Info      | Platinum Stability Input| When making a comment, Players select if the platinum trophy was stable| Pass     |
|Game Info      | Glitched Trophies Drowdown | When making a comment, Players select if there was glitched trophies| Pass     |
|Game Info      | Glitched Trophies Input     | When making a comment, Players can type in what trophies was glitched| Pass     |
|Game Info      | Game Version Input       | When making a comment, Players select the game version | Pass     |
|Game Info      | Playtime Input       | When making a comment, Players select their playtime for the game | Pass     |
|Game Info      | Platform Dropdown       | When making a comment, Players select what platfrom they are playing on| Pass     |
|Game Info      | Main Comment Input       | When making a comment, Players can input a text based comment | Pass     |
|Game Info      | Comment View Details      | When reviewing the comments it opens the dropdown including all the inputs from above| Pass     |
|Game Info      | Edit Button      | After making a comment and still signed in, allows a user to edit the review | Pass     |
|Game Info      | Update Button       | When editing a comment and still signed in, allows a user to update the review| Pass     |
|Game Info      | Delete Button       | Opens a pop up menu to delete comment | Pass     |
|Game Info      | 'delete comment?' Delete Button       | Deletes the comment | Pass     |
|Game Info      | 'delete comment?' Close Button       | Closes the 'delete comment?' menu. | Pass     |
|--------------|-------------------------|-----------------------------------------------------------------|---------|
|Footer      | Facebook Icon                | Takes user to Playstations Facebook  | Pass     |
|Footer      | Twitter Icon                | Takes user to Playstations Twitter  | Pass     |
|Footer      | Instagram Icon                | Takes user to Playstations Instagram  | Pass     |
|Footer      | Youtube Icon                | Takes user to Playstations Youtube  | Pass     |
|Footer      | Viewable on all pages   |The Footer to be visible on all webpages    | Pass     |
|--------------|-------------------------|-----------------------------------------------------------------|---------|

When it comes to the section about the comments, due to not being linked to the playstations database the comment inputs about Playstation Level, Game Version and Platinum Achieved have had to be done manually due to not being able to pull the data from a accurate database like it would be if i had access to the relevant Playstations Data.

## Code validators
### HTML by URL
- The [W3C Validator](https://validator.w3.org/) was used to validate the HTML.
#### Home
- ![Home page validator screenshot](Readme_Files/HTML_URL/HTML_Validated_URL_Home.png)

#### Games page
- ![Games page validator screenshot](Readme_Files/HTML_URL/HTML_Validated_URL_Games.png)

#### Games Detail page
- ![Games Detail page validator screenshot](Readme_Files/HTML_URL/HTML_Validated_URL_Game_Details.png)
- This had an error due to summeradmin using font color in its form which is something I can't edit or change.  

#### Register page
- ![Register page validator screenshot](Readme_Files/HTML_URL/HTML_Validated_URL_Sign_Up.png)
- Very similar error, this is due to signup in its form using to many or unsupported tags and elements

#### Logout page
- ![Logout page validator screenshot](Readme_Files/HTML_URL/HTML_Validated_URL_Log_Out.png)

#### Login page
- ![Login page validator screenshot](Readme_Files/HTML_URL/HTML_Validated_URL_Log_In.png)

#### Account_Profile page
- ![Account_Profile page validator screenshot](Readme_Files/HTML_URL/HTML_Validated_URL_Account.png)
- This was an error due to not being able to login as this was using the HTML by URL 

### HTML by Direct Input
#### Home
- ![Home page validator screenshot](Readme_Files/HTML_Direct_Input/HTML_Validated_Direct_Input_Home.png)

#### Games page
- ![Games page validator screenshot](Readme_Files/HTML_Direct_Input/HTML_Validated_Direct_Input_Games.png)

#### Games Detail page
- ![Games Detail page validator screenshot](Readme_Files/HTML_Direct_Input/HTML_Validated_Direct_Input_Game_Details.png)
- This had an error due to summeradmin using font color in its form which is something I can't edit or change.  

#### Register page
- ![Register page validator screenshot](Readme_Files/HTML_Direct_Input/HTML_Validated_Direct_Input_Sign_Up.png)
- Very similar error, this is due to signup in its form using to many or unsupported tags and elements

#### Logout page
- ![Logout page validator screenshot](Readme_Files/HTML_Direct_Input/HTML_Validated_Direct_Input_Log_Out.png)

#### Login page
- ![Login page validator screenshot](Readme_Files/HTML_Direct_Input/HTML_Validated_Direct_Input_Log_In.png)

#### Account_Profile page
- ![Account_Profile page validator screenshot](Readme_Files/HTML_Direct_Input/HTML_Validated_Direct_Input_Account.png)

### CSS custom code
- The [W3C CSS Validator](https://jigsaw.w3.org/css-validator/) was used to validate the CSS.
- ![CSS validator screenshot](Readme_Files/CSS/CSS_Validated.png)

<p>
    <a href="http://jigsaw.w3.org/css-validator/check/referer">
        <img style="border:0;width:88px;height:31px"
            src="http://jigsaw.w3.org/css-validator/images/vcss"
            alt="Valid CSS!" />
    </a>
</p>
<p>
<a href="http://jigsaw.w3.org/css-validator/check/referer">
    <img style="border:0;width:88px;height:31px"
        src="http://jigsaw.w3.org/css-validator/images/vcss-blue"
        alt="Valid CSS!" />
    </a>
</p>

### Javascript custom code
- The [JSHint JS Validator](hhttps://jshint.com/) was used to validate the Javascript.

#### Comments
- ![Comments script validator screenshot](Readme_Files/JS/Comments_JS_Validated.png)

#### Purchased_Checker
- ![Purchased Checker script validator screenshot](Readme_Files/JS/Purchase_Checker_JS_Validated.png)

### Python
- The [CI Python Linter](https://pep8ci.herokuapp.com/) was used to validate the Python files.

## Playstation Project
- settings.py
- ![PEP8 screenshot](Readme_Files/Python/playstation_project/settings_py_validated.png)
- playstation/urls.py
- ![PEP8 screenshot](Readme_Files/Python/playstation_project/urls_py_validated.png)
- asgi.py
- ![PEP8 screenshot](Readme_Files/Python/playstation_project/asgi_py_validated.png)
- wsgi.py
- ![PEP8 screenshot](Readme_Files/Python/playstation_project/wsgi_py_validated.png)

## Store App
- admin.py
- ![PEP8 screenshot](Readme_Files/Python/store_app/admin_py_validated.png)
- apps.py
- ![PEP8 screenshot](Readme_Files/Python/store_app/apps_py_validated.png)
- forms.py
- ![PEP8 screenshot](Readme_Files/Python/store_app/forms_py_validated.png)
- models.py
- ![PEP8 screenshot](Readme_Files/Python/store_app/models_py_validated.png)
- store/urls.py
- ![PEP8 screenshot](Readme_Files/Python/store_app/urls_py_validated.png)
- views.py
- ![PEP8 screenshot](Readme_Files/Python/store_app/views_py_validated.png)

## Support App
- admin.py
- ![PEP8 screenshot](Readme_Files/Python/support_app/admin_py_validated.png)
- apps.py
- ![PEP8 screenshot](Readme_Files/Python/support_app/apps_py_validated.png)
- forms.py
- ![PEP8 screenshot](Readme_Files/Python/support_app/forms_py_validated.png)
- models.py
- ![PEP8 screenshot](Readme_Files/Python/support_app/models_py_validated.png)
- support/urls.py
- ![PEP8 screenshot](Readme_Files/Python/support_app/urls_py_validated.png)
- views.py
- ![PEP8 screenshot](Readme_Files/Python/support_app/views_py_validated.png)

## Account_Profile App
- admin.py
- ![PEP8 screenshot](Readme_Files/Python/account_profile_app/admin_py_validated.png)
- apps.py
- ![PEP8 screenshot](Readme_Files/Python/account_profile_app/apps_py_validated.png)
- models.py
- ![PEP8 screenshot](Readme_Files/Python/account_profile_app/models_py_validated.png)
- account_profile/urls.py
- ![PEP8 screenshot](Readme_Files/Python/account_profile_app/urls_py_validated.png)
- views.py
- ![PEP8 screenshot](Readme_Files/Python/account_profile_app/views_py_validated.png)

### Lighthouse - Mobile
#### Home
- ![Lighthouse screenshot for home page](Readme_Files/Lighthouse/Mobile/Home_Lighthouse.png)

#### Games
- ![Lighthouse screenshot for games page](Readme_Files/Lighthouse/Mobile/Games_Lighthouse.png)

#### Games Details
- ![Lighthouse screenshot for games details page](Readme_Files/Lighthouse/Mobile/Game_Details_Lighthouse.png)

#### Register
- ![Lighthouse screenshot for register page](Readme_Files/Lighthouse/Mobile/Sign_Up_Lighthouse.png)

#### Login
- ![Lighthouse screenshot for login page](Readme_Files/Lighthouse/Mobile/Log_In_Lighthouse.png)

#### Logout
- ![Lighthouse screenshot for logout page](Readme_Files/Lighthouse/Mobile/Log_Out_Lighthouse.png)

#### Support
- ![Lighthouse screenshot for support page](Readme_Files/Lighthouse/Mobile/Support_Lighthouse.png)

#### Account
- ![Lighthouse screenshot for account page](Readme_Files/Lighthouse/Mobile/Account_Lighthouse.png)


### Lighthouse - Desktop
#### Home
- ![Lighthouse screenshot for home page](Readme_Files/Lighthouse/Desktop/Home_Lighthouse.png)

#### Games
- ![Lighthouse screenshot for games page](Readme_Files/Lighthouse/Desktop/Games_Lighthouse.png)

#### Games Details
- ![Lighthouse screenshot for games details page](Readme_Files/Lighthouse/Desktop/Game_Details_Lighthouse.png)

#### Register
- ![Lighthouse screenshot for register page](Readme_Files/Lighthouse/Desktop/Sign_Up_Lighthouse.png)

#### Login
- ![Lighthouse screenshot for login page](Readme_Files/Lighthouse/Desktop/Log_In_Lighthouse.png)

#### Logout
- ![Lighthouse screenshot for logout page](Readme_Files/Lighthouse/Desktop/Log_Out_Lighthouse.png)

#### Support
- ![Lighthouse screenshot for support page](Readme_Files/Lighthouse/Desktop/Support_Lighthouse.png)

#### Account
- ![Lighthouse screenshot for account page](Readme_Files/Lighthouse/Desktop/Account_Lighthouse.png)

#### Future improvements based on Lighthouse
- 


## Responsiveness
### Mobile (iPhone 16 Pro)
- ![mobile responsiveness screenshot- home](Readme_Files/Responsiveness/Iphone_16_Home.png)
- ![mobile responsiveness screenshot- register](Readme_Files/Responsiveness/Iphone_16_Register.png)
- ![mobile responsiveness screenshot- game details](Readme_Files/Responsiveness/Iphone_16_Game_Details.png)

### Mobile (iPhone 13 Mini)
- ![mobile responsiveness screenshot- home](Readme_Files/Responsiveness/Iphone_13_Mini_Home.png)
- ![mobile responsiveness screenshot- register](Readme_Files/Responsiveness/Iphone_13_Mini_Register.png)
- ![mobile responsiveness screenshot- game details](Readme_Files/Responsiveness/Iphone_13_Mini_Game_Details.png)

### Tablet (iPad Pro 2024)
- ![tablet responsiveness screenshot- home](Readme_Files/Responsiveness/Ipad_Home.png)
- ![tablet responsiveness screenshot- register](Readme_Files/Responsiveness/Ipad_Register.png)
- ![tablet responsiveness screenshot- game details](Readme_Files/Responsiveness/Ipad_Game_Details.png)

### Laptop (Windows 11)
- ![laptop responsiveness screenshot- home](Readme_Files/Responsiveness/Laptop_Home.png)
- ![laptop responsiveness screenshot- register](Readme_Files/Responsiveness/Laptop_Register.png)
- ![laptop responsiveness screenshot- game details](Readme_Files/Responsiveness/Laptop_Game_Details.png)

## Browsers
- I use Google Chrome as my browser so all screenshots above are from Google Chrome.
- ![Google Chrome screenshot](Readme_Files/Browsers/Google_Chrome.png)
- The site was tested on Microsoft Edge:
- ![Microsoft Edge screenshot](Readme_Files/Browsers/Microsoft_Edge.png)
- The site was tested on Opera:
- ![Opera screrenshot](Readme_Files/Browsers/OperaGX.png)

## Bugs
- 
