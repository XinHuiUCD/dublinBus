<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->


<!-- PROJECT LOGO -->

<br />
<div align="center">
  <a href="https://github.com/XinHuiUCD/dublinBus">
    <img src="https://github.com/XinHuiUCD/dublinBus/blob/main/dbus/src/assets/Dublin-Bus-logo.png" alt="Logo" width="320" height="160">
  </a>

<h3 align="center">Team 10</h3>

  <p align="center">
    Dublin Bus
    <br />
    <a href="https://github.com/othneildrew/Best-README-Template"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="http://ipa-011.ucd.ie/">View Live Project</a>
    ·
    <a href="https://github.com/XinHuiUCD/dublinBus/issues">Report Bug</a>
    ·
    <a href="https://github.com/XinHuiUCD/dublinBus/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
        <li><a href="#run">Run</a></li>
      </ul>
    </li>
    <li><a href="#features">Features</a>
      <ul>
        <li><a href="#journey-planner">Journey Planner</a></li>
        <li><a href="#fare-calculation">Fare Calculation</a></li>
        <li><a href="#route-information">Route Information</a></li>
        <li><a href="#real-time-information">Real Time Information</a></li>
        <li><a href="#weather-information">Weather Information</a></li>
        <li><a href="#twitter">Twitter</a></li>
        <li><a href="#register-and-login">Register & Login</a></li>
        <li><a href="#dark-mode">Dark Mode</a></li>
        <li><a href="#mobile-optimization">Mobile Optimization</a></li>
      </ul>
    </li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project
<div align="center">
  <a href="https://github.com/XinHuiUCD/dublinBus">
    <img src="https://github.com/XinHuiUCD/dublinBus/blob/main/README_imgs/Journey_Planner.gif" alt="Journey_Planner">
  </a>
</div>
  <h3>Make sure to click the marker icon after entering your address!<h3>

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

* [![Vue][Vue.js]][Vue-url]
* [![Django][Django.com]][Django-url]
* [![Bootstrap][Bootstrap.com]][Bootstrap-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

### Prerequisites

This is an example of how to list things you need to use the software and how to install them.
* npm
  ```sh
  npm install npm@latest -g
  ```

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/XinHuiUCD/dublinBus.git
   ```
2. cd into the cloned directory
   ```sh
   cd dbus
   ```
3. Install NPM packages
   ```sh
   npm install
   ```
4. Install pip requirements & activate pipenv shell
   ```sh
   pipenv install --dev && pipenv shell
   ```

### Run
1. Serve the frontend
   ```sh
   npm run serve
   ```
2. Serve the backend. Note: You must be in pipenv shell at this point.
   ```sh
   python manage.py runserver 9000
   ```
3. Access App from frontend or backend
   ```sh
   http://localhost:8080/
   ```
   
<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Features

### Journey-Planner
<div>
  <p>Enter the destination you want to go to, click the Submit button, and our app will show you the time predicted by our model, the different bus routes, and the fare required.</p>
  <h3>Make sure to click the marker icon after entering your address!<h3>
  <a href="https://github.com/XinHuiUCD/dublinBus">
    <img src="https://github.com/XinHuiUCD/dublinBus/blob/main/README_imgs/Journey_Planner.png">
  </a>
</div>

### Fare-Calculation
<div>
  <p>Users can view their fare by clicking on the Fare button. This is calculated by the distance of the journey. All potential fare are displayed so the user does not have specify their age. </p>
  <a href="https://github.com/XinHuiUCD/dublinBus">
    <img src="https://github.com/XinHuiUCD/dublinBus/blob/main/README_imgs/fare_calculation.png">
  </a>
</div>

### Route-Information
<div>
  <p>The route information feature allows users to search for the bus routes they want to view. Also, users can add their favorite routes to their favorites for future viewing.</p>
  <a href="https://github.com/XinHuiUCD/dublinBus">
    <img src="https://github.com/XinHuiUCD/dublinBus/blob/main/README_imgs/Route_Info.png">
  </a>
</div>

### Real-Time-Information
<div>
  <p>The user can select a bus stop on the map and view the expected arrivals of buses for that particular stop. </p>
  <a href="https://github.com/XinHuiUCD/dublinBus">
    <img src="https://github.com/XinHuiUCD/dublinBus/blob/main/README_imgs/RealtimeInfo.png">
  </a>
</div>

### Weather-Information
<div>
  <p>The weather feature allows users to view the current weather in Dublin, tomorrow's weather and weather information for three days from now. This information includes temperature, feels like temperature and weather description information.</p>
    <a href="https://github.com/XinHuiUCD/dublinBus">
      <img src="https://github.com/XinHuiUCD/dublinBus/blob/main/README_imgs/current_weather.png">
      <img src="https://github.com/XinHuiUCD/dublinBus/blob/main/README_imgs/tomorrow_weather.png">
      <img src="https://github.com/XinHuiUCD/dublinBus/blob/main/README_imgs/future_weather.png">
    </a>
</div>

### Twitter
<div>
  <p>The Twitter feature allows users to view the latest tweets from Dublin Bus, so that users can easily can view new information and alerts from Dublin Bus that our models cannot predict.</p>
  <a href="https://github.com/XinHuiUCD/dublinBus">
    <img src="https://github.com/XinHuiUCD/dublinBus/blob/main/README_imgs/Twitter.png">
  </a>
</div>

### Register-and-Login
<div>
  <p>The Register and Login features allow users to create their own account and display their username on the page. Users' information is stored in the database and verified with JWT-Authorization. In addition, all functions are not affected if users do not login, there are no restrictions.</p>
  <a href="https://github.com/XinHuiUCD/dublinBus">
    <img src="https://github.com/XinHuiUCD/dublinBus/blob/main/README_imgs/Register.png">
    <img src="https://github.com/XinHuiUCD/dublinBus/blob/main/README_imgs/Login.png">
    <img src="https://github.com/XinHuiUCD/dublinBus/blob/main/README_imgs/login_completed.png">
  </a>
</div>

### Dark-Mode
<div>
  <p>The main purpose of setting the dark mode function is to facilitate users to use the product at night. In addition, the dark mode will also have a certain protective effect on people's eyes, which is good for users.</p>
  <a href="https://github.com/XinHuiUCD/dublinBus">
    <img src="https://github.com/XinHuiUCD/dublinBus/blob/main/README_imgs/Dark_mode.png">
  </a>
</div>

### Mobile-Optimization
<div>
  <p>Our App is also optimized for mobile, so users can use the product perfectly on mobile as well.Everything in the navigation bar is placed in one button, and when users click on the button, they can view all the functions.</p>
  <a href="https://github.com/XinHuiUCD/dublinBus">
    <img src="https://github.com/XinHuiUCD/dublinBus/blob/main/README_imgs/mobile1.png" width="32%">
    <img src="https://github.com/XinHuiUCD/dublinBus/blob/main/README_imgs/mobile2.png" width="32%">
    <img src="https://github.com/XinHuiUCD/dublinBus/blob/main/README_imgs/mobile3.png" width="32%">
  </a>
</div>
<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE 
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p> 
-->



<!-- CONTACT -->
## Contact
[Gus Boothman - Front-end](https://github.com/Gus1616)
<br/>
[Will O’Donohoe - Data Analytic](https://github.com/21chubaka)
<br/>
[Cheng Zhang - Front-end](https://github.com/20211342)
<br/>
[Xinhui Jiang - Back-end](https://github.com/XinHuiUCD)

Project Link: [https://github.com/XinHuiUCD/dublinBus](https://github.com/XinHuiUCD/dublinBus)

<p align="right">(<a href="#readme-top">back to top</a>)</p>





<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->

[Vue.js]: https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D
[Vue-url]: https://vuejs.org/
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[Django.com]: https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white
[Django-url]: https://www.djangoproject.com

