pipeline {
  agent none
  stages {
    stage('Read Email') {
      parallel {
        stage('Read Email') {
          environment {
            downloadfile = ''
          }
          steps {
            echo 'Reading Email'
            writeFile(file: 'kjkj', text: 'ktext', encoding: 'enc')
          }
        }
        stage('Match Text') {
          steps {
            echo 'Matching Text'
          }
        }
        stage('Move to Folder') {
          steps {
            echo 'Moving Email to Folder'
          }
        }
      }
    }
    stage('Download Attachment') {
      parallel {
        stage('Download Attachment') {
          steps {
            echo 'Download Attachment'
          }
        }
        stage('Download Email Attachment') {
          steps {
            echo 'Downloading Email Attachment'
          }
        }
      }
    }
    stage('Format Data') {
      parallel {
        stage('Format Data') {
          steps {
            echo 'Format Data'
          }
        }
        stage('OCR - PDF to Text') {
          steps {
            echo 'Performing OCR'
          }
        }
        stage('Structure -TXT to XLS') {
          environment {
            downloadfilepath = 'C:\\Users\\User\\Desktop'
          }
          steps {
            echo 'Structuring Data TXT to XLS'
          }
        }
      }
    }
  }
  environment {
    data = '12as'
  }
}