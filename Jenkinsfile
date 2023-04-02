
pipeline {
  agent any
  stages {
    stage('version') {
      steps {
        sh 'python3 --version'
      }
    }
    stage('jenkins') {
      steps {
        sh 'python3 jenkins_python.py'
      }
    }
  }
}
