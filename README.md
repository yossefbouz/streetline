# Streetline

A Flask-based web application.

## Project Structure

```
streetline/
├── app.py              # Main Flask application
├── static/
│   └── css/
│       └── style.css   # Stylesheets
├── templates/          # HTML templates
│   ├── base.html
│   ├── home.html
│   ├── contact.html
│   ├── shop.html
│   └── tutorial.html
└── venv/              # Virtual environment
```

## Setup & Installation

1. Create a virtual environment:
```bash
python -m venv venv
```

2. Activate the virtual environment:
```bash
# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install flask
```

4. Run the application:
```bash
python app.py
```

## License

MIT
