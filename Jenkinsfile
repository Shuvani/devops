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
                    dockerImage = docker.build(registry, "./app_python")
                    docker.withRegistry( '', registryCredential ) {
                        dockerImage.push()
                    }
                }
            }
        }
    }
}