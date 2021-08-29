properties([pipelineTriggers([githubPush()])])

pipeline {
    environment {
        registry = "shuvani/moscow_time"
        registryCredential = 'DockerHub'
    }
    agent { docker { image 'python:3-slim' } }
    stages {
        stage('Build') {
            steps {
                sh """
                    pip install --no-cache-dir -r app_python/requirements.txt
                """
            }
        }
        stage('Linting') { // Run pylint against your code
            steps {
                sh """
                    flake8 app_python/*.py
                """
            }
        }
        stage('Test') {
            steps {
                sh """
                    pytest app_python/test.py
                """
            }
        }
        stage('Deploy') {
            steps {
                script {
                    docker.build registry + ":0.0.0"
                    docker.withRegistry( '', registryCredential ) {
                        dockerImage.push()
                    }
                }
            }
        }
    }
}