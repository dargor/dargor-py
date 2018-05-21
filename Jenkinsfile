pipeline {
    agent {
        docker {
            image 'python:3-slim'
        }
    }
    stages {
        stage('build') {
            steps {
                sh '''
                    apt-get -qy update
                    apt-get -qy install make
                    make
                    pip install -U dist/*.whl
                '''
            }
        }
    }
}
