pipeline {
    environment {
        registry = "shuvani/moscow_time:8.0.1"
        registryCredential = 'DockerHub'
    }
    agent any
    stages {

        stage('Build, lint and test') {
            agent { docker { image 'python:3-slim' } }
            steps {
                sh 'pip install --no-cache-dir -r app_python/requirements.txt'
                sh 'flake8 app_python/*.py'
                sh 'pytest app_python/test.py'
            }
        }

        stage('Deploy') {
            when {
                branch 'main'
            }
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

    post {
        always {
            cleanWs()
        }
    }
}
