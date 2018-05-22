pipeline {
    agent {
        dockerfile true
    }
    stages {
        stage('build') {
            steps {
                sh '''
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
    post {
        success {
            archiveArtifacts artifacts: 'dist/*.whl', fingerprint: true
        }
    }
}
