properties([pipelineTriggers([githubPush()])])

pipeline {
    agent { docker { image 'python:3-slim' } }
    stages {
        node {
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
        }
    }
}