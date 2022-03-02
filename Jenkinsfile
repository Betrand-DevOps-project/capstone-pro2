pipeline {
      agent any
      environment{
      DOCKERHUB_CREDENTIALS = credentials('DockerHub')
    }

          stages {
               stage('Clone Repository') {
               steps {
               checkout scm
               }
          }
          stage('Build Image') {
               steps {
               sh "docker build -t  bndah/mywelcomepage ."
               }
         }
          stage('Login to DockerHub'){
               steps{
                     sh 'echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'
               }
         }
         stage('Push image') {
               steps {
               sh 'docker push  bndah/mywelcomepage'
               }
         }
         stage('copy deployment file') {
               steps {
               sh "scp -o StrictHostKeyChecking=no Deployment.yml ubuntu@3.83.45.0:/home/ubuntu"
               sh "scp -o StrictHostKeyChecking=no Ansible.yml ubuntu@3.83.45.0:/home/ubuntu"
               }
         }
         stage('Deploy k8') {
               steps {
                     
               sh 'ansible-playbook ans.yml'
               }
         }
         stage('Testing') {
              steps {
                    echo 'Testing...'
                    }
         }
}
}
