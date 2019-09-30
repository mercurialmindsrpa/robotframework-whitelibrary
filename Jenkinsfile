pipeline {
  agent none
  stages {
    stage('Read Email') {
      parallel {
        stage('Read Email') {
          steps {
            echo 'Hello'
          }
        }
        stage('Match Text') {
          steps {
            echo 'mn'
          }
        }
        stage('Move to Folder') {
          steps {
            sleep 1
            sleep 1
          }
        }
      }
    }
    stage('Download Attachment') {
      parallel {
        stage('Download Attachment') {
          steps {
            echo 'aws'
          }
        }
        stage('Download Email Attachment') {
          steps {
            sleep 1
          }
        }
      }
    }
    stage('Format Data') {
      parallel {
        stage('Format Data') {
          steps {
            sleep 1
          }
        }
        stage('OCR - PDF to Text') {
          steps {
            sleep 1
          }
        }
        stage('Structure -TXT to XLS') {
          steps {
            sleep 1
          }
        }
      }
    }
  }
  environment {
    data = '12as'
  }
}