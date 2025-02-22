AretaAI Project:

Developers:
-Yatharth Jain
-Khyati Sikarwar

Overview:
AretaAI is a natural language processing (NLP) project that utilizes spaCy for entity recognition and query processing. The project consists of two main applications: aretaai-which utilizes spacy to perform NLP->Query convertions and returns the query to aretasearch which then uses SQL3 to search database and return the desired document.

Features:
- Entity recognition using spaCy
- Query processing and result display using user defined application aretasearch. 
- Search functionality for searching entities are achived through django api and open source git applications.

Requirements
- Python 3.12
- Django 5.1
- spaCy 3.4
- Git Bash
- Git Hub(and it's open source api)
- Chatgpt and deepseek for debugging suggetions.
- Kaggle(Used for premade banking database) Link-"https://www.kaggle.com/datasets/prakharrathi25/banking-dataset-marketing-targets/code"

Installation
1. Clone the repository: git clone https://github.com/sikarwarkhyati/aretaai.git.
2. Navigate to the project directory.
3. Create a virtual environment: python -m venv venv
4. Activate the virtual environment: venv\Scripts\activate (Windows) or source venv/bin/activate (Mac/Linux).
5. Install the required packages mentioned in requirments.
6. Run the migrations: python manage.py migrate.

Usage:
Note-(The development was not completed , thought the intended usage will enable you to navigate to the index page(Mentioned as query.html) which will accept NLP queries and return relevant data.)
1. Run the development server: python manage.py runserver
2. Access the application in your web browser: http://localhost:8000/
3. Use the query and search functionality to test the application.


License
This project is licensed under the MIT License. See the LICENSE file for details.

Acknowledgments
- spaCy for their excellent NLP library.
- Django for their robust web framework.

Reasons for using various dependencies:
- We have used django to help rapid devolopment and ensure scalablity, django enebles us to rapidly and robustly complete the devolopment process.
- We have used chatgpt and stackoverflow for identifying and resolving certain bugs.

Thank you areta for this wonderfull opotunity.
