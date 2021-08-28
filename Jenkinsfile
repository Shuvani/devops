pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                script {
                  sh """
                  pip install -r app_python/requirements.txt
                  """
                }
            }
        }
        stage('Linting') { // Run pylint against your code
          steps {
            script {
              sh """
              flake8 app_python/*.py
              """
            }
          }
        }
        stage('Test') {
            steps {
                script {
                  sh """
                  pytest app_python/test.py
                  """
                }
            }
        }
    }
}