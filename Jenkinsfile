pipeline {
      agent any
      enviroment {
          dockerImage =''
          registry ='bndah/mywelcomepage'
          registryCredential ='bndah-dockerhub'
      
          stages {
               stage('Clone Repository') {
               steps {
               checkout scm
               }
          }
          stage('Build Image') {
               steps {
               sh "docker build -t bndah/mywelcomepage ."
               }
         }
         
         stage('Push image') {
               steps {
                     script {
                           docker.withRegistry( '', registryCredential ) {
                           dockerImage.push()
                  }
              }
           }            
         }
         stage('Copy the files') {
               steps {
               sh "scp -o StrictHostKeyChecking=no deploy.yaml ubuntu@3.83.45.0:/home/ubuntu"
               sh "scp -o StrictHostKeyChecking=no ans.yml ubuntu@3.83.45.0:/home/ubuntu"
               }
         }       
         stage('Create deployment and Service') {
               steps {
               sh 'ansible -m ping all'
               sh 'ansible-playbook ans.yml'
               }
         }
         stage('expose my app') {
               steps {
               sh 'ssh ubuntu@3.83.45.0 minikube service flask'
               }
         }
         stage('Terraform Init'){
             steps{
                 sh 'terraform init'
             }
         }
         stage ("terraform Action") {
             steps {
                echo "Terraform action is --> ${action}"
                sh ('terraform ${action} --auto-approve') 
             }
         }

         stage('Testing') {
              steps {
                    echo 'Testing...'
                    }
             }
          }
    }
}
