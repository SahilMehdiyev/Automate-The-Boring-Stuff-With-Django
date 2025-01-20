# Automate The Boring Stuff With Django

This project is designed to demonstrate the use of Django for automating repetitive tasks and creating efficient web applications. It is inspired by the popular book *Automate the Boring Stuff with Python*, focusing on leveraging Django's powerful features for rapid development.

## Features

- User-friendly web interface
- Task automation capabilities
- Integration with third-party services (e.g., email, APIs)
- Secure and scalable architecture
- Modular and reusable code structure

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/SahilMehdiyev/Automate-The-Boring-Stuff-With-Django.git
   cd Automate-The-Boring-Stuff-With-Django
   ```

2. **Install dependencies:**
   Ensure you have [Poetry](https://python-poetry.org/) installed, then run:
   ```bash
   poetry install
   ```

3. **Set up environment variables:**
   Create a `.env` file in the root directory with the following variables:
   ```plaintext
   DEBUG=True
   SECRET_KEY=your-secret-key
   EMAIL_HOST=smtp.gmail.com
   EMAIL_PORT=587
   EMAIL_USE_TLS=True
   EMAIL_HOST_USER=your_email@gmail.com
   EMAIL_HOST_PASSWORD=your_email_password
   ```

4. **Apply migrations:**
   ```bash
   poetry run python manage.py migrate
   ```

5. **Run the development server:**
   ```bash
   poetry run python manage.py runserver
   ```

6. Open your browser and navigate to `http://127.0.0.1:8000`.

## Usage

- **Automated Tasks:** Add tasks through the web interface and monitor their execution.
- **Integration:** Configure third-party APIs in the settings to enhance functionality.
- **Customization:** Modify existing apps or add new ones to suit your needs.

## Contributing

Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them with clear messages.
4. Push your branch and open a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For questions or support, please reach out to:

- **Author:** Sahil Mehdiyev
- **Email:** sahil@example.com
- **GitHub:** [SahilMehdiyev](https://github.com/SahilMehdiyev)
