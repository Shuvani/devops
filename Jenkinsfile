pipeline {
    environment {
        registry = "shuvani/moscow_time:3.3.2"
        registryCredential = 'DockerHub'
    }
    agent any
    stages {

        stage('Build') {
            agent { docker { image 'python:3-slim' } }
            steps {
                sh 'pip install --no-cache-dir -r app_python/requirements.txt'
            }
        }

        stage('Linting and testing') {
            agent { docker { image 'python:3-slim' } }
            steps {
                parallel(
                    lint: {
                        sh 'flake8 app_python/*.py'
                    },
                    test: {
                        sh 'pytest app_python/test.py'
                    }
                )
            }
        }

        stage('Deploy') {
            steps {
                script {
                    dockerImage = docker.build(registry, "./app_python")
                    docker.withRegistry( '', registryCredential ) {
                        dockerImage.push()
                    }
                }
            }
        }
    }
}