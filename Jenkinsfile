pipeline {

    agent any
    stages {
        stage('Test Linting') {
            steps {
                sh 'find . -type f -name "*.py" | xargs pylint'
            }
        }
        stage('Docker Build') {
            steps {
                sh '''
                echo $USER
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
                docker login --username $DOCKER_HUB_USERNAME --password $DOCKER_HUB_PASSWORD
                docker push dsdatsme/redis-hit-counter
                docker push dsdatsme/python2-hit-counter
                '''
            }
        }
        stage('Docker Push') {
            steps {
                sh '''
                cd infra
                aws cloudformation update-stack --stack-name devops-capstone --template-body file://setup_infra.yml --parameters file://parameters.json --region us-east-1 --capabilities CAPABILITY_NAMED_IAM
                '''
            }
        }
    }
}
