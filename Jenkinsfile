pipeline {
  agent none
  stages {
    stage('test') {
      parallel {
        stage('test') {
          steps {
            echo 'Hello'
          }
        }
        stage('test2') {
          steps {
            echo 'mn'
          }
        }
      }
    }
    stage('test23') {
      steps {
        echo 'aws'
      }
    }
  }
  environment {
    data = '12as'
  }
}