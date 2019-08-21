pipeline {
    agent any
    triggers {
        pollSCM('') 
    }
    stages {
        stage('Build') {
            steps {
                sh 'docker build --tag=hellocicd .'
                sh 'docker image tag hellocicd localhost:5000/flask:version1'
                sh 'docker push localhost:5000/flask:version1'
            }
        }
        stage('Test') {
            steps {
                sh 'pytest test_run.py'
            }
        }
        stage('Deploy') {
            steps {
                sh 'docker swarm init'
                sh 'docker stack deploy -c docker-compose.yml getstartedlab'
            }
        }
    }
}