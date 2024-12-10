# Netflix Clone - Movie Streaming Platform

A Django-based movie streaming platform that replicates core Netflix functionalities. This application allows users to browse, rate, and manage their favorite movies while providing personalized recommendations based on user interactions.

## 🚀 Features

### Movie Management
- Browse extensive movie catalog
- View detailed movie information
- Watch movie trailers
- Track movie views and popularity

### User Interactions
- Rate movies (5-star rating system)
- Like/Unlike movies
- Comment on movies
- Create and manage personal watchlists

### Personalization
- Personalized movie recommendations based on user preferences
- User-specific watchlists
- User profile management

### UI Features
- Netflix-style carousel for featured movies
- Responsive design for all devices
- Dynamic movie cards with hover effects
- Genre-based filtering
- Trending movies section

## 🛠 Technical Stack

### Backend
- Django
- Django ORM
- Python

### Frontend
- HTML5
- CSS3
- JavaScript
- Bootstrap 5
- Font Awesome
- Bootstrap Icons

### Database
- SQLite (default)

## 📋 Prerequisites

- Python 3.x
- pip (Python package manager)
- Virtual environment (recommended)

## 🔧 Installation

1. Clone the repository
```bash
git clone https://github.com/vauzher/Movies-Streaming-App.git
cd netflix-clone
```
3. Create and activate virtual environment
```bash
python -m venv venv
source venv/bin/activate # On Windows: venv\Scripts\activate
```
4. Install dependencies
```bash
pip install -r requirements.txt
```
5. Apply migrations
```bash
python manage.py migrate
```
6. Create superuser (admin)
```bash
python manage.py createsuperuser
```
7. Run development server
```bash
python manage.py runserver
```


## 💡 Usage

1. Access the admin panel at `/admin` to manage movies and users
2. Add movies through the admin interface
3. Users can register and start interacting with movies
4. Browse movies on the homepage
5. View detailed information about each movie
6. Rate, like, and comment on movies
7. Create and manage personal watchlists

## 🔐 Authentication

- User registration and login required for:
  - Rating movies
  - Leaving comments
  - Creating watchlists
  - Liking movies

## 🎨 Customization

- Modify `base.html` for site-wide styling changes
- Update CSS variables in the style section for theme customization
- Add new features by extending existing views and templates

## 🤝 Contributing

1. Fork the repository
2. Create a new branch
3. Make your changes
4. Submit a pull request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- Netflix for inspiration
- Bootstrap team for the framework
- Django community for the amazing framework

## 📧 Contact

Vauzher - vauzher@bytesnipes.com
Project Link: https://github.com/vauzher/Movies-Streaming-App.git









