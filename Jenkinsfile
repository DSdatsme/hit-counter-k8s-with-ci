pipeline {

    agent any
    stages {
        stage('Test Linting') {
            steps {
                sh 'find . -type f -name "*.py" | xargs pylint '
            }
        }
        stage('Docker Build') {
            steps {
                sh '''
                cd frontend
                docker build -t dsdatsme/python2-hit-counter  .
                cd ..
                docker build -t dsdatsme/redis-hit-counter -f backend/Dockerfile .
                '''
            }
        }
        stage('Docker Push') {
            steps {
                sh '''
                // docker login --username $DOCKER_HUB_USERNAME --password $DOCKER_HUB_PASSWORD
                // docker push dsdatsme/redis-hit-counter
                // docker push dsdatsme/python2-hit-counter
                '''
            }
        }
    }
}
