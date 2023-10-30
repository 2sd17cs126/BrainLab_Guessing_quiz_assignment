# BrainLab_Guessing_quiz_assignment

Steps to run the app:
Open the cmd/Vscode and be on the BrainsLab_Guessing_quiz_assignment directory and run the below commands.
1)python -m venv myenv
2)myenv\Scripts\activate
3)cd capitals_game
4)pip install -r requirements.txt
5)python manage.py runserver( on running this you will see the server is started at http://127.0.0.1:8000/)
6)open the browser and enter http://127.0.0.1:8000/game



Project implementation overview:

I have developed this app using Django features:
1) Django Models to store the data from api https://countriesnow.space/api/v0.1/countries/capital 
2) Written script(location: management\commands\populate_countries.py ) to populate data from api to Model Country and to do achieve this i run the command 'python manage.py populate_countries' after making migrations
3)Used static  to collect static files , to achieve this used the command 'python manage.py collectstatic'.
4)Used Django default sqlite database
5)To view data in sqlite database i have used DB Browser tool,attaching snapshot in snap folder.
