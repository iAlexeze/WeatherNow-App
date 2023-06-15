WeatherNow App


WeatherNow is a breathtaking and innovative weather application built with Python Flask. It provides users with real-time weather information and forecasts for any location worldwide. This app leverages the power of Flask, Docker, and Kubernetes to deliver a seamless and scalable weather experience.

Features:

Get current weather information for any location
View temperature, unit, and forecast details
User-friendly interface with a sleek and modern design
Responsive layout for optimal viewing on various devices
Built-in caching mechanism for improved performance
Easy deployment with Docker and Kubernetes


Installation and Usage

Docker

To run the WeatherNow app in a Docker environment, follow these steps:

Clone the repository:

git clone https://github.com/ialexeze/weathernow.git

Navigate to the project directory:

cd weathernow
Build the Docker image:

docker build -t weathernow:latest .

Run the Docker container:

docker run -d -p 5000:5000 weathernow:latest

Open your web browser and access the app at http://localhost:5000.

It is incoporated with Redis database for caching and efficiency of API calls


Kubernetes
To deploy the WeatherNow app in a Kubernetes cluster, use the provided Docker image ialexeze/weathernow:v1.0. Follow these steps:

Create a Kubernetes deployment:

kubectl create deployment weathernow --image=ialexeze/weathernow:v1.0
kubectl create deployment weathernow --image=redis:latest

Expose the deployment as a service:

kubectl expose deployment weathernow --port=5000 --target-port=5000

Access the app using the cluster IP and port assigned to the service.

Contributing
Contributions to WeatherNow are welcome! Here are a few ways you can contribute:

Report bugs and issues: If you come across any bugs or issues, please open an issue on the GitHub repository.
Suggest enhancements: If you have any ideas or suggestions to improve WeatherNow, feel free to share them.
Submit pull requests: If you'd like to contribute directly to the codebase, you can submit a pull request with your changes.
License
WeatherNow is released under the MIT License.

Credits
WeatherNow was created by the talented developers at iAlexDev. We extend our gratitude to the open-source community for their invaluable contributions.

Thank you for choosing WeatherNow! We hope you enjoy using our app and stay informed about the weather conditions wherever you go.







