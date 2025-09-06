pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'git@github.com:Ferry-AT/ip-checker.git',
                    credentialsId: 'github-ssh'
            }
        }

        stage('Build & Start Services') {
            steps {
                // Build images and start containers with docker-compose
                sh 'docker compose up --build -d'
            }
        }

        stage('Run App') {
            steps {
                // Run the Python app inside its container
                sh 'docker compose run --rm ip_checker'
            }
        }
    }

    post {
        always {
            // Stop and clean up all containers
            sh 'docker compose down'
        }
    }
}
