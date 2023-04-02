
pipeline {
  agent any
  stages {
    stage('version') {
      steps {
        sh 'python3 --version'
      }
    }
    stage('cd') {
      steps {
        sh 'python3 jenkins_python.py'
      }
    }
}
