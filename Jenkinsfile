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

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t ip-checker .'
            }
        }

        stage('Run Container') {
            steps {
                sh 'docker run --rm ip-checker'
            }
        }
    }
}
