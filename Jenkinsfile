pipeline {
    agent {
        dockerfile true
    }
    stages {
        stage('build') {
            steps {
                sh '''
                    pip install -Ur requirements.txt
                    make
                    pip install -U dist/*.whl
                '''
            }
        }
        stage('test') {
            steps {
                sh '''
                    python -c 'import dargor'
                '''
            }
        }
    }
}
