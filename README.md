# Django Internet Speed Tester

Django Internet Speed Tester is a web application built with Django that allows users to test their internet speed. It provides functionalities to measure download and upload speeds as well as ping.

![Demo](media/demo.png)

## Features

- Measure download speed
- Measure upload speed
- Check ping latency
- User-friendly interface
- Historical speed test results

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/Silvokyda/internet-speed-tester.git
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Run migrations:

    ```bash
    python manage.py migrate
    ```

4. Start the development server:

    ```bash
    python manage.py runserver
    ```

5. Access the application at `http://localhost:8000`

## Usage

1. Navigate to the home page.
2. Click on the "Start Speed Test" button.
3. Wait for the test to complete.
4. View the results displayed on the page.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request if you find any bugs or have any suggestions for improvements.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
