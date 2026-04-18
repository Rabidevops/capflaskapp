pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "raveendra137/cap-cloud-app"
         IMAGE_TAG = "${BUILD_NUMBER}"
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
                    sh "docker build -t $DOCKER_IMAGE:${BUILD_NUMBER} ."
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
                    sh "docker push $DOCKER_IMAGE:${BUILD_NUMBER}"
                }
            }
        }

        stage('Run Container') {
            steps {
                script {
                    sh """
                    docker stop cap-container || true
                    docker rm cap-container || true
                    docker run -d -p 8082:5000 --name cap-container $DOCKER_IMAGE:${BUILD_NUMBER}
                    """
                }


             post {
        success {
            emailext (
                subject: "✅ SUCCESS: ${env.JOB_NAME} #${env.BUILD_NUMBER}",
                body: """
                <h2>Deployment Successful 🚀</h2>
                <p><b>Job:</b> ${env.JOB_NAME}</p>
                <p><b>Build:</b> ${env.BUILD_NUMBER}</p>
                <p><b>Docker Image:</b> ${IMAGE_NAME}:${IMAGE_TAG}</p>
                <p><b>Container:</b> ${CONTAINER_NAME}</p>
                <p><b>Status:</b> Running Successfully</p>
                <p><a href="${env.BUILD_URL}">View Build Logs</a></p>
                """,
                mimeType: 'text/html',
                to: "yourmail@gmail.com",
                attachLog: true
            )
        }

        failure {
            emailext (
                subject: "❌ FAILED: ${env.JOB_NAME} #${env.BUILD_NUMBER}",
                body: """
                <h2>Deployment Failed ❌</h2>
                <p>Check logs: <a href="${env.BUILD_URL}">${env.BUILD_URL}</a></p>
                """,
                mimeType: 'text/html',
                to: "yourmail@gmail.com",
                attachLog: true
            )
        }
    }
}
            }
        }
    }
}
