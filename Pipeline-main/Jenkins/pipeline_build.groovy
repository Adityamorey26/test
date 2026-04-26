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
    }
}