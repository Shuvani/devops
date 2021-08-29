properties([pipelineTriggers([githubPush()])])

pipeline {
    environment {
        registry = "shuvani/moscow_time"
        registryCredential = 'DockerHub'
    }
    agent any
    stages {
        stage('Deploy') {
            steps {
                script {
                    dockerImage = docker.build(registry, "./app_python")  + ":0.0.0"
                    docker.withRegistry( '', registryCredential ) {
                        dockerImage.push()
                    }
                }
            }
        }
    }
}