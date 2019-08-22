pipeline {
    agent any
    triggers {
        pollSCM('* * * * *') 
    }
    stages {
        stage('Build') {
            steps {
                sh 'docker build --tag=hellocicd .'
                sh 'docker image tag hellocicd localhost:5000/flask:version1'
                sh 'docker push localhost:5000/flask:version1'
            }
        }
        stage('Deploy') {
            steps {
            	sh 'docker swarm leave --force'
            	sh 'docker swarm init'
            	sh 'docker swarm join --token SWMTKN-1-15k0vmyy5lqsn7607i7dx3r7yf8mnfu7msoioljfp2edpbbdwc-d16vt2msbsx94tz9hl88e3l4w 192.168.1.52:2377'
            	sh 'docker stack rm getstartedlab'
                sh 'docker stack deploy -c docker-compose.yml getstartedlab'
            }
        }
    }
}