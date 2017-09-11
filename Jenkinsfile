
pipeline {
    agent any

    stages {
        stage('Build') {
            steps { 
                dir unit-test/trial/src/ 
                python my_sum.py -i 1 2
            }
        }
        stage('Test') {
            steps { 
                dir unit-test/trial/tests/ 
                python test_sum.py
            }
        }
    }
}
