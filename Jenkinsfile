pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "raveendra137/cap-cloud-app"
    }

    stages {

        stage('Clone Code') {
            steps {
                 git branch: 'main', changelog: false, poll: false, url: 'https://github.com/Rabidevops/capflaskapp.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    sh "docker build -t $DOCKER_IMAGE:latest ."
                }
            }
        }

        stage('Login to DockerHub') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'Dockercreds',
                    usernameVariable: 'USER',
                    passwordVariable: 'PASS'
                )]) {
                    sh "echo $PASS | docker login -u $USER --password-stdin"
                }
            }
        }

        stage('Push Image') {
            steps {
                script {
                    sh "docker push $DOCKER_IMAGE:latest"
                }
            }
        }

        stage('Run Container') {
            steps {
                script {
                    sh """
                    docker stop cap-container || true
                    docker rm cap-container || true
                    docker run -d -p 8082:5000 --name cap-container $DOCKER_IMAGE:latest
                    """
                }
            }
        }
    }
}
