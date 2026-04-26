pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/YOUR_USERNAME/pipeline.git'
            }
        }

        stage('Build') {
            steps {
                bat 'docker build -t flask-app -f docker/Dockerfile .'
            }
        }

        stage('Test') {
            steps {
                bat 'echo Running basic test...'
            }
        }

        stage('Deploy') {
            steps {
                bat 'docker rm -f flask-container || exit 0'
                bat 'docker run -d -p 5000:5000 --name flask-container flask-app'
            }
        }
    }
}