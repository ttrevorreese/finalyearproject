# Murrieta: Connected

![Logo](https://github.com/ttrevorreese/finalyearproject/blob/e60168e9d00ebd8f99534fd9c09fce76eb9ae668/Assets/Murrieta%20Connected%20BW.png)

This is the repository for my Final Year Project, titled Murrieta: Connected, for my BSc at the University of Roehampton London. 

**This repository is a developing prototype, so not everything is currently available.**

## Overview

This project is aimed at creating a usable bus system for the town of Murrieta, California in the United States of America. Since the current public transport infrastructure is lackluster at best, I am aiming to overhaul the current system and create a new bus system, with the routes created by algorithms for optimization. This will then be presented to the user with an interactive map and the ability to search for the best route from a selected origin and destination node.

## Company

Murrieta: Connected is a theoretical company that could be created using the information created from this project. The idea is to be able to build a realistic business model from the output of the program.

## Project Scope

The scope of this project is to build a program from scratch within the time constraint of two university-length terms. This means that the project must be reasonably attainable within this time frame.

The project is to be undertaken by myself and myself only, but Scrum methods and Kanban ideology is expected to be applied throughout.

## Data

The data used in this project is a hand-collected dataset of 174 individual points throughout the city of Murrieta, California, USA based on my own personal knowledge of the city as well as official documents found on the city's official website.

The [United States Census](https://data.census.gov/profile?g=160XX00US0650076), [Murrieta Zoning Map](https://www.murrietaca.gov/DocumentCenter/View/4374/Murrieta-Zoning-Mappdf), and [Riverside Transit Agency](https://www.riversidetransit.com/index.php/riding-the-bus/maps-schedules) have been great resources for data collection.

## Key Features

The routes are created from running Dijkstra's algorithm utilizing an adjacency list with all of the distances between each node stored within the list. These are accessed and searched through when each node is hit within a search and the best route is found.

To determine the routes that are created, I picked out the best points within the city of Murrieta that will span across all of the main roads of the city and that will serve the public with realistic routes for reasonable and usable destinations.

These routes are then generated using Geoapify's Routing API that searches through the adjacency list with Dijkstra's algorithm. These are then plotted onto a Folium map within Python, which can be viewed below.

![Map](https://github.com/ttrevorreese/finalyearproject/blob/c6c3b7a84e476f15e5cd9460f9199402c3a9f453/website/images/map.jpg)

## Build Structure

The program is built upon the most current version of Python3 (as of February 2023) using .ipynb notebooks.

There is a *prototype* website located within the `website` folder in this repository. To view this prototype,

- Clone this repository into your Visual Studio Code.
- Open the `website` folder.
- Right-click the `index.html` file within the folder and click "Open With Live Server."

## Bug Reporting

If there are any bugs or issues with the program or installation, please use the issues tab located within this GitHub repository. This will make it easy for user communication with me, as I will be able to locate the bug(s) and try to create a solution as fast as possible.

## Artefacts Used

<img align="left" alt="Python" width="26px" src=https://github.com/devicons/devicon/blob/2ae2a900d2f041da66e950e4d48052658d850630/icons/python/python-original.svg style="padding-right:20px;"/>

Python for the programming language of the project.

<img align="left" alt="GitHub" width="26px" src=https://github.com/devicons/devicon/blob/2ae2a900d2f041da66e950e4d48052658d850630/icons/github/github-original.svg style="padding-right:20px;"/>

Github for the version control and public repository hosting of the project.

<img align="left" alt="Folium" width="26px" src=https://python-visualization.github.io/folium/_images/folium_logo.jpg style="padding-right:20px;"/>

Folium package for the map implementation within Python.

<img align="left" alt="Geoapify" width="26px" src=https://res.cloudinary.com/crunchbase-production/image/upload/c_lpad,h_170,w_170,f_auto,b_white,q_auto:eco,dpr_1/sslcmlhkroqkijraeqsh style="padding-right:20px;"/>

Geoapify Routing API for routing and map plotting within Python and the Folium package.

<img align="left" alt="Pandas" width="26px" src=https://github.com/devicons/devicon/blob/2ae2a900d2f041da66e950e4d48052658d850630/icons/pandas/pandas-original.svg style="padding-right:20px;"/>

Pandas for a lot of the mathematics and computing within the Python programming.

<img align="left" alt="Markdown" width="26px" src=https://github.com/devicons/devicon/blob/2ae2a900d2f041da66e950e4d48052658d850630/icons/markdown/markdown-original.svg style="padding-right:20px;"/>

Markdown for the presentation and layout of the public GitHub repository.

<img align="left" alt="Google Cloud" width="26px" src=https://github.com/devicons/devicon/blob/2ae2a900d2f041da66e950e4d48052658d850630/icons/googlecloud/googlecloud-original.svg style="padding-right:20px;"/>

Google Cloud for the hosting of my documents in progress.

<img align="left" alt="Photoshop" width="26px" src=https://github.com/devicons/devicon/blob/2ae2a900d2f041da66e950e4d48052658d850630/icons/photoshop/photoshop-plain.svg style="padding-right:20px;"/>

Photoshop for the moodboarding for the logo creation and the mockups for the presentation.

<img align="left" alt="Illustrator" width="26px" src=https://github.com/devicons/devicon/blob/2ae2a900d2f041da66e950e4d48052658d850630/icons/illustrator/illustrator-plain.svg style="padding-right:20px;"/>

Illustrator for the creation of the logo.

<img align="left" alt="Google Maps" width="26px" src=https://lh3.googleusercontent.com/9tLfTpdILdHDAvGrRm7GdbjWdpbWSMOa0csoQ8pUba9tLP8tq7M4Quks1xuMQAVnAxVfryiDXRzZ-KDnkPv8Sm4g_YFom1ltQHjQ6Q style="padding-right:20px;"/>

Google Maps for the data collection and testing stages of the project.

<img align="left" alt="Google Colab" width="26px" src=https://upload.wikimedia.org/wikipedia/commons/thumb/d/d0/Google_Colaboratory_SVG_Logo.svg/800px-Google_Colaboratory_SVG_Logo.svg.png?20221103151432 style="padding-right:20px;"/>

Google Colab for the hosting of the .ipynb Jupyter notebooks during the development and implementation stages of the project.

## Further Development

I have goals to implement another algorithm into the program that will automatically search for the best routes. To do this, I will need to implement some scores for each of the nodes so the algorithm has an incentive to find the best routes.

Another goal is to create a fully-functional, completely interactive website that will display all of the routes on a website robustly.

A long-term goal is to introduce this project in its final form (once the previous two goals have been achieved) to the Murrieta City Council in order to try and get it implemented and brought to fruition to serve the public.

## Contributors

- [Trevor Reese](https://github.com/ttrevorreese)
- Dr. Yuanlin Gu, Project Advisor
- Mohammad Ahmad, Secondary Project Advisor
- Dr. Charles Clarke, Program Convenor
- Dr. Kevin Chalmers, Deputy Head of School
- Dr. Wei Li, Stand-In Project Advisor

## Credits

Thank you to Muhamad Reza Adityawarman of Freebiesbug for the free HTML and CSS website template.

## Acknowledgements

First and foremost, I would like to thank my primary advisor, Dr. Yuanlin Gu, for his continued guidance and support. There were a lot of ups and downs for me during the duration of this project, but he always gave me the support and reassurance I needed to stay on track and to complete the project to the best of my abilities. He always provided great feedback that helped me fill in the pieces of the puzzle and overcome obstacles. I am genuinely grateful for his help and support. Additionally, I would like to thank my secondary supervisor, Mr. Mohammad Ahmad, for ensuring that I was not putting all of my time into one part of the project and giving me the motivation and reassurance I needed to get to the next stage of the project. I would also like to thank Dr. Wei Li for stepping in at the last minute for guidance in the final stages.

I would also like to thank my classmates and friends, Matthew Lowrie, Mandev Seahra, Sayeed Bin Yahya, Zakariya Oulhadj, Tyler Supersad, Tomasz Bernacki, Andrew Prystiaiko, Samoil-Bogdan Adascalului, Sidharth Jain, and all others for their support, feedback, and collaboration throughout the duration of the course. It was a privilege working with each and every one of them and gaining crucial experience working with others.

I also owe a lot to my friends for being my family away from home. I am incredibly fortunate to have you all in my life and to have met you during such a crucial point in my life: Gio, Irene, Jocelyn, Ella, Victoria, Elizabeth, Sophie, Fabian, Jacob, Pedro, Aisling, Chloe, Kaya, Izzy, Alaa, Dylan, Lewis, Matthew, and many more.

For the ones who supported me back in Murrieta, thank you. It was a massive step for me and my life to come here, and I am thankful for each and every one of you who stuck by my side: Michael, Sam, Reese, Caleb, and many others. Thank you for your love and support.

Most importantly, I would like to thank my family. I am who I am because of each and every one of you. Mom, Dad, thank you for your continuous support and allowing me to follow my dreams halfway across the world. Thank you for your guidance, your wisdom, and your love. I would not have gotten here without you. I love you. And to my amazing siblings, Austin, Devin, Sydney, and Natalie: I love you. I have learned so much from each and every one of you and you all inspire me to be a better person. I am forever grateful to have such a loving and supportive family by my side at all times.
