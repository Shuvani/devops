properties([pipelineTriggers([githubPush()])])

pipeline {
    agent { docker { image 'python:3-slim' } }
    stages {
        stage('Build') {
            steps {
                sh 'pip install --no-cache-dir -r app_python/requirements.txt'
            }
        }
        stage('Linting and testing') {
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
    }
}