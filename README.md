<div id="top"></div>
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
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/hakrichTech?tab=repositories">
    <img src="https://hakrichnews.com/favicon.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">@HkmCodePy Framework - Configuration System </h3>

  <p align="center">
    An awesome Configuration package, you can add to your  projects!
    <br />
    <!-- <a href="https://github.com/othneildrew/Best-README-Template"><strong>Explore the docs »</strong></a> -->
    <br />
    <br />
    <!-- <a href="https://github.com/othneildrew/Best-README-Template">View Demo</a> -->
    <!-- · -->
    <a href="https://github.com/hakrichTech/HkmCodePy/issues">Report Bug</a>
    ·
    <!-- <a href="https://github.com/othneildrew/Best-README-Template/issues">Request Feature</a> -->
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Package</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

[![Product Name Screen Shot][product-screenshot]](https://example.com)

There are many great Frameworks packages in python available on GitHub; however, I didn't find one that really suited my needs so I created this enhanced one. I want to create a Python Framework so amazing that it'll be the last one you ever need -- I think this is it.

Here's why:
* Your time should be focused on creating something amazing. A project that solves a problem and helps others
* You shouldn't be doing the same tasks over and over like creating a Cofiguration file from scratch
* You should implement DRY principles to the rest of your life :smile:

Of course, no one Framework will serve all projects since your needs may be different. So I'll be adding more in the near future. You may also suggest changes by forking this repo and creating a pull request or opening an issue. Thanks to all the people have contributed to expanding this Framework!

Use the `Code button` to get started.

<p align="right">(<a href="#top">back to top</a>)</p>



### Built With

<!-- This section should list any major frameworks/libraries used to bootstrap your project. Leave any add-ons/plugins for the acknowledgements section. Here are a few examples. -->

* [HkmCodePy Framework](https://python.hkmcode.com/)
* [Python](https://python.hkmcode.com/)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

This is an example of how you may give instructions on setting up your project configurations file locally.
To get it up copy up and running follow commands.

* after install everything needed jump to your project root directory, open a terminal and run the following command
  ```sh
  hkmconfig -i
  ```

The above command will generate a configuration package folder in your project root directory called  <a href="#">Hkm_Bin</a> folder with __int__.py file int it
and <a href="#">configuration.yaml</a> file in root directory

* if you open configuration.yaml file you will have this content by default
```yaml
# APPLICATION
App:
    baseURL: http://localhost
    port: 8080
    defaultLocale: fr
```
The App config settings is a default one comes in the package

* To call a Default config setting in your project is:
```py
from hkmConfig.Config import ConfigSystem

config = ConfigSystem()
appConfig = config.Config('App')

```
* Or

```py
from hkmConfig.NamespaceHelpers import hkmConfig

appConfig = hkmConfig('App')

```

* Calling one of the property of config:

```py

print(appconfig.port) # print: 8080

```
* If you change the value of port in configuration.yaml file to 6060:
```yaml
# APPLICATION
App:
    port: 6060
```

* Then:

```py
print(appconfig.port) # print: 6060

```

* To create a config file execute the following command in your project root folder

```sh
hkmconfig -c Testconfig
```
* You will see a Testconfig.py file generated in Hkm_Bin folder with the following contents:

```py
from hkmConfig.Base import Config

class Testconfig(Config):
    def RUN(self):
        self.config_file = 'Testconfig'

```

* and in configuration.yaml

```yaml

# TESTCONFIG
Testconfig:
#  configProperty: value
```

* If want to add any setting in Testconfig ex: test setting
  you go and open Testconfig.py file and add the following line under <strong>self.config_file = 'Testconfig'</strong> in the same ident

```py
class Testconfig(Config):
    def RUN(self):
        self.config_file = 'Testconfig'
        self.test = 'Hello test'
```

* Then to call it any where in your project just do

```py
testConfig = hkmConfig('Hkm_Bin.Testconfig')
print(testConfig.test) # print: Hello test
```

* To change it in configuration.yaml file just do:
```yaml
# TESTCONFIG
Testconfig:
   test: test modif
```

* Then to call it again 

```py
testConfig = hkmConfig('Hkm_Bin.Testconfig')
print(testConfig.test) # print: test modif
```

* which mean "<em>Hello test</em>" is a default value if they dont change it in the configuration.yaml file

### Prerequisites

<!-- This is an example of how to list things you need to use the software and how to install them. -->

* pip
  ```sh
  apt install python3-pip
  ```
* pyyaml
 ```sh
 pip install pyyaml
 ```

### Installation

<!-- _Below is an example of how you can instruct your audience on installing and setting up your app. This template doesn't rely on any external dependencies or services._ -->

<!-- 1. Get a free API Key at [https://example.com](https://example.com) -->
1. Clone the repo
   ```sh
   git clone https://github.com/hakrichTech/HkmCodePy.git
   ```
2. Install package
   ```sh
   python3 setup.py install
   ```
<!-- 3. Enter your API in `config.js`
   ```js
   const API_KEY = 'ENTER YOUR API';
   ``` -->

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
<!-- ## Usage

Use this space to show useful examples of how a project can be used. Additional screenshots, code examples and demos work well in this space. You may also link to more resources.

_For more examples, please refer to the [Documentation](https://example.com)_

<p align="right">(<a href="#top">back to top</a>)</p> -->



<!-- ROADMAP -->
<!-- ## Roadmap

- [x] Add Changelog
- [x] Add back to top links
- [ ] Add Additional Templates w/ Examples
- [ ] Add "components" document to easily copy & paste sections of the readme
- [ ] Multi-language Support
    - [ ] Chinese
    - [ ] Spanish

See the [open issues](https://github.com/othneildrew/Best-README-Template/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#top">back to top</a>)</p>
 -->


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

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the GNU License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

hakeem code  - [@hakrichTech ](https://github.com/hakrichTech - hakeemshamavu@hakrichteam.com

Project Link: [https://github.com/hakrichTech/HkmCodePy](https://github.com/hakrichTech/HkmCodePy)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
<!-- ## Acknowledgments

Use this space to list resources you find helpful and would like to give credit to. I've included a few of my favorites to kick things off!

* [Choose an Open Source License](https://choosealicense.com)
* [GitHub Emoji Cheat Sheet](https://www.webpagefx.com/tools/emoji-cheat-sheet)
* [Malven's Flexbox Cheatsheet](https://flexbox.malven.co/)
* [Malven's Grid Cheatsheet](https://grid.malven.co/)
* [Img Shields](https://shields.io)
* [GitHub Pages](https://pages.github.com)
* [Font Awesome](https://fontawesome.com)
* [React Icons](https://react-icons.github.io/react-icons/search)

<p align="right">(<a href="#top">back to top</a>)</p>
 -->


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/othneildrew/Best-README-Template.svg?style=for-the-badge
[contributors-url]: https://github.com/othneildrew/Best-README-Template/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/othneildrew/Best-README-Template.svg?style=for-the-badge
[forks-url]: https://github.com/othneildrew/Best-README-Template/network/members
[stars-shield]: https://img.shields.io/github/stars/othneildrew/Best-README-Template.svg?style=for-the-badge
[stars-url]: https://github.com/othneildrew/Best-README-Template/stargazers
[issues-shield]: https://img.shields.io/github/issues/othneildrew/Best-README-Template.svg?style=for-the-badge
[issues-url]: https://github.com/othneildrew/Best-README-Template/issues
[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=for-the-badge
[license-url]: https://github.com/othneildrew/Best-README-Template/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/othneildrew
[product-screenshot]: images/screenshot.png 
