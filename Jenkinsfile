pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                sh 'docker build --tag=friendlyhello .'
                withDockerRegistry([ credentialsId: "YWpheW5hdGhjaDphamF5bmF0aEAzNTI=", url: "" ]) {
                    sh 'docker tag hello ajaynathch/flask:version2'
                    sh 'docker push ajaynathch/flask:version2'
                }
                
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