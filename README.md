# 🍽️ Django Recipe App  

A simple Django-based web application that allows users to add, store, and search for their favorite recipes.  

## 🚀 Features  
✅ Add recipes with a name, description, and image  
✅ Store recipes in a database  
✅ View all added recipes  
✅ Search for recipes by name  
✅ Show a 404 page if a recipe is not found  

## 🛠️ Technologies Used  
- Python & Django  
- HTML, CSS (for UI)  
- MySQL (installed using pip)  

## 📌 Setup Instructions  
Follow these steps to run the project locally:  
```sh
1️⃣ Clone the Repository  
git clone https://github.com/SandeepR8/django-recipe-app.git
cd django-recipe-app
2️⃣ Create a Virtual Environment
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate     # On Windows

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Apply Migrations
python manage.py migrate

5️⃣ Install MySQL cleint 
pip install mysqlclient

6️⃣ Run the Development Server
python manage.py runserver

7️⃣ Install Pillow(image processing)
python -m pip install pillow

