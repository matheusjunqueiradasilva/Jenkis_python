pipeline {
  agent any
  stages {
    stage('version') {
      steps {
        sh 'python3 --version'
      }
    }
    stage('python') {
      steps {
        sh 'python3 jenkins_python.py'
      }
    }
  }
}
