# notion-music-rating-tool
This repository contains a project developed with Flask and Integromat, which uses the Spotify API to copy music albums to a Notion database. The project allows the user to search for albums on Spotify and add them to their personal database on Notion, allowing for easy organization, album rating and access to album information.
# How to run the project
This project is based on Flask and Integromat to copy Spotify albums to a Notion database. Follow these steps to run the project on your computer:

## Prerequisites
* Have Python and pip installed.
* Have an account on **Spotify** and **Notion**.
* Have a Notion access [integration](https://www.notion.so/my-integrations).
* Have [Make(formerly Integromat)](https://make.com) webhook URL.
* Have the following Notion templates:
  * [Album template](https://laubert.notion.site/fd35628ecf7a4b4b82a361320b7ec593?v=f559053b19ec43549c66e01e90fa7024)
  * [Song template](https://laubert.notion.site/1a7cbd068101409ba808e45997a579f0?v=eb7f6e6b83a64a6b9aed79602fdb629b)
## Steps
1) Clone this repository to your computer.
2) Open a terminal and navigate to the project folder.
3) Install the necessary dependencies by running the following command: `pip install -r requirements.txt`
4) Create a file called `config.py` in the project folder and add the following environment variables:
   * **SPOTIFY_CLIENT_ID**: Your Spotify bot public ID.
   * **SPOTIFY_CLIENT_SECRET**: Your Spotify access token.
   * **INTEGROMAT_URL**: Your Integromat webhook URL.
5) In the project folder, open the file ``integromat_script.json`` and replace the following values:
    * ``{{TEMPLATE_ALBUM_ID}}`` with the ID of the album template in Notion.
    * ``{{TEMPLATE_SONG_ID}}`` with the ID of the song template in Notion.
6) Start the Flask server by running the following command: python app.py
7) Open a browser and type http://localhost:5000 to access the main page of the project.
8) Enter the link of a Spotify album on the page and press the submit button. The album will be copied to your Notion database.

Done! Now you have your project running. Remember that you can modify the code according to your needs and use it to copy more albums.

## alternative (hosting in repl.it)
1) Create a new project on Repl.it using Python.
2) Click on "Add File" button and add the project files (templates folder, app.py, config.py, spotifyNHook.py, requirements.txt) 
3) Click on "Settings" button and add the following environment variables:
    * **SPOTIFY_CLIENT_ID**: Your Spotify bot public ID.
    * **SPOTIFY_CLIENT_SECRET**: Your Spotify access token.
    * **INTEGROMAT_URL**: Your Integromat webhook URL.
4) Click on "Run" button to start the project
5) Open a browser and type https://your_project_name.repl.co to access the main page of the project.

Keep in mind that on Repl.it the script runs with a time out, if your script takes longer to run than that time, Repl.it will stop the execution, to avoid this, it is recommended to use a hosting service or a personal server to run your script.